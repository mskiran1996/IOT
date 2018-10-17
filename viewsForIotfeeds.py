from company.models import *
from shipment.models import *
from masterdata.models import *
from usermanagement.models import *
from uuid import uuid4
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone



def random_key():    
    return uuid4().hex[:8]



@csrf_exempt
def user_login(request):
    deviceid=request.POST.get('deviceId')
    driverlno=request.POST.get('dlNo')
    phno=request.POST.get('phoneNo') 
    try:
        truck = Trucks.objects.get(android_device_id = deviceid)
        driver = Driver.objects.get(driving_licence_no = driverlno)#phno field not defined in model structure
        if driver.is_verified and truck.is_ready_for_assignment:
           request.session['device_id'] = deviceid
           request.session['dl_No'] = driverlno
           request.session['user_key'] = random_key()+"-"+str(driver.id)
           driverid = str(driver.id)
           status = "1"
           truckid = str(truck.id)
           #message="User is valid, active and authenticated ,session started "
           response ={'status':status,'uId':driverid,'truckId':truckid}
    
    except:
           status = "0"
           message="Incorrect credentials"
    response = {'status':status,'message':message}
    return JsonResponse(response)


@csrf_exempt
def user_logout(request):
    try:
        del request.session['user_key']
        del request.session['device_id']
        del request.session['dl_No']
 
        message = 'logout success'  
    except KeyError:
                    message= 'You are already logged out'
    response ={'message':message}
    return JsonResponse(response)
    
 
@csrf_exempt    
def shipment_list(request):
    sourceid = request.POST.get('sourceId')
    destinationid = request.POST.get('destinationId')
    source_lat = request.POST.get('sourceLat')
    source_long = request.POST.get('sourceLong')
    date = request.POST.get('date')
    sort = request.POST.get('sortBy')
    filter_by = request.POST.get('filterBy') 
    page_start = request.POST.get('start')
    page_limit = request.POST.get('limit')
    shipmentlist = Shipment.objects.filter(origin_address = sourceid , destination_address = destinationid,pick_up = date)
    response = {}
    for s in shipmentlist:
        id_= str(s.id)              
        status = s.status
        #stackable = int(s.stackable) #boolean required int        
        loaddetails = Shipment_Load_Items.objects.filter(shipment_id = s.id) 
        details =[{"name":l.load_type,"type":l.dimension_type,"dimension":str(l.length)+"x"+str(l.width)+"x"+str(l.height),"qty":l.quantity,"stackable":int(s.stackable)} for l in loaddetails]       
        location = Location.objects.get(id =sourceid,latitude = source_lat ,longitude = source_long)
        address = Address.objects.get(city = str(location.name))
        srcTown = str(address.city)+"," +str(address.city.state)
        srcAddress = str(address.address1)+","+str(address.address2)
        location = Location.objects.get(id =destinationid)
        address = Address.objects.get(city = str(location.name))
        dstTown = str(address.city)+"," +str(address.city.state)
        dstAddress = str(address.address1)+","+str(address.address2)
        weight = s.total_weight
        pickTime = s.pick_up
        delTime = s.delivery
        pickCutTime=s.pickup_cutoff
        delCutTime = s.delivery_cutoff
        options = Shipment_Option.objects.get(shipment_id =s.id)
        o={"name":str(options.option),"info":str(options.info1)}
        dic =[{"id":id_,"status":status,"srcTown":srcTown,"srcAddress":srcAddress,
              "dstTown":dstTown,"dstAddress":dstAddress,"loadDetails":details,"weight":weight,
                "pickTime":pickTime,"delTime":delTime,"pickCutTime":pickCutTime,"delCutTime":delCutTime,"options":o}]
    response = {"status":"1","shipments":dic}
    return JsonResponse(response)    
        
        


@csrf_exempt
def request_for_shipment_pickup(request):
    userid = request.POST.get('uId')                                            
    shipmentid = request.POST.get('shipmentId')
    try:
        userkey = request.session.get('user_key')
        if userkey is not None:
           if userkey.split('-')[1] == userid:
              driverid = (Driver.objects.get(driver_licence_no=request.session['dl_No']).id
              truckid = (Trucks.objects.get(android_device_id = request.session['device_id']).id
              try:
                  s= Shipment.objects.get(shipment_id_no = shipmentid)
                  try:
                      sr = Shipment_Requests(shipment=s.id,driver=driverid,truck=truckid,request_status =1)
                      sr.save()
                      status =  "1"
                      message = "success"
                  except:
                         status = "0"
                         message = "Unable to complete request"
              except:
                     status ="0"
                     message ="Incorrect shipmentId"
              
           else:
                status ="0"
                message = "Incorrect userid"
    except KeyError:
                    status = "0"
                    message = "Please login to continue" 

    response = {'status':status,'message':message}
    return JsonResponse(response)


@csrf_exempt
def delivery_signoff(request):
    userid = request.POST.get("uId")
    shipmentid = request.POST.get("shipmentId")
    cust_name = request.POST.get("name")
    phno = request.POST.get("mobile")
    cmmnt = request.POST.get("comments")
    sign = request.POST.get("signature")#image field
    del_loc = pass  #get location form android device
    try:
        userkey = request.session.get('user_key')
        if userkey is not None:
           if userkey.split('-')[1] == userid:
              driverid = (Driver.objects.get(driver_licence_no=request.session['dl_No'])).id
              truckid = (Trucks.objects.get(android_device_id = request.session['device_id'])).id
              try:
                  #s = Shipment.objects.get(shipment_id_no = shipmentid)
                  sd = Shipment_Truck_Driver_Relation.objects.get(shipment_id = shipmentid )
                  if sd.driver.id == driverid:
                     try:
                         driver = Driver.objects.get(driver_licence_no=request.session['dl_No'])
                         di = Delivery_Information(name=cust_name, notes=cmnt, phone=phno, signature=sign, shipment=shipmentid, designation=driver.user.designation.name, delivery_date=timezone.now(), delivery_location=del_loc)
                         di.save()
                         status =  "1"
                     except:
                         status ="0"
                         message = "incorrect field details"
              except:
                     status ="0"
                     message = "Incorrect shipmentId"
              
           else:
                status ="0"
                message = "Incorrect userid"
    except KeyError:
                    status = "0"
                    message = "Please login to continue" 

    response = {'status':status,'message':message}
    return JsonResponse(response)
    


@csrf_exempt
def place_search(request):
    search_str = request.POST.get('searchString')
    response ={}

    cities = City.objects.filter(name__startswith = search_str)
    for city in cities:
        c = City.objects.get(name = city)
        response[c.id] = city

    states = State.objects.filter(name__startswith = search_str) 
    for state in states:
        s = State.objects.get(name = state)
        response[s.id] = state  

    countries = Country.objects.filter(name__startswith = search_str)
    for country in countries:
        cy = Country.objects.get(name = country)
        response[cy.id] = country
    return JsonResponse(response)





def update_truck_location(request):
    pass






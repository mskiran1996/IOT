from django.db import models
from shipment.models import *
from django.utils.translation import ugettext_lazy as _

class Notification(Base):
    nt_from = models.ForeignKey(User, blank=True, null=True)
    content_type = models.ForeignKey(ContentType,
            verbose_name=_('content type'),
            related_name="django_content_type_set_for_%(class)s")
    object_id = models.TextField(_('object ID'))
    notification_type = models.IntegerField(default = 0)
    comment = models.CharField(max_length=255, blank=True, null=True)
    submit_date = models.DateTimeField(auto_now_add = True)
    is_seen = models.BooleanField(default = False)


class Notification_History(models.Model):
    notification = models.ForeignKey(Notification, blank=True, null=True)
    to = models.ForeignKey(User, blank=True, null=True)
    seen = models.BooleanField(default = False)

    def __unicode__(self):
        try:
            if self.notification and self.to:
                return u" %s  -  %s"%(self.notification,self.to)
        except:
            return self.id

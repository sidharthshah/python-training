from datetime import datetime
from django.db import models

class LogEntry(models.Model):
    name = models.CharField(max_length=255)
    in_time = models.DateTimeField(default=datetime.now())
    out_time = models.DateTimeField(default=datetime.now())
    comments = models.TextField(blank=True, null=True, default='')

    class Meta:
        verbose_name = 'Johl!'
        verbose_name_plural = 'Johlies!'

    def __unicode__(self):
        return "%s checked in at %s" % (self.name, self.in_time)
    
    @classmethod
    def get_counts(self):
        return len(self.objects.all())

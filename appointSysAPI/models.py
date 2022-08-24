from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Appointments(models.Model):
    
    appoint_date = models.DateTimeField(max_length=max, blank=False,default='')
    description = models.CharField(max_length=200,blank=False, default='')
    appoint_status = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
from rest_framework import serializers 
from appointSysAPI.models import Appointments
 
 
class AppointmentsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Appointments
        fields = ('id',
                  'appoint_date',
                  'description',
                  'appoint_status',
                  'user')
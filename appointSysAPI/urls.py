from django.urls import path, include
#from django.urls import re_path as url
from .views import (
    AppointmentsListApiView,
    AppointmentDetailApiView
)

urlpatterns = [
    path('api', AppointmentsListApiView.as_view()),
    path('api/<int:appointment_id>/', AppointmentDetailApiView.as_view()),
]
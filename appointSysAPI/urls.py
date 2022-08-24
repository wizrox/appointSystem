from django.urls import path, include
from .views import (
    AppointmentsListApiView,
    AppointmentDetailApiView
)

urlpatterns = [
    path('api', AppointmentsListApiView.as_view()),
    path('api/<int:appointment_id>/', AppointmentDetailApiView.as_view()),
]
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Appointments
from .serializers import AppointmentsSerializer

class AppointmentsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Appointments items for given requested user
        '''

        appointments = Appointments.objects.filter(user = request.user.id)
        
        # appointments = Appointments.objects.all()

        serializer = AppointmentsSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Appointment with given data
        '''
        data = {
            'appoint_date': request.data.get('appoint_date'), 
            'description': request.data.get('description'),
            'user': request.user.id
        }
        serializer = AppointmentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, appointment_id, user_id):
        '''
        Helper method to get the object with given appointment_id, and user_id
        '''
        try:
            return Appointments.objects.get(id=appointment_id, user = user_id)
        except Appointments.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, appointment_id, *args, **kwargs):
        '''
        Retrieves the Todo with given appointment_id
        '''
        appointment_instance = self.get_object(appointment_id, request.user.id)
        if not appointment_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AppointmentsSerializer(appointment_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, appointment_id, *args, **kwargs):
        '''
        Updates the todo item with given appointment_id if exists
        '''
        appointment_instance = self.get_object(appointment_id, request.user.id)
        if not appointment_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'appoint_date': request.data.get('appoint_date'), 
            'description': request.data.get('description'),
            'appoint_status': request.data.get('appoint_status'),
            'user': request.user.id
        }

        serializer = AppointmentsSerializer(instance = appointment_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, appointment_id, *args, **kwargs):
        '''
        Deletes the todo item with given appointment_id if exists
        '''
        appointment_instance = self.get_object(appointment_id, request.user.id)
        if not appointment_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        appointment_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

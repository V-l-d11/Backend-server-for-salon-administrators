from django.http import HttpRequest, HttpResponse
from .models import User, Worker,Service,Klient,Appointment,RecordNew
from .serializer import UserSerializer, ServiceSerializer,  WorkerSerializer, TaskSerializer, CasesListSerializer,KlientSerializer,StaffSerializer,AppointmentSerializer,RecordNewSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


# User by id - get, update, delete
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Get user
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Hello World
def helloWorld(HttpRequest):
    return HttpResponse("Hello World")


#Worker by id- get, update, delete
class WorkerM(generics.RetrieveUpdateDestroyAPIView):
    queryset=Worker.objects.all()
    serializer_class=WorkerSerializer

class WorkerListM(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

#Service by id- get,update,delete

class ServiceM(generics.RetrieveUpdateDestroyAPIView):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer

class ServiceListM(generics.ListCreateAPIView):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer


#Klient by id-get, update,delete

class KlientM(generics.RetrieveUpdateDestroyAPIView):
    queryset=Klient.objects.all()
    serializer_class=KlientSerializer

class KlientListM(generics.ListCreateAPIView):
    queryset=Klient.objects.all()
    serializer_class=KlientSerializer

##################################
@api_view(['GET'])
def available_staff(request, datetime_requested, service_required):
    available_staff = Appointment.objects.available_staff(datetime_requested, service_required)
    serializer = StaffSerializer(available_staff, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        client_id=serializer.validated_data['client']
        print(client_id,"ClientIDD")
        staff_id=serializer.validated_data['staff']
        start_time=serializer.validated_data['start_time']
        end_time=serializer.validated_data['end_time']
        if is_staff_available(staff_id,start_time,end_time):
            serializer.save()
            print("hello")
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Staff is not available at the specified time'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def is_staff_available(staff_id, start_time, end_time):
    appointments = Appointment.objects.filter(staff_id=staff_id)
    
    for appointment in appointments:
        if start_time < appointment.end_time and end_time > appointment.start_time:
            print(f"Appointment conflict: {start_time} - {end_time} intersects with existing appointment: {appointment.start_time} - {appointment.end_time}")
            return False
    return True

#######################################################
#Availibale Staff

class RecordListCreateAPIView(generics.ListCreateAPIView):
    queryset=RecordNew.objects.all()
    serializer_class=RecordNewSerializer

class RecordCreateAPIView(generics.CreateAPIView):
    queryset=RecordNew.objects.all()
    serializer_class=RecordNewSerializer

class RecordUpdateAPIView(generics.UpdateAPIView):
    queryset = RecordNew.objects.all()
    serializer_class = RecordNewSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Извлекаем данные из запроса
        start_time = serializer.validated_data.get('start_time', instance.start_time)
        end_time = serializer.validated_data.get('end_time', instance.end_time)
        master = serializer.validated_data.get('master', instance.master)

        # Проверяем пересечение с другими записями, исключая текущую запись
        conflicting_records = RecordNew.objects.filter(
            master=master,
            start_time__lt=end_time,
            end_time__gt=start_time,
        ).exclude(pk=instance.pk)
        if conflicting_records.exists():
            raise ValidationError("Мастер уже занят в это время")

        # Обновляем запись
        self.perform_update(serializer)
        return Response(serializer.data)
    





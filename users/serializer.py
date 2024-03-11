from rest_framework import serializers
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .models import User, Service, Worker, CasesList, Task, Klient,Staff,Appointment,RecordNew

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'

####################
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields='__all__'



#################

class WorkerSerializer(serializers.ModelSerializer):
    servicesList=serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)
    class Meta:
        model=Worker
        fields=['id','name','services','work_schedule']
    

##########################################

class KlientSerializer(serializers.ModelSerializer):

    class Meta:
        model=Klient
        fields=['id','name','number','like']



###########################################
class CasesListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CasesList
        fields='__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'

##########################################################



class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


#####New Records

class RecordNewSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecordNew
        fields='__all__'
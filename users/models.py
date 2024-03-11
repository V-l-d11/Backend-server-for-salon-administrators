from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

class User(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    gender=models.CharField(max_length=255)

    def __str__(self):
        return self.name

#Services
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=10)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name



#Klient
class Klient(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=30)
    like=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=100)
    specializations = models.ManyToManyField(Service, related_name='staff_specializations')


#######
class AppointmentManager(models.Manager):
    def available_staff(self,datetime_requested,service_required):
        busy_staff_ids=self.filter(
            start_time__lte=datetime_requested,
            end_time__gte=datetime_requested
        ).values_list('staff_id',flat=True)
        available_staff = Staff.objects.exclude(id__in=busy_staff_ids).filter(specializations__name=service_required)
        
        return available_staff

class Appointment(models.Model):
    client=models.ForeignKey(Klient, on_delete=models.CASCADE)
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    objects=AppointmentManager()




#Workers
class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    work_time = ArrayField(models.DateTimeField(),null=True)
    servicesList=models.ManyToManyField(Service, related_name='workers',blank=True)
    
    def is_avalable(self,start_time,end_time):
        conflicting_records= Record.objects.filter(
            master=self,
            start_time__lt= end_time,
            end_time__gt= start_time
        )
        return not conflicting_records.existing()

    def __str__(self):
        return self.name






##Records

class Record(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    couse_time=models.DateTimeField(null=True)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    klient=models.ForeignKey(Klient,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RecordNew(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    client=models.ForeignKey(Klient,on_delete=models.CASCADE)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    master=models.ForeignKey(Worker, on_delete=models.CASCADE)

    def clean(self):
        conflicting_records = RecordNew.objects.filter(
            master=self.master,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(pk=self.pk)  # Исключаем текущую запись при обновлении
        if conflicting_records.exists():
            raise ValidationError("Мастер уже занят в это время")

    def save(self,*args,**kwargs):
        self.clean()
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.client} - {self.service} - {self.start_time}"        
   

#######Cases

class CasesList(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    status=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    dateDedline=models.DateTimeField()
    date=models.DateTimeField()
    cases_list=models.ForeignKey(CasesList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


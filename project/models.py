from django.db import models

# Create your models here.
class userdetails(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.IntegerField()
    emailid=models.CharField(max_length=30)
    username=models.CharField(unique=True,max_length=30)
    password=models.CharField(max_length=30)
    status=models.IntegerField()
   
    def __str__(self):
        return self.name

class impdetails(models.Model):
    userdetails=models.ForeignKey('userdetails',on_delete=models.CASCADE)
    age=models.IntegerField()
    Bldgrp=models.CharField(max_length=30)
    apartment=models.CharField(max_length=30)
    landmark=models.CharField(max_length=30)
    locality=models.CharField(max_length=30)
    City=models.CharField(max_length=30)

    def __str__(self):
        return self.Bldgrp
    
    class Meta:
        ordering=['Bldgrp']

class relativedetails(models.Model):
    userdetails=models.ForeignKey('userdetails',on_delete=models.CASCADE)
    rname=models.CharField(max_length=30)
    age=models.IntegerField()
    Bldgrp=models.CharField(max_length=30)

    def __str__(self):
        return self.rname

    class Meta:
        ordering=['rname']

class hospital_list(models.Model):
    userdetails=models.ForeignKey('userdetails',on_delete=models.CASCADE)
    hospital_name=models.CharField(max_length=30)
    locality=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
    contact=models.IntegerField()

    def __str__(self):
        return self.hospital_name

    class Meta:
        ordering=['hospital_name']

class history(models.Model):
    userdetails=models.ForeignKey('userdetails',on_delete=models.CASCADE)
    no_of_persons=models.IntegerField()
    patient_type=models.CharField(max_length=30)
    date=models.CharField(max_length=30)

    def __str__(self):
        return self.no_of_persons

    class Meta:
        ordering=['no_of_persons']








    
from django.db import models


class cars(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    year = models.IntegerField()
    Seats = models.IntegerField()
    Color = models.CharField(max_length=10)
    VIN = models.CharField(max_length=20)
    Current_Mileage = models.CharField(max_length=10)
    Service_Interval = models.CharField(max_length=10)
    Next_Service = models.CharField(max_length=10)


class trucks(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    year = models.IntegerField()
    Seats = models.IntegerField()
    Bed_Length = models.CharField(max_length=10)
    Color = models.CharField(max_length=10)
    VIN = models.CharField(max_length=20)
    Current_Mileage = models.CharField(max_length=10)
    Service_Interval = models.CharField(max_length=10)
    Next_Service = models.CharField(max_length=10)



class boats(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    year = models.IntegerField()
    Length = models.CharField(max_length=10)
    Width = models.CharField(max_length=10)
    HIN = models.CharField(max_length=20)
    Current_Hours = models.CharField(max_length=10)
    Service_Interval = models.CharField(max_length=10)
    Next_Service = models.CharField(max_length=10)

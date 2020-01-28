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
    Color = models.CharField(max_length=10)
    VIN = models.CharField(max_length=20)
    Current_Mileage = models.CharField(max_length=10)
    Service_Interval = models.CharField(max_length=10)
    Next_Service = models.CharField(max_length=10)
    Bed_Length = models.DecimalField(max_digits=10,decimal_places=4)


class boats(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    year = models.IntegerField(4)
    Length = models.DecimalField(max_digits=10,decimal_places=4)
    Width = models.DecimalField(max_digits=10,decimal_places=4)
    HIN = models.CharField(max_length=20)
    Current_Hours = models.IntegerField()
    Service_Interval = models.CharField(max_length=10)
    Next_Service = models.CharField(max_length=10)

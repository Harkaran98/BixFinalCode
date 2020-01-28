from rest_framework import viewsets
from . import models
from . import serializers


class CarViewset(viewsets.ModelViewSet):
    queryset = models.cars.objects.all()
    serializer_class = serializers.CarSerializer


class TruckViewset(viewsets.ModelViewSet):
    queryset = models.trucks.objects.all()
    serializer_class = serializers.TruckSerializer


class BoatViewset(viewsets.ModelViewSet):
    queryset = models.boats.objects.all()
    serializer_class = serializers.BoatSerializer

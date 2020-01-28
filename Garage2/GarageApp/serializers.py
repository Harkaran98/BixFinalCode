from rest_framework import serializers
from .models import cars, trucks, boats


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = cars
        fields = '__all__'


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = trucks
        fields = '__all__'


class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = boats
        fields = '__all__'

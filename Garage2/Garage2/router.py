from GarageApp.viewsets import CarViewset, TruckViewset, BoatViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cars',CarViewset)
router.register('trucks',TruckViewset)
router.register('boats', BoatViewset)
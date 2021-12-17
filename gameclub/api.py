from rest_framework import routers
from mainapp import views

router = routers.DefaultRouter()
router.register(r'device', views.DeviceViewSet, basename='device')
router.register(r'gamer', views.GamerViewSet)
router.register(r'rented_device', views.RentedDeviceViewSet)

for url in router.urls:
    print(url, '/n')
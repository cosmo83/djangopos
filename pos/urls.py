from django.urls import include, path
from rest_framework import routers
from .views import SaleViewSet,SaleLineViewSet


router = routers.DefaultRouter()
router.register(r'sales', SaleViewSet)
router.register(r'salelines', SaleLineViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django.urls import include, path
from rest_framework import routers
from .views import SaleViewSet,SaleLineViewSet,SalesPageView
from django.contrib.auth.decorators import login_required, permission_required


router = routers.DefaultRouter()
router.register(r'sales', SaleViewSet)
router.register(r'salelines', SaleLineViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sales/', login_required(SalesPageView.as_view()), name='sales')
]

from django.urls import include, path
from rest_framework import routers
from .views import SaleViewSet,SaleLineViewSet,InventoryViewSet,SalesPageView
from django.contrib.auth.decorators import login_required, permission_required
from . import views

router = routers.DefaultRouter()
router.register(r'sales', SaleViewSet)
router.register(r'salelines', SaleLineViewSet)
router.register(r'inventory', InventoryViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
    path('api/productsearch/<str:searchcode>/',views.productsearch_list,name='productsearch'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sales/', login_required(SalesPageView.as_view()), name='sales')
]

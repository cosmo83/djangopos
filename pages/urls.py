from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from .views import homePageView,SalesPageView

urlpatterns = [
    path('', login_required(homePageView.as_view()), name='home'),
    path('sales', login_required(SalesPageView.as_view()), name='sales')
]


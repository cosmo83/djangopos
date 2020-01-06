from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from .views import homePageView,homePage1View,homePage2View,homePage3View,switch

urlpatterns = [
    path('', login_required(homePageView.as_view()), name='index'),
    path('dashboard1', login_required(homePage1View.as_view()), name='dashboard1'),
    path('dashboard2', login_required(homePage2View.as_view()), name='dashboard2'),
    path('dashboard3', login_required(homePage3View.as_view()), name='dashboard3'),
    path('switch/<int:storeid>/', login_required(switch), name='switchstore')
]

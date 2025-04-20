
from django.urls import path
from . import views
# store/urls.py

from .views import store_view


urlpatterns = [
    

    path('', views.store_home, name='store_home'),
    path('store/', store_view, name='store'),
    path('order/<int:product_id>/', views.place_order, name='place_order'),
    path('order/success/', views.order_success, name='order_success'),

]










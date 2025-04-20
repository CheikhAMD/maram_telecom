from django.urls import path
from . import views

urlpatterns = [
    path('', views.repair_form_view, name='repair'),
    path('success/', views.repair_success_view, name='repair_success'),
]


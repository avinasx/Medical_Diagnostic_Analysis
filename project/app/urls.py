from django.urls import path
from django.urls import reverse
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.test, name='test'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
    path('patient/', views.patient, name='patient'),
    
]
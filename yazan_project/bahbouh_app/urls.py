from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('yazan',views.yazan),
    path('nasri',views.nasri)
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.super_list),
    # path('hero/', views.super_list),
    # path('villian/', views.super_list),
]


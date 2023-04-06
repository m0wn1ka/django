from django.urls import path
from . import views

urlpatterns = [
    path('gandhi/', views.gandhi),
    path('nehru/',views.nehru),
    path('',views.default),
]
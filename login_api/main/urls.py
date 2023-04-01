# from api.views import RegisterApi,LoginApi
from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.index_view, name='index'),
     path('success/', views.success_view, name='success'),
]
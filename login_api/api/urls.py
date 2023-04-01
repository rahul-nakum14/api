from django.urls import path
from . views import RegisterApi,LoginApi

urlpatterns = [
    path('register/',RegisterApi.as_view()),
    path('login/',LoginApi.as_view()),
    path('register/<int:pk>', RegisterApi.as_view()),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('search', search, name='search'),
    path('detail/<str:id>',detail,name="detail"),
]

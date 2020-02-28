import sys

from django.contrib import admin
from django.urls import path
sys.path.append("..")
from npuzzle_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index")
]

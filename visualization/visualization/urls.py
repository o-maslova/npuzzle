import sys

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
sys.path.append("..")
from npuzzle_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('solving/', views.solving, name="solving"),
    path('', TemplateView.as_view(template_name="index.html"))
]

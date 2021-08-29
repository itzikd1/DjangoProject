from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectsSerializer.as_view()),
]

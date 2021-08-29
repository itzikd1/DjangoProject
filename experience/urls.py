from django.urls import path
from django.views.generic import TemplateView

app_name = 'experience'

urlpatterns = [
    path('', TemplateView.as_view(template_name="experience/index.html")),
]

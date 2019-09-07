from django.urls import path
from . import views

urlpatterns = [
    path("", views.section_index, name="section_index"),
    path("<int:pk>/", views.section_detail, name="section_detail"),
]

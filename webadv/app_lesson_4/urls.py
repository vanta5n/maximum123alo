from django.urls import path
from .views import indexik

urlpatterns = [
    path('lesson_4', indexik)
]
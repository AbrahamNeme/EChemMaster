from django.urls import path
from .views import get_all_cventry, get_cventry_by_name

urlpatterns = [
    path('all/', get_all_cventry),
    path('entrybyname/', get_cventry_by_name),
]

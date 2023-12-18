from django.urls import path
from .views import get_all_cventry, get_cventry_by_name, get_cventry_by_material, get_normalized_cventry

urlpatterns = [
    path('all/', get_all_cventry),
    path('entrybyname/<str:name>/', get_cventry_by_name),
    path('entrybymaterial/<str:material>/', get_cventry_by_material),
    path('get_normalized_cventry/<str:name>/', get_normalized_cventry, name='get_normalized_cventry'),
]

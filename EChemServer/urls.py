from django.urls import path
from .views import get_all_cventry, get_cventry_by_name, get_cventry_by_material, get_normalized_cventry

urlpatterns = [
    path('all/', views.get_all_cventry, name='get_all_cventry'),
    path('entrybymaterial/<str:material>/', views.get_cventry_by_material, name='get_cventry_by_material'),
    path('entrybyname/<str:name>/', views.get_cventry_by_name, name='get_cventry_by_name'),
    path('entriesbyname/<str:names>/', views.get_cventries_by_name, name='get_cventries_by_name'),
]

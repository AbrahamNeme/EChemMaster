from django.urls import path
from . import views
    

urlpatterns = [
    path('all/', views.get_all_cventry, name='get_all_cventry'),
    path('entrybyname/<str:name>/', views.get_cventry_by_name, name='get_cventry_by_name'),
    path('entrybymaterial/<str:material>/', views.get_cventry_by_material, name='get_cventry_by_material'),
]

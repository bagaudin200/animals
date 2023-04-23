from django.urls import path
from .views import AnimalListView, AnimalEditView, AnimalDeleteView

urlpatterns = [
    path('animals/', AnimalListView.as_view(), name='animal_list'),
    path('animals/<int:pk>/edit/', AnimalEditView.as_view(), name='animal_edit'),
    path('animals/<int:pk>/delete/', AnimalDeleteView.as_view(), name='animal_delete'),
]
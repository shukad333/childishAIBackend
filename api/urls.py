from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemListCreateView.as_view(), name='item-list'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
]
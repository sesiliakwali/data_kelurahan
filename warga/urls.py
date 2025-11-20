from django.urls import path
from .views import (
    WargaListView, WargaDetailView, 
    WargaCreateView, WargaUpdateView, WargaDeleteView
)
urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),

    # Edit dan Hapus harus duluan
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),

    # Detail selalu paling bawah
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
]

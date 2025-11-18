from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga
from django.urls import reverse_lazy

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

class WargaCreateView(CreateView):
    model = Warga
    fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaUpdateView(UpdateView):
    model = Warga
    fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')
class WargaUpdateView(UpdateView):
    model = Warga
    fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

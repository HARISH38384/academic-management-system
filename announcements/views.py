from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Announcement

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/announcement_list.html'
    context_object_name = 'announcements'

class AnnouncementCreateView(CreateView):
    model = Announcement
    template_name = 'announcements/announcement_form.html'
    fields = '__all__'
    success_url = reverse_lazy('announcement_list')

class AnnouncementUpdateView(UpdateView):
    model = Announcement
    template_name = 'announcements/announcement_form.html'
    fields = '__all__'
    success_url = reverse_lazy('announcement_list')

class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = 'announcements/announcement_confirm_delete.html'
    success_url = reverse_lazy('announcement_list')

from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubjectListView.as_view(), name='subject_list'),
    path('new/', views.SubjectCreateView.as_view(), name='subject_create'),
    path('<int:pk>/edit/', views.SubjectUpdateView.as_view(), name='subject_update'),
    path('<int:pk>/delete/', views.SubjectDeleteView.as_view(), name='subject_delete'),
]

import os

apps = {
    'teachers': {'model': 'Teacher', 'fields': "name = models.CharField(max_length=100)\n    email = models.EmailField(unique=True)\n    phone = models.CharField(max_length=15)\n    qualification = models.CharField(max_length=100)\n    experience = models.IntegerField(default=0)"},
    'departments': {'model': 'Department', 'fields': "name = models.CharField(max_length=100, unique=True)\n    hod = models.CharField(max_length=100)\n    established_date = models.DateField()"},
    'courses': {'model': 'Course', 'fields': "name = models.CharField(max_length=100, unique=True)\n    duration_years = models.IntegerField()\n    credits = models.IntegerField()"},
    'subjects': {'model': 'Subject', 'fields': "name = models.CharField(max_length=100)\n    code = models.CharField(max_length=20, unique=True)\n    credits = models.IntegerField()"},
    'announcements': {'model': 'Announcement', 'fields': "title = models.CharField(max_length=200)\n    content = models.TextField()\n    date = models.DateField(auto_now_add=True)"},
}

for app_name, app_data in apps.items():
    model_name = app_data['model']
    model_lower = model_name.lower()
    fields = app_data['fields']
    
    # 1. Models
    with open(f"{app_name}/models.py", "w") as f:
        f.write(f"from django.db import models\n\nclass {model_name}(models.Model):\n    {fields}\n\n    def __str__(self):\n        return self.name if hasattr(self, 'name') else self.title\n")

    # 2. Views
    with open(f"{app_name}/views.py", "w") as f:
        f.write(f"""from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import {model_name}

class {model_name}ListView(ListView):
    model = {model_name}
    template_name = '{app_name}/{model_lower}_list.html'
    context_object_name = '{app_name}'

class {model_name}CreateView(CreateView):
    model = {model_name}
    template_name = '{app_name}/{model_lower}_form.html'
    fields = '__all__'
    success_url = reverse_lazy('{model_lower}_list')

class {model_name}UpdateView(UpdateView):
    model = {model_name}
    template_name = '{app_name}/{model_lower}_form.html'
    fields = '__all__'
    success_url = reverse_lazy('{model_lower}_list')

class {model_name}DeleteView(DeleteView):
    model = {model_name}
    template_name = '{app_name}/{model_lower}_confirm_delete.html'
    success_url = reverse_lazy('{model_lower}_list')
""")

    # 3. URLs
    with open(f"{app_name}/urls.py", "w") as f:
        f.write(f"""from django.urls import path
from . import views

urlpatterns = [
    path('', views.{model_name}ListView.as_view(), name='{model_lower}_list'),
    path('new/', views.{model_name}CreateView.as_view(), name='{model_lower}_create'),
    path('<int:pk>/edit/', views.{model_name}UpdateView.as_view(), name='{model_lower}_update'),
    path('<int:pk>/delete/', views.{model_name}DeleteView.as_view(), name='{model_lower}_delete'),
]
""")

    # 4. Templates
    os.makedirs(f"templates/{app_name}", exist_ok=True)
    
    # List Template
    with open(f"templates/{app_name}/{model_lower}_list.html", "w") as f:
        f.write(f"""{{% extends 'base.html' %}}
{{% block content %}}
<div class="container-fluid" data-aos="fade-in">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h2 class="fw-bold mb-0">{model_name} Management</h2>
        <a href="{{% url '{model_lower}_create' %}}" class="btn btn-primary rounded-pill px-4 shadow-sm">
            <i class="bi bi-plus me-2"></i> Add {model_name}
        </a>
    </div>
    <div class="glass-card p-4">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="text-muted">
                    <tr><th>Item</th><th>Actions</th></tr>
                </thead>
                <tbody>
                    {{% for item in {app_name} %}}
                    <tr>
                        <td class="fw-bold">{{{{ item }}}}</td>
                        <td>
                            <a href="{{% url '{model_lower}_update' item.pk %}}" class="btn btn-sm btn-outline-primary rounded-circle me-1"><i class="bi bi-pencil"></i></a>
                            <a href="{{% url '{model_lower}_delete' item.pk %}}" class="btn btn-sm btn-outline-danger rounded-circle"><i class="bi bi-trash"></i></a>
                        </td>
                    </tr>
                    {{% empty %}}
                    <tr><td colspan="2" class="text-center py-5 text-muted">No Data Found</td></tr>
                    {{% endfor %}}
                </tbody>
            </table>
        </div>
    </div>
</div>
{{% endblock %}}""")

    # Form Template
    with open(f"templates/{app_name}/{model_lower}_form.html", "w") as f:
        f.write(f"""{{% extends 'base.html' %}}
{{% block content %}}
<div class="container-fluid" data-aos="fade-up">
    <div class="row justify-content-center">
        <div class="col-lg-6">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h2 class="fw-bold mb-0">{{% if form.instance.pk %}}Edit {model_name}{{% else %}}Add {model_name}{{% endif %}}</h2>
                <a href="{{% url '{model_lower}_list' %}}" class="btn btn-outline-secondary rounded-pill px-4"><i class="bi bi-arrow-left me-2"></i> Back</a>
            </div>
            <div class="glass-card p-5">
                <form method="post" class="needs-validation">
                    {{% csrf_token %}}
                    <div class="row g-3 mb-4">
                        {{{{ form.as_p }}}}
                    </div>
                    <div class="d-grid mt-4">
                        <button type="submit" class="btn btn-primary rounded-pill py-3 fw-bold shadow"><i class="bi bi-check-circle me-2"></i> Save Changes</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}""")

    # Delete Template
    with open(f"templates/{app_name}/{model_lower}_confirm_delete.html", "w") as f:
        f.write(f"""{{% extends 'base.html' %}}
{{% block content %}}
<div class="container-fluid" data-aos="zoom-in">
    <div class="row justify-content-center">
        <div class="col-md-6 mt-5">
            <div class="glass-card p-5 text-center border-danger" style="border-top: 5px solid var(--danger);">
                <i class="bi bi-exclamation-triangle-fill text-danger mb-3" style="font-size: 4rem;"></i>
                <h3 class="fw-bold mb-3">Delete {model_name}?</h3>
                <p class="text-muted mb-4">Are you sure you want to delete this {model_name}? This cannot be undone.</p>
                <form method="post">
                    {{% csrf_token %}}
                    <div class="d-flex justify-content-center gap-3">
                        <a href="{{% url '{model_lower}_list' %}}" class="btn btn-light rounded-pill px-5">Cancel</a>
                        <button type="submit" class="btn btn-danger rounded-pill px-5 shadow">Yes, Delete</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}""")

print("All Modules Generated Successfully!")

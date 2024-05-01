from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView

from medical_services.forms import CategoryForm, ServicesForm
from medical_services.models import Category, Service

from django.urls import reverse_lazy


# Классы категории
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    permission_required = 'medical_services.add_category'
    success_url = reverse_lazy("category_list")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None


class CategoryListView(ListView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    permission_required = 'medical_services.add_category'
    success_url = reverse_lazy("category_list")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy("category_list")
    template_name = "medical_services/category_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.get_object().category_title
        return context

class CategoryServiceListView(ListView):
    model = Service

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Service.objects.filter(category_id=category_pk)


# Классы услуг
class ServiceCreateView(CreateView):
    model = Service
    form_class = ServicesForm
    permission_required = 'medical_services.add_product'
    success_url = reverse_lazy("service_list")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None


class ServiceListView(ListView):
    model = Service


class ServiceDetailView(DetailView):
    model = Service

    def get(self, request, pk):
        product = Service.objects.get(pk=pk)
        context = {
            'object_list': Service.objects.filter(id=pk),
        }
        return render(request, 'medical_services/service_detail.html', context)


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServicesForm

    success_url = reverse_lazy("service_list")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy("service_list")
    template_name = "medical_services/service_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.get_object().services_title
        return context


# Другие классы
def home(request):
    return render(request, 'medical_services/home.html')

def index(request):
    return render(request, 'medical_services/index.html')
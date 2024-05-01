from django.urls import path
from medical_services.views import home, index, CategoryListView, CategoryCreateView, ServiceListView, \
    CategoryServiceListView, \
    ServiceCreateView, ServiceDetailView, ServiceUpdateView, ServiceDeleteView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('', home, name='home'),

    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    path('service_create/', ServiceCreateView.as_view(), name='service_create'),
    path('service_list/', ServiceListView.as_view(), name='service_list'),
    path('service_list/<int:pk>/', CategoryServiceListView.as_view(), name='service_list'),
    path('service_detail/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('service_update/<int:pk>/', ServiceUpdateView.as_view(), name='service_update'),
    path('service_delete/<int:pk>/', ServiceDeleteView.as_view(), name='service_delete'),

    ]

from django.contrib import admin

from medical_services.models import Category, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title', 'category_description', 'category_image')
    search_fields = ('category_title', 'category_description')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('services_title', 'services_description', 'price', 'category', 'deadline')
    search_fields = ('services_title', 'services_description')

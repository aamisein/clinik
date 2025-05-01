# 
from django.contrib import admin
from .models import Visit, Service
from jalali_date.admin import ModelAdminJalaliMixin

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Visit)
class VisitAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'current_visit_date', 'next_visit_date', 'service']
    list_filter = ['service', 'current_visit_date', 'next_visit_date']
    search_fields = ['first_name', 'last_name', 'phone']
from django.contrib import admin
from .models import SecurityRecord


# Register your models here.
@admin.register(SecurityRecord)
class SecurityRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name", "description"]
    list_per_page = 10
    ordering = ["-id"]

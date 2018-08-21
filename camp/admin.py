from django.contrib import admin
from .models import Camp

# Register your models here.

@admin.register(Camp)
class CampAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'venue']


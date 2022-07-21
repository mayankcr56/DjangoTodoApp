from django.contrib import admin
from .models import Task

class Tasks(admin.ModelAdmin):
    list_display = ('name', 'description')


# Register your models here.

admin.site.register(Task)
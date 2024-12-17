from django.contrib import admin
from .models import Task, History

@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ['id','title','description']
    list_display_links = ['title']

@admin.register(History)
class AdminHistory(admin.ModelAdmin):
    list_display = ['id','htitle','hdescription']
    list_display_links = ['htitle']

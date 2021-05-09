from django.contrib import admin
from .models import Project, Alltask


class AlltaskAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'project', 'user']


# Register your models here.
admin.site.register(Project)
admin.site.register(Alltask, AlltaskAdmin)

from django.contrib import admin
from .models import Project, Environment

# Register your models here.
admin.register(Project,)





class ProjectAdmin(admin.ModelAdmin):
        list_display = ["name","browser" ,"driver_file", "description" ]

class EnvironmentAdmin(admin.ModelAdmin):
        list_display=["key","value","environment"]
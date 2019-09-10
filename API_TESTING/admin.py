from django.contrib import admin
from .models import Project, Environment,ApiData,Query_params




admin.site.register(Project)
admin.site.register(Environment)
admin.site.register(ApiData)
admin.site.register(Query_params)



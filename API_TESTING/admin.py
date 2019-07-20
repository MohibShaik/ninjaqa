from django.contrib import admin
from .models import Project, Environment,ApiData,Query_params





class ProjectAdmin(admin.ModelAdmin):
        list_display = ["name","desc" ]

class EnvironmentAdmin(admin.ModelAdmin):
        list_display=["environment","project","base_url"]


class ApiDataAdmin(admin.ModelAdmin):
    list_display = ["api_endpoint", "request_method" ]

class Query_paramsAdmin(admin.ModelAdmin):
    list_display = ["environment", "key","value" ]


admin.site.register(Project,ProjectAdmin)
admin.site.register(Environment,EnvironmentAdmin)
admin.site.register(ApiData,ApiDataAdmin)
admin.site.register( Query_params, Query_paramsAdmin)



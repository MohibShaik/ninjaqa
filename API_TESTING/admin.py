from django.contrib import admin
from .models import project, environment,apiData,query_params





class ProjectAdmin(admin.ModelAdmin):
        list_display = ["name","desc" ]

class EnvironmentAdmin(admin.ModelAdmin):
        list_display=["environment","project","base_url"]


class ApiDataAdmin(admin.ModelAdmin):
    list_display = ["api_endpoint", "request_method" ]

class Query_paramsAdmin(admin.ModelAdmin):
    list_display = ["environment", "key","value" ]


admin.site.register(project,ProjectAdmin)
admin.site.register(environment,EnvironmentAdmin)
admin.site.register(apiData,ApiDataAdmin)
admin.site.register( query_params, Query_paramsAdmin)



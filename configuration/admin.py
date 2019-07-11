from django.contrib import admin
from django.contrib.auth.models import User, Group
from configuration.models import Data,Element, Page,Project, Driver,Environment

admin.site.unregister(User)
admin.site.unregister(Group)


class DriverAdmin(admin.ModelAdmin):
        list_display = ["name","browser" ,"driver_file", "description" ]

class DataAdmin(admin.ModelAdmin):
        list_display=["key","value","environment"]
        #fieldsets = [various field sets and fields etc ]
class ElementAdmin(admin.ModelAdmin):
        list_display=["name","page","by","value"]


class PageAdmin(admin.ModelAdmin):
        list_display = ["project","name" ,"relative_path","details" ]

class ProjectAdmin(admin.ModelAdmin):
        list_display = ["name" ,"desc" ]


class EnvironmentAdmin(admin.ModelAdmin):
        list_display = ["project" ,"environment","base_url" ]
admin.site.register(Data,DataAdmin)
admin.site.register(Element,ElementAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Driver,DriverAdmin)
admin.site.register(Environment,EnvironmentAdmin)


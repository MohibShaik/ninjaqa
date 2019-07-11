from django.contrib import admin

from reports.models import Report


class ReportAdmin(admin.ModelAdmin):
        list_display = ["environment","report_name","report_file","details", "run_by"]

admin.site.register(Report,ReportAdmin)



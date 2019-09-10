"""reporting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path,include

import API_TESTING
from API_TESTING import urls
# from rest_framework import routers
# from API_TESTING.views import ProjectViewSet,EnvironmentViewSet,ApiDataViewSet,Query_paramsViewSet

from reports.views import  run_test_case, runs,runsuite

# from API_TESTING.views import test
admin.site.site_header = "QA-Ninja"
admin.site.site_title = "QA-Ninja"
admin.site.index_title = ""

# Using Router in DRF
# router = routers.DefaultRouter()
#
#
# router.register('project', ProjectViewSet)
# router.register('environment', EnvironmentViewSet)
# router.register('apiData', ApiDataViewSet)
# router.register('query_params', Query_paramsViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include(API_TESTING.urls)),
    
    # Original Template taken from https://github.com/gkushang/cucumber-html-reporter
    path('template/', TemplateView.as_view(template_name='cucumber_report_bootstrap.html')),
    path('runs/', runs,name= 'Home'),
    path('runs/<run_id>', runs,name= 'Home'),
    path('run/', run_test_case,name= 'run_test_case'),
    path('runsuite/', runsuite,name= 'runsuite'),
    # path('api/v1/', include(router.urls)),
    # path('', include(router.urls))
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

    


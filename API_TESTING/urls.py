# from django.conf.urls import url
# from rest_framework import routers

from API_TESTING import views
# from .serializers import ProjectViewSet, EnvironmentViewSet, ApiDataViewSet, Query_paramsViewSet
from django.urls import path

urlpatterns = [

    path('api_test/', views.get_data)



]

from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
import json
from reports.models import Report
from API_TESTING.models import Project,Environment,ApiData,Query_params
from .serializers import ProjectSerializer, EnvironmentViewSet, ApiDataViewSet, Query_paramsViewSet
import os
import subprocess
from django.http import JsonResponse
from datetime import datetime
import requests


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class ApiDataViewSet(viewsets.ModelViewSet):
    queryset = ApiData.objects.all()
    serializer_class = ApiDataSerializer


class Query_paramsViewSet(viewsets.ModelViewSet):
    queryset = Query_params.objects.all()
    serializer_class = Query_paramsSerializer

























# def test(request,run_id=None):
#     base_url=end_point=None
#     base_url = Environment.objects.get(pk=run_id)
#     b_url=str(base_url)
#     print(type(b_url))


#     request_type = ApiData.objects.get(pk=run_id)
#     r_type=str(request_type).split()
#     method=r_type[1]
#     end_point = r_type[0]
#     print(type(end_point))

#     P= Query_params.objects.get(pk=run_id)
#     PARAMS=str(P)
    


    
#     URL = b_url+end_point
#     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#     print(URL)
#     if request.method == 'GET':
#         response = requests.get(url=URL, params=PARAMS)
#         json_data=response.json()
        
#     elif request.method=="POST":
#         response = request.POST(url=base_url)
#         json_data = response.json()

#     elif request.method=="DELETE":
#        response = request.DELETE(url=base_url)
#        json_data = response.json()

#     elif request.method =='PUT':
#         response = request.PUT(url=base_url)
#         json_data = response.json()
#     return TemplateResponse(request, 'test.html', {'json_data': json_data})

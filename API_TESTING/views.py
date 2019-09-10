from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
import json
from .models import Project, Environment, ApiData, Query_params
from .serializers import ProjectSerializer, EnvironmentSerializer, ApiDataSerializer, Query_paramsSerializer
import os
import subprocess
from django.http import JsonResponse
# from datetime import datetime
# from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework import status
from .form import APIForm


def get_data(request):
    if request.method == 'POST':
        form = APIForm(request.POST)
        if form.is_valid():
            pass

    form = APIForm()

    return render(request, 'api_testing.html', {'form': form})

# Using of DRF
#
# class ProjectViewSet(viewsets.ModelViewSet):
#
#     serializer_class = ProjectSerializer
#     queryset = Project.objects.all()
#
# class EnvironmentViewSet(viewsets.ModelViewSet):
#     queryset = Environment.objects.all()
#     serializer_class = EnvironmentSerializer
#
#
# class ApiDataViewSet(viewsets.ModelViewSet):
#     queryset = ApiData.objects.all()
#     serializer_class = ApiDataSerializer
#
# class Query_paramsViewSet(viewsets.ModelViewSet):
#     queryset = Query_params.objects.all()
#     serializer_class = Query_paramsSerializer
# #


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

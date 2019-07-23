from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
import json
from reports.models import Report
from API_TESTING.models import Project,Environment,ApiData,Query_params
import os
import subprocess
from django.http import JsonResponse
from datetime import datetime
import requests


def test(request,run_id=None):
    base_url=end_point=None
    base_url = Environment.objects.get(pk=run_id)
    print("............................")
    print(base_url)

    request_type = ApiData.objects.get(pk=run_id)
    print("::::::::::::::::")
    print(request_type)

           
    if request.method=='GET':
        response = requests.get('base_url')
        json_data=response.json()
        
    return TemplateResponse(request, 'test.html',{'json_data':json_data})

    # elif request.method=="POST":
    #     response = request.POST(url)
    #     json_data = response.json()

    #     return json_data

    # elif request.method=="DELETE":
    #    response = request.DELETE(url)
    #    json_data = response.json()

    #    return json_data

    # elif request.method =='PUT':
    #     response = request.PUT(url)
    #     json_data = response.json()

    #     return json_d

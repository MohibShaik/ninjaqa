from django.shortcuts import render
from django.template.response import TemplateResponse
import json
# Create your views here.
from reports.models import Report
from API_TESTING.models import Project,Environment,ApiData,Query_params
import os
import subprocess
from django.http import JsonResponse
from datetime import datetime

# def test():
#     projects=Project.objects.all().values_list('name')
#     print(projects[0][0])
#     return True



def home(request):
    projects=Project.objects.all().values_list('name')
    b_url=Environment.objects.all().values_list('base_url')
    base_url=b_url[0][0]
    print(base_url)
    type(base_url)


    endpoint=ApiData.objects.all().values_list('api_endpoint')
    api_point=endpoint[0][0]
    type(api_point)
    print(api_point)
    url=base_url+api_point
    print(url)

    if request.method=='GET':
        response=request.GET(url)
        json_data=response.json()
        
        return json_data

    elif request.method=="POST":
        response=requests.request(verb,url=url)
        return response

    # elifrequest.method=="DELETE":
    #     url+=api_endpoint
    #     response=requests.request(verb,url=url)
    #     return response

    # elif request.method =='PUT':
    #     url+=api_endpoint
    #     response=requests.request(verb,url=url)
    #     return response











    # 
    # geodata = response.json()
    # ret
    # return render(request, 'core/home.html', {
    #     'ip': geodata['ip'],
    #     'country': geodata['country_name']
    # })
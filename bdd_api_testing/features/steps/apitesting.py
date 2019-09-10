import os, sys  
import importlib
root_dir = os.path.abspath(".")[:-len('bdd_api_testing')]
sys.path.append(root_dir)
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE","reporting.settings")
application = get_wsgi_application()
from environment import environment
from API_TESTING import models
from behave import *
import requests

global_project = models.project.objects.get(name=environment['project'])
print(global_project)
global_environment = models.environment.objects.get(project=global_project, environment=environment['environment'])
print(global_environment)




global_general_variables = {}
http_request_header = {}
http_request_body = {}
http_request_url_query_param = {}


@given(u'Read the {base_url}')
def step_impl(context,base_url):
    base_url = global_environment.base_url
    global_general_variables['basic_application_URL'] = base_url
    print(global_general_variables['basic_application_URL'])




@given(u'Set GET_api_endpoint as {get_api_endpoint}')
def step_impl(context, get_api_endpoint):
    get_api_endpoint=models.apiData.objects.get(api_endpoint=get_api_endpoint)

    global_general_variables['GET_api_endpoint'] = get_api_endpoint.api_endpoint
   


@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    http_request_header['content-type'] = header_content_type



@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    http_request_header['Accept'] = header_accept_type



@when(u'Set Query param as "{query_param}"')
def step_impl(context, query_param):
    if 'empty' in query_param:
        http_request_url_query_param.clear()
    else:
        http_request_url_query_param.clear()





@when(u'Raise "{http_request_type}" HTTP request')
def step_impl(context, http_request_type):
    url_temp = global_general_variables['basic_application_URL']
    if 'GET' == http_request_type:
        url_temp += global_general_variables['GET_api_endpoint']
        http_request_body.clear()
        global_general_variables['response_full'] = requests.get(url_temp,headers=http_request_header,data=http_request_body)
       

        print(global_general_variables['response_full'] )                                                



@then(u'Valid HTTP response should be received')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, 'Null response received'



@then(u'Response http code should be {expected_response_code:d}')
def step_impl(context, expected_response_code):
    global_general_variables['expected_response_code'] = expected_response_code
    actual_response_code = global_general_variables['response_full'].status_code
    print(str(global_general_variables['response_full'].json()))

    if str(actual_response_code) not in str(expected_response_code):
        print (str(global_general_variables['response_full'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)
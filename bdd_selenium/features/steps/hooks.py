import os, sys  
import importlib
root_dir = os.path.abspath(".")[:-len('bdd_selenium')]
sys.path.append(root_dir)
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE","reporting.settings")
application = get_wsgi_application()
from environment import environment
from configuration import models
from behave import *
import utility
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
delay=20



#project = models.Project.objects.get(name=environment['project'])
global_project = models.Project.objects.get(name=environment['project'])
global_environment = models.Environment.objects.get(project=global_project, environment=environment['environment'])
global_driver_obj = models.Driver.objects.get(name=environment['driver'])
if global_driver_obj.browser=='chrome':
     global_driver = webdriver.Chrome("../"+global_driver_obj.driver_file.name)
# TODO : Add more browsers     
global_var={
     'elements':{},
     'data':{}
}

############## UTILITY ##################


def get_element(elem, parent_element=None):
    if not parent_element:
        parent = global_driver
    else:
        parent = parent_element

    if elem.by == 'id':
        return WebDriverWait(parent, delay).until(EC.presence_of_element_located((By.ID, elem.value)))

    elif elem.by == 'xpath':
        return WebDriverWait(parent, delay).until(EC.element_to_be_clickable((By.XPATH, elem.value)))

    elif elem.by == 'css_selector':
        return WebDriverWait(parent, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, elem.value)))
    elif elem.by == 'class':
        return WebDriverWait(parent, delay).until(EC.presence_of_element_located((By.CLASS_NAME, elem.value)))
    elif elem.by=='name':
        return WebDriverWait(parent, delay).until(EC.presence_of_element_located((By.NAME, elem.value)))


def get_elements(config_key, key, parent_element=None):
    if not parent_element:
        parent = driver
    else:
        parent = parent_element

    conf = configuration["pages"][config_key]["elements"]

    elem = conf[key]
    if elem['by'] == 'xpath':
        return parent.find_elements_by_xpath(elem['val'])
    if elem['by'] == 'css_selector':
        return parent.find_elements_by_xpath(elem['val']) 
    if elem['by'] == 'class':
        return parent.find_elements_by_class_name(elem['val'])


def escape():
    from base import driver
    return webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    
#########################################

@given(u'open {page} page')
def step_impl(context ,page):
     page = models.Page.objects.get(name=page, project=global_project)
     url = global_environment.base_url + page.relative_path
     global_driver.get(url)
#       load login  page elements and data 
@given(u'load {page_name} page elements and data')  
def step_impl(context ,page_name):
     page = models.Page.objects.get(name=page_name, project=global_project)
     rec_list = models.Data.objects.filter(page=page, environment=global_environment)
     for rec in rec_list:
          global_var['data'][rec.key] = rec.value
     elem_list = models.Element.objects.filter(page=page)
     for elem in elem_list:
          global_var['elements'][elem.name] = elem


@then(u'fill {element_name} with {element_value} value')
def step_impl(context, element_name, element_value):
     element=get_element(global_var['elements'][element_name])
     element.send_keys(global_var['data'][element_value])
     time.sleep(2)



@then(u'click {element_name}')
def step_impl(context, element_name):
     element=get_element(global_var['elements'][element_name])
     element.click()
    

@then(u'select {element_value}')
def step_impl(context,element_value):
     element=get_element(global_var['elements'][element_value])
     element.click()
     element.send_keys(Keys.ESCAPE)
     time.sleep(1)

     
     
     
     

      


# @then(u'check text of {element_name} equal to {element_value}')
# def step_impl(context, element_name, element_value):
#      element=get_element(global_var['elements'][element_name])
#      assert element.text == global_var['data'][element_value]





import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


delay = 30 # seconds

def read_config(*elems, config_key="meta"):
    #conf = getattr(configuration[],config_var)
    resp=configuration[config_key][elems[0]]
    for elem in elems[1:]:
        resp=resp[elem]
    return resp


def open_url(url):
    from base import driver
    print(driver)
    print(url)
    print("OPENING")
    return driver.get(url)

def send_keys(element,text):
    getattr(element,'send_keys')(text)

def click(element, wait_after_click=None):
    getattr(element,'click')()
    if wait_after_click:
        time.sleep(wait_after_click)

def select(element,wait_after_click=None):
    getattr(element,'select')()


    
    

def get_element(elem,parent_element=None):
    if not parent_element :
        from base import driver
        parent=driver
    else:
        parent=parent_element

    if elem['by']=='id':
        return WebDriverWait(parent, delay).until(EC.presence_of_element_located((By.ID, elem['val'])))

    if elem['by']=='xpath':
        return WebDriverWait(parent, delay).until(EC.presence_of_element_located((By.XPATH, elem['val'])))

    if elem['by']=='css_selector':
        return WebDriverWait(parent, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, elem['val'])))
    if elem['by']=='class':
        return WebDriverWait(parent, delay).until(EC.presence_of_element_located((By.CLASS_NAME, elem['val'])))

def get_elements(config_key,key,parent_element=None):
    if not parent_element :
        from base import driver
        parent=driver
    else:
        parent=parent_element

    conf = configuration["pages"][config_key]["elements"]

    elem = conf[key]
    if elem['by']=='xpath':
        return parent.find_elements_by_xpath(elem['val'])
    if elem['by']=='css_selector':
        return parent.find_elements_by_xpath(elem['val'])
    if elem['by']=='class':
        return parent.find_elements_by_class_name(elem['val'])

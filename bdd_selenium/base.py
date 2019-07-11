from selenium import webdriver
from utility import read_config
driver = webdriver.Chrome(read_config('driver'))
from django.shortcuts import render
from django.template.response import TemplateResponse
import json
# Create your views here.
from reports.models import Report
from configuration.models import Project,Environment
import os
import subprocess
from django.http import JsonResponse
from datetime import datetime
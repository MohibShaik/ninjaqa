from rest_framework import serializers
from .models import *


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project


class ApiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiData


class Query_paramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Query_params

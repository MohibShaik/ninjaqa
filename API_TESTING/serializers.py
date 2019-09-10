from rest_framework import serializers
from .models import Project,Environment,ApiData,Query_params


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields=('id', 'url', 'environment','project', 'base_url')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields=('__all__')


class ApiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiData
        fields = ('__all__')


class Query_paramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Query_params
        fields = ('__all__')

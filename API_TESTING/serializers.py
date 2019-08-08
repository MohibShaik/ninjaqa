from rest_framework import serializers
from .models import project,environment,apiData,query_params


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = environment
        fields=('__all__')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields=('__all__')


class ApiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = apiData
        fields = ('__all__')


class Query_paramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = query_params
        fields = ('__all__')

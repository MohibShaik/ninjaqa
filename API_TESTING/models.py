from django.db import models

# Create your models here.
REQUEST_TYPE=[
    ['GET','GET'],
    ['POST','POST'],
    ['PUT','PUT'],
    ['DELETE','DELETE'],
]

ENVIRONMENT_TYPE_CHOICES = [
    ['local','Local'],
    ['dev','Development'],
    ['qa','QA'],
    ['stage','Staging'],
    ['prod','Production'],
]

class Project(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=256)

    def __str__(self):
        return self.name



class Environment(models.Model):
    environment =models.CharField(max_length=10, choices=ENVIRONMENT_TYPE_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    base_url = models.URLField(max_length=256)
    def __str__(self):
        return self.base_url


class ApiData(models.Model):
    api_endpoint=models.CharField(max_length=100)
    request_method=models.CharField(max_length=10, choices=REQUEST_TYPE)
    def __str__(self):

        return'{} {}'.format(self.api_endpoint, self.request_method)

class Query_params(models.Model):
    environment=models.ForeignKey(Environment,on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=1024)

    def __str__(self):

        return self.key + "=" + str(self.value)

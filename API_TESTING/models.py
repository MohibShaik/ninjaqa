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
        return self.environment # "%s (%s)" % (self.environment, self.project.name) 
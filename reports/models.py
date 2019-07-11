from django.db import models
from configuration.models import Environment
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    details=models.CharField(max_length=256)
    report_name = models.CharField(max_length=200)
    report_file = models.CharField(max_length=200)
    run_by = models.ForeignKey(User,on_delete=models.CASCADE)
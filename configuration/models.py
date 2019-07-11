from django.db import models

ELEMENT_CHOICES = [
    ['id','By ID'],
    ['class','By Class'],
    ['xpath','By Xpath'],
    ['name','By Name'],
    ['css_selector','Css Selector'],

]

BROWSER_CHOICES = [
    ['chrome','Chrome'],
    ['ie','Internet Explorer'],
    ['firefox','Firefox']
]
ENVIRONMENT_TYPE_CHOICES = [
    ['local','Local'],
    ['dev','Development'],
    ['qa','QA'],
    ['stage','Staging'],
    ['prod','Production'],
]
class Driver(models.Model):
    name = models.CharField(max_length=200)
    driver_file = models.FileField(upload_to='files/driver')
    description = models.CharField(max_length=256)
    browser = models.CharField(max_length=50,choices = BROWSER_CHOICES)
    
    def __str__(self):
        return self.name


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
        
class Page(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    relative_path=models.CharField(max_length=100)

    details = models.CharField(max_length=256)

    def __str__(self):
        return "%s (%s)"%(self.name,self.project.name )

class Element(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    by = models.CharField(max_length=100,choices=ELEMENT_CHOICES)
    value = models.CharField(max_length=1024)
    def __str__(self):
        return self.name  

class Data(models.Model):
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=1024)
    def __str__(self):
        return self.key + "(" + str(self.environment) + " )"


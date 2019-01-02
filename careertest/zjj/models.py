from django.db import models
from qsj.models import Company,Moding

# Create your models here.
class Job(models.Model):
    jobname=models.CharField(max_length=100)
    company_id=models.ForeignKey(to=Company,on_delete=models.CASCADE,default=1)
    moding_id=models.ForeignKey(to=Moding,on_delete=models.CASCADE)
    isdelete=models.BooleanField(default=False)


class Jobneed(models.Model):
    job_id=models.ForeignKey(to='Job',on_delete=models.CASCADE)
    jobdescription=models.CharField(max_length=1024)
    jobrequirements=models.CharField(max_length=1024)
    moding_id=models.ForeignKey(to=Moding,on_delete=models.CASCADE)
    isdelete=models.BooleanField(default=False)


class Tester(models.Model):
    name=models.CharField(max_length=20)
    jobneed_id=models.ForeignKey(to='Jobneed',on_delete=models.CASCADE)
    sex=models.BooleanField(default=True)
    comment=models.CharField(max_length=1024)
    status=models.CharField(max_length=280)
    isdelete=models.BooleanField(default=False)

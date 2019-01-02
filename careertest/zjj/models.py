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
    jobneed_name = models.CharField(max_length=100)     # 职位需求名称，默认和关联的职位名称一致
    jobdescription=models.CharField(max_length=1024)
    jobrequirements=models.CharField(max_length=1024)
    moding_id=models.ForeignKey(to=Moding,on_delete=models.CASCADE)
    isdelete=models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now=True)   # 创建时间
    create_user_id = models.CharField(max_length=100)   # 创建人，可以关联到hr
    jobneed_status = models.IntegerField()  # 职位需求状态表，1：招聘中，0：招聘结束


class Tester(models.Model):
    name=models.CharField(max_length=20)
    jobneed_id=models.ForeignKey(to='Jobneed',on_delete=models.CASCADE)
    sex=models.BooleanField(default=True)
    comment=models.CharField(max_length=1024)
    status=models.CharField(max_length=280)
    isdelete=models.BooleanField(default=False)

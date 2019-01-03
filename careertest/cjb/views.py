# coding=utf8
from django.shortcuts import render, redirect
import time
from .models import Testchart, Tester, Report
from zjj.models import Job, Jobneed, Tester
from qsj.models import UserAdmin, UserHR, UserExpert, Company, Factor, Moding, ModelDesign
from fxj.models import Qustion, Answer



from django.db.models import *
from django.core.paginator import Paginator


# Create your views here.
def jobneed3(request):
    return render(request, 'cjb/jobneed3.html')


def jobneed_query(request):
    jns = Jobneed.objects.all()

    context = {'ob_jns': jns}
    return render(request, 'cjb/jobneed.html', context)


def jobneed_add(request):
    if request.is_ajax():
        jn_name = request.POST.get('jn_name')
        jn_desc = request.POST.get('jn_desc')
        jn_requ = request.POST.get('jn_requ')
        jn_model = request.POST.get('jn_model')

        jn_data = Jobneed()
        jn_data.jobneed_name = jn_name
        jn_data.jobdescription = jn_desc
        jn_data.jobrequirements = jn_requ
        # jn_data.isdelete = False
        # jn_data.create_time = ''

        try:
            jn_data.job_id = Job.objects.get(jobname=jn_name)
        except Exception:
            jn_data.job_id = None

        try:
            jn_data.moding_id = Moding.objects.get(name=jn_model)
        except Exception:
            jn_data.moding_id = None

        try:
            create_name = request.sessions.get('HR')
            jn_data.create_user_name = UserHR.objects.get(user=create_name)
        except Exception:
            jn_data.create_user_name = UserHR.objects.filter(pk=1)
            print(jn_data.create_user_name, '------')

        if jn_model:
            jn_data.jobneed_status = 1
        else:
            jn_data.jobneed_status = 2

        jn_data.save()

    jns = Jobneed.objects.all()
    context = {'ob_jns': jns}
    return render(request, 'cjb/jobneed.html', context)
    # let data_jn_add = {'jn_name':jn_name, 'jn_desc':jn_desc, 'jn_requ':jn_requ, 'jn_model':jn_model, }
    # job_id=models.ForeignKey(to='Job',on_delete=models.CASCADE,null=True,blank=True)
    # jobneed_name = models.CharField(max_length=100,default='')     # 职位需求名称，默认和关联的职位名称一致
    # jobdescription=models.CharField(max_length=1024)
    # jobrequirements=models.CharField(max_length=1024)
    # moding_id=models.ForeignKey(to=Moding,on_delete=models.CASCADE,null=True,blank=True)
    # isdelete=models.BooleanField(default=False)
    # create_time = models.DateTimeField(auto_now=True)   # 创建时间
    # create_user_name = models.CharField(max_length=100,default='')   # 创建人，可以关联到hr
    # jobneed_status = models.IntegerField(default=1)  # 职位需求状态表，1：招聘中，0：招聘结束，2：模型定制中



def jobneed_edit(request):
    return render(request, 'cjb/jobneed.html')



def login(request):
    return render(request, 'pjs/login.html')



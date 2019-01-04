# coding=utf8
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
import time
from cjb.models import Testchart, Report
from zjj.models import Job, Jobneed, Tester
from qsj.models import UserAdmin, UserHR, UserExpert, Company, Factor, Moding, ModelDesign
from fxj.models import Qustion, Answer
from django.db import models
from django.db.models import *
from django.core.paginator import Paginator
import json


# Create your views here.
def jobneed3(request):
    return render(request, 'cjb/jobneed3.html')


def jobneed2(request):
    return render(request, 'cjb/base_hr2.html')


def main(request):
    return render(request, 'cjb/base_hr2.html')


def company(request):
    return render(request, 'cjb/company2.html')


def jobneed_query(request):
    if request.is_ajax():
        # jns = Jobneed.objects.values('id', 'create_hr_id__user', 'create_time', 'jobneed_name', 'jobneed_status')
        # # 遍历元素获取每个职位需求的各种状态的数据
        # for jn in jns:
        #     c_invite = Tester.objects.filter(Q(jobneed_id=jn['id']) & Q(status=2)).count()
        #     c_tested = Tester.objects.filter(Q(jobneed_id=jn['id']) & Q(status=3)).count()
        #     c_selected = Tester.objects.filter(Q(jobneed_id=jn['id']) & Q(status=4)).count()
        #     jn.update({'c_invite': c_invite, 'c_tested': c_tested, 'c_offer': c_selected})

        # 下面这个语句也可以直接获取到每个职位需求的各种状态的数据
        jns = Jobneed.objects.filter(isdelete=False).annotate(c_invite=Count('tester', filter=Q(tester__status=2)),
                                       c_tested=Count('tester', filter=Q(tester__status=3)),
                                       c_selected=Count('tester', filter=Q(tester__status=4)),
                                       c_deselect=Count('tester', filter=Q(tester__status=4)))

        print(jns, '-------jns-----')
        context = {'ob_jns': jns}
        return render(request, 'cjb/jobneed2.html', context)
    else:
        return redirect('/cjb/main/')


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
            jn_data.create_hr_id = UserHR.objects.get(user=create_name)
        except Exception:
            jn_data.create_hr_id = UserHR.objects.get(pk=1)
            print(jn_data.create_hr_id, '---create_hr_id---')

        if jn_model:
            jn_data.jobneed_status = 1
        else:
            jn_data.jobneed_status = 2

        jn_data.save()

    jns = Jobneed.objects.all()
    context = {'ob_jns': jns}
    return render(request, 'cjb/jobneed2.html', context)


def jobneed_edit(request):
    return render(request, 'cjb/jobneed.html')


def jobneed_del(request):
    if request.is_ajax():
        jn_id = request.POST.get('id')
    try:
        jn_tobedel = Jobneed.objects.filter(isdelete=False).get(pk=jn_id)
        jn_tobedel.isdelete = True
        jn_tobedel.save()
        # print(Jobneed.objects.get(pk=jn_id).isdelete,'-----isdelete----')
        context = {'del_result': 'delete success!'}
    except Exception:
        context = {'del_result': 'delete fail!'}

    # return HttpResponse(context)
    return JsonResponse(context)


def tester_query(request):
    tes = Tester.objects.filter().values('create_hr_id__user', 'status', 'sex', 'jobneed_id__jobneed_name', 'name')
    context = {'obj_tes': tes}
    print(context, '---testquery---')
    return render(request, 'cjb/tester.html', context)


def tester_add(request):
    return render(request, 'cjb/tester.html')


def tester_edit(request):
    return render(request, 'cjb/tester.html')


def tester_del(request):
    return render(request, 'cjb/tester.html')



def login(request):



    return render(request, 'pjs/login.html')



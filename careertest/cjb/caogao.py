from django.shortcuts import render, redirect
import time
from .models import Testchart, Tester, Report
from zjj.models import Job, Jobneed, Tester
from qsj.models import UserAdmin, UserHR, UserExpert, Company, Factor, Moding, ModelDesign
from fxj.models import Qustion, Answer
from django.db import models
from django.db.models import *
from django.core.paginator import Paginator


d = Jobneed.objects.annotate(
c=Value(Tester.objects.filter(Q(status=1) & Q(jobneed_id=F("jobneed_id_id"))), output_field=models.CharField()))

e = Jobneed.objects.get(pk=5).jn_id.all().values()

e = Jobneed.objects.filter(jn_id__status=1).values()

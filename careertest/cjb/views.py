from django.shortcuts import render
import time


# Create your views here.
def jobneed(request):
    return render(request, 'cjb/jobneed.html')


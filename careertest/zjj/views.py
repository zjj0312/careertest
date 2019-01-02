from django.shortcuts import render

# Create your views here.
def company(request):
    return render(request,'zjj/company.html')
def index(request):
    return render(request,'zjj/index.html')

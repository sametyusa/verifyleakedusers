from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from accountgg.functions import testCredsByAPI, uploadFile
from accountgg.forms import FileForm
from django.template.response import TemplateResponse
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login as applogin, authenticate, logout #add this
from django.contrib import messages
import logging, json
from . import forms

# Create your views here.
def index(request):  
    if request.method == 'POST':  
        uploadForm = FileForm(request.POST, request.FILES)  
        if uploadForm.is_valid():  
            fileUpload = uploadFile(request.FILES['file'])
            testResults = testCredsByAPI(fileUpload)
            logger = logging.getLogger(__name__)
            context = {
                "testResults" : testResults,
            }
        if 'error' in testResults:
            context = {'msg':testResults['error']}
        return render(request,"check.html",context)
    else:  
        uploadForm = FileForm()  
        return render(request,"check.html",{'form':uploadForm})  

def redirectLogin(request):
    return redirect('check.html')

def loginView(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
       form = forms.LoginForm(request.POST)
       if form.is_valid():
           user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
       if user is not None:
           applogin(request,user)
           return redirect('index') 
       else:
           message = '<div class=\'error\'>Username or password is wrong</div>'
    return render(request,'login.html', context={'form':form, 'message':message})

def logOutView(request):
    logout(request)
    return redirect('loginView')
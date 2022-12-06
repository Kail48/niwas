from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from user.forms import CustomUserCreationForm
from user.models import TenantUserProfile,AgentUserProfile,CustomUser

# Create your views here.
def isWorking(request):
    return render(request,'properties/workin.html')
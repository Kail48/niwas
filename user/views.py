from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from .models import TenantUserProfile,AgentUserProfile


def tenantRegister(request):
    form=CustomUserCreationForm()
    context={'form':form}
    print('..........at register...........\n')
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        print('validating')
        if form.is_valid():
            user1=form.save(commit=False)
            user1.username=user1.username.lower()
            user1.save()
            TenantUserProfile.objects.create(user=user1,user_name=user1.username,email=user1.email)
            print("saved")
            return redirect('agent-register')
        else:
            print('something wrong')
            context={'form':form}
            return render(request,'user/tenant-register.html',context)
    return render(request,'user/tenant-register.html',context)

def agentRegister(request):
    form=CustomUserCreationForm()
    context={'form':form}
    print('..........at register...........\n')
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        print('validating')
        if form.is_valid():
            user1=form.save(commit=False)
            user1.username=user1.username.lower()
            user1.save()
            AgentUserProfile.objects.create(user=user1,user_name=user1.username,email=user1.email)
            print("saved")
            return redirect('agent-register')
        else:
            print('something wrong')
            context={'form':form}
            return render(request,'user/tenant-register.html',context)
    return render(request,'user/agent-register.html',context)
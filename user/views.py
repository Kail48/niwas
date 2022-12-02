from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from .models import TenantUserProfile,AgentUserProfile,CustomUser
from django.contrib.auth import login,authenticate,logout

#After creation of a User either Agent profile or tenant profile is automatically linked
#with that user based on what option the user chose earlier in welcome page

def signupRedirect(request):
    messages.error(request,"Something did not work, Maybe you already have an account with this email?")
    return redirect('user-login')

def googleLoginPortal(request):
    return render(request,'user/google-login-portal.html')    
    
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
            return redirect('user-login')
        else:
            messages.error(request,"You did not enter in fields correctly")
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
            return redirect('user-login')
        else:
            print('something wrong')
            context={'form':form}
            return render(request,'user/tenant-register.html',context)
    return render(request,'user/agent-register.html',context)

def welcomePage(request):
    return render(request,'welcomepage.html')

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('logout-user')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=CustomUser.objects.get(username=username)
        except:
            messages.error(request,"Username does not exist")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            try:
                profile=AgentUserProfile.objects.get(user=user)
            except:
                return redirect('user/login-confirm-tenant.html')
            if profile is not None:
                return render(request,'user/login-confirm-agent.html')
            
        else:
            messages.error(request,'username or password incorrect')
            
    return render(request,"user/user-login.html")

    
def logOutUser(request):
    print('out')
    logout(request)
    return redirect('user-login')
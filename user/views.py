from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from properties.models import Property
from .models import TenantUserProfile,AgentUserProfile,CustomUser
from django.contrib.auth import login,authenticate,logout

#After creation of a User either Agent profile or tenant profile is automatically linked
#with that user based on what option the user chose earlier in welcome page
def newUserRegister(request):
    form=CustomUserCreationForm()
    context={'form':form}
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        print('validating')
        if form.is_valid():
            user1=form.save(commit=False)
            email=user1.email
            existing_users=CustomUser.objects.filter(email=email)
    
            
            if len(existing_users)>0:
                form=CustomUserCreationForm()
                context={'form':form}
                messages.error(request,"Email already exists")
                return render(request,'user/new-user-register.html',context)
            else:
                user1.username=user1.username.lower()
                user1.save()
                login(request,user1)
                return redirect('google-login-portal')
        else:
            messages.error(request,"You did not enter in fields correctly")
            context={'form':form}
            return render(request,'user/new-user-register.html',context)
    return render(request,'user/new-user-register.html',context)

def createNewAgent(request):
    user=request.user
    AgentUserProfile.objects.create(user=user,user_name=user.username,email=user.email)
    return render(request,'user/login-confirm-agent.html')

def createNewTenant(request):
    user=request.user
    TenantUserProfile.objects.create(user=user,user_name=user.username,email=user.email)
    return render(request,'user/login-confirm-tenant.html')

def signupRedirect(request):
    messages.error(request,"Something did not work, Maybe you already have an account with this email?")
    return redirect('user-login')

def googleLoginPortal(request):
    user=request.user
    agentProfile=None
    tenantProfile=None
    try:
         agentProfile=AgentUserProfile.objects.get(user=user)
         
    except:
        pass
    try:
        tenantProfile=TenantUserProfile.objects.get(user=user)
    except:
        pass
    if agentProfile is not None:
        return render(request,'user/login-confirm-agent.html')
    elif tenantProfile is not None:
        return render(request,'user/login-confirm-tenant.html')
    else:
        return render(request,'user/google-login-portal.html') 
    


def welcomePage(request):
    return redirect('properties-list')
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
                return render(request,'user/login-confirm-tenant.html')
            if profile is not None:
                return render(request,'user/login-confirm-agent.html')
            
        else:
            messages.error(request,'username or password incorrect')
            
    return render(request,"user/user-login.html")

    
def logOutUser(request):
    messages.success(request,"Successfully logged out")
    logout(request)
    return redirect('user-login')
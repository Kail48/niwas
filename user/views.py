from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm,PhoneForm
from properties.models import Property,Bookings
from .models import TenantUserProfile,AgentUserProfile,CustomUser
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from properties.utils import *

#After creation of a User either Agent profile or tenant profile is automatically linked
#with that user based on what option the user chose earlier in welcome page
def testTemplate(request):
    return render(request,'user/add-details-tenant.html')

@login_required
def viewBookings(request):
    agent=getAgentFromUser(request.user)
    properties=Property.objects.filter(agent=agent)
    bookings={}
    totalViews=0
    for property in properties:
        totalViews+=property.views
        booking=Bookings.objects.filter(property=property).order_by('created')
        bookings[property.title]=booking
    allBookings=[]
    for property in properties:
        booking=Bookings.objects.filter(property=property)
        if len(booking)>0:
            allBookings.extend(booking)
    isEmpty=False
    if len(allBookings)<1:
        isEmpty=True

    context={
        'totalProperties':len(properties),
        'totalBookings':len(allBookings),
        'isEmpty':isEmpty,
        'bookings':bookings,
        'allBookings':allBookings,
        'totalViews':totalViews,
        'bookRatio':int(totalViews/len(allBookings))
        
    }
    print(bookings)
    return render(request,'user/view-bookings.html',context) 

@login_required
def viewProfile(request):
    user=request.user
    print(user)
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
        return redirect('view-agent-profile')
    elif tenantProfile is not None:
        return redirect('view-tenant-profile')
    else:
        return redirect('user-login') 
    

def viewTenantProfile(request):
    user=request.user
    profile=TenantUserProfile.objects.get(user=user)
    bookings=Bookings.objects.filter(tenant=profile)
    isEmpty=False
    isEmpty=len(bookings)<1
    print(user.type)
    context={
        'profile':profile,
        'bookings':bookings,
        'isEmpty':isEmpty,
    }
    return render(request,'user/view-tenant-profile.html',context)

def viewAgentProfile(request):
    user=request.user
    profile=AgentUserProfile.objects.get(user=user)
    isEmpty=False
    properties=Property.objects.filter(agent=profile)
    isEmpty= len(properties)<1
    context={
        'profile':profile,
        'isEmpty':isEmpty,
        'properties':properties
    }
    return render(request,'user/view-agent-profile.html',context)


def completeTenantProfile(request,pk):
    if request.method=='POST':
        user=request.user
        name=request.POST.get('name')
        number=request.POST.get('number')
        form = PhoneForm({"number": number})
        print("number is: "+number)
        if form.is_valid() and len(name)>0:
            tenant=TenantUserProfile.objects.get(id=pk)
            tenant.name=name
            tenant.phone_number=number
            user.type='T'
            user.save()
            tenant.save()
            return redirect('welcome-page')
        else:
            tenant=TenantUserProfile.objects.get(id=pk)
            user=tenant.user
            user.delete()
            return redirect('user-login')

def completeAgentProfile(request,pk):
    user=request.user
    if request.method=='POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        form = PhoneForm({"number": number})
        photo=request.FILES.get('photo')
        print("number is: "+number)
        if form.is_valid() and len(name)>0 and photo is not None:
            agent=AgentUserProfile.objects.get(id=pk)
            agent.name=name
            agent.phone_number=number
            agent.profile_picture=photo
            agent.save()
            user.type='A'
            user.save()
            return redirect('welcome-page')
        else:
            agent=AgentUserProfile.objects.get(id=pk)
            user=agent.user
            user.delete()
            messages.error(request,"did you fill everything correctly?")
            return redirect('user-login')       



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
    agent=AgentUserProfile.objects.create(user=user,user_name=user.username,email=user.email)
    context={
        'agent':agent,
        }
    return render(request,'user/add-details-agent.html',context)

def createNewTenant(request):
    user=request.user
    tenant=TenantUserProfile.objects.create(user=user,user_name=user.username,email=user.email)
    print(tenant)
    context={
        'tenant':tenant,
        }
    return render(request,'user/add-details-tenant.html',context)

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
        return redirect('/')
    elif tenantProfile is not None:
         return redirect('/')
    else:
        return render(request,'user/google-login-portal.html') 
    


def welcomePage(request):
    return redirect('properties-list')

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
                 return redirect('/')
            if profile is not None:
                 return redirect('/')
            
        else:
            messages.error(request,'username or password incorrect')
            
    return render(request,"user/user-login.html")

    
def logOutUser(request):
    messages.success(request,"Successfully logged out")
    logout(request)
    return redirect('user-login')
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from user.forms import CustomUserCreationForm
from user.models import TenantUserProfile,AgentUserProfile,CustomUser
from .forms import *
def propertyList(request):
    if request.method=='GET':
        type=request.GET.get('type')
        city=request.GET.get('city')
        address=request.GET.get('address')
        minPrice=request.GET.get('min-price')
        maxPrice=request.GET.get('max-price')
        parkingChoice=request.GET.get('parking')
        context={
            'type':type,
            'city':city,
            'address':address,
            'min-price':minPrice,
            'max-price':maxPrice,
            'parling-choice':parkingChoice
        }
        print(context)
        return render(request,'properties/property-list.html',context) 
    else:
        context={
            'city':'none',
            'address':'none'
        }  
        return render(request,'properties/property-list.html',context)
def cancelPorpertyCreation(request,pk):
    temp_property=Property.objects.get(id=pk)
    temp_property.delete()
    Kitchen.objects.filter(property__isnull=True).delete()
    Bathroom.objects.filter(property__isnull=True).delete()
    Bedroom.objects.filter(property__isnull=True).delete()
    return redirect('create-property')

def addVideo(request,pk):
    print('inside add video view')
    if request.method=='POST':
        form=VideoForm(request.POST,request.FILES)
        if form.is_valid():
            print('Image form is valid')
            video=form.save()
            property=Property.objects.get(id=pk)
            video.property=property
            return render(request,'properties/done.html')
        else:
            messages.error(request,'Please fill the details correctly')
            context={'form':PropertyForm()}
            return render(request,'properties/create-properties.html',context)
    else:
        form=VideoForm()
        property=Property.objects.get(id=pk)
        context={'form':form,'property':property}
        return render(request,'properties/add-video.html',context)
    

def addImages(request,pk):
    if request.method=='POST':
        form=BedroomImageForm(request.POST,request.FILES)
        if form.is_valid():
            print('Image form is valid')
            image=form.save()
            property=Property.objects.get(id=pk)
            bedroom=Bedroom.objects.get(property=property)
            image.bedroom=bedroom
            form=BedroomImageForm()
            context={'form':form,'property':property}
            messages.success(request,"image added successfully")
            return render(request,'properties/add-rooms.html',context)
        else:
            messages.error(request,'Please fill the details correctly')
            context={'form':PropertyForm()}
            return render(request,'properties/create-properties.html',context)

def addRooms(request,pk):
    if request.method=='POST':
        room_number={
            'SR':1,
            'DR':2,
            '1BHK':1,
            '2BHK':2,
            '3BHK':3,
            '4BHK':4,
        }
        form=BathroomForm(request.POST,request.FILES)
        if form.is_valid():
            print('Bathroom form is valid')
            bathroom=form.save()
            property=Property.objects.get(id=pk)
            bathroom.property=property
            bedroom=Bedroom.objects.create(numbers=room_number[str(property.category)],property=property)
            bedroom.save()
            form=BedroomImageForm()
            context={'form':form,'property':property}
            return render(request,'properties/add-rooms.html',context)
        else:
            messages.error(request,'Please fill the details correctly')
            context={'form':PropertyForm()}
            return render(request,'properties/create-properties.html',context)
# Create your views here.
def addBathroom(request,pk):
    if request.method=='POST':
        form=KitchenForm(request.POST,request.FILES)
        if form.is_valid():
            print('kitchen form is valid')
            kitchen=form.save()
            property=Property.objects.get(id=pk)
            kitchen.property=property
            form=BathroomForm()
            context={'property':property,'form':form}
            return render(request,'properties/add-bathroom.html',context)
        else:
            messages.error(request,'Please fill the details correctly')
            context={'form':PropertyForm()}
            return render(request,'properties/create-properties.html',context)

def addKitchen(request):
    if request.method=='POST':
        form=PropertyForm(request.POST)
        if form.is_valid():
            saved_property=form.save()
            form=KitchenForm()
            context={'property':saved_property,'form':form}
            return render(request,'properties/add-kitchen.html',context)
        else:
            messages.error(request,'Please fill the details correctly')
            context={'form':form}
            return render(request,'properties/create-properties.html',context)
def createProperty(request):
    
    form=PropertyForm()
    context={'form':form}
    return render(request,'properties/create-properties.html',context)
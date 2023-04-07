from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from user.forms import CustomUserCreationForm
from user.models import TenantUserProfile,AgentUserProfile,CustomUser
from .utils import getAgentFromUser,getTenantFromUser
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/user-login')
def deleteProperty(request,pk):
    property=Property.objects.get(id=pk)
    agent=getAgentFromUser(request.user)
    if property.agent==agent:
        property.delete()
        messages.success(request,'Property has been deleted.')
        return redirect('/')
    else:
        messages.error(request,'Property could not be deleted.')
        return redirect('/')

@login_required(login_url='/user-login')
def deleteBooking(request,pk):
    booking=Bookings.objects.get(id=pk)
    tenant=booking.tenant
    userTenant=getTenantFromUser(request.user)
    if tenant==userTenant:
        booking.delete()
        return redirect('/')
    else:
        return redirect('/')
@login_required(login_url='/user-login')
def bookProperty(request,pk):
    tenant=getTenantFromUser(request.user)
    property=Property.objects.get(id=pk)
    
    duplicate_list=Bookings.objects.filter(tenant=tenant,property=property)
    if len(duplicate_list)>0:
        messages.error(request,'You have booked this property already')
        return redirect('properties-list')
    booking=Bookings.objects.create(tenant=tenant,property=property)
    booking.save()
    property.add_booking()
    property.save()
    messages.success(request,'Booked Successfully')
    return redirect('welcome-page') 
def getImages(request):
    return render(request,'properties/get-images.html')

def showProperty(request,pk):
    property=Property.objects.get(id=pk)
    property.add_view()
    property.save()
    kitchen=Kitchen.objects.get(property=property)
    bathroom=Bathroom.objects.get(property=property)
    videoTour=VideoTour.objects.get(property=property)
    bedroom=Bedroom.objects.get(property=property)
    hasTour=str(videoTour.videofile) !=""
    images=BedroomImage.objects.filter(bedroom=bedroom)
    isBookmarked=False
    if request.user.is_authenticated:
        if getTenantFromUser(request.user) is not None:
            bookmark=Bookings.objects.filter(tenant=getTenantFromUser(request.user),property=property)
            isBookmarked=len(bookmark)>0
    print(isBookmarked)
    context={
        'property':property,
        'kitchen':kitchen,
        'bathroom':bathroom,
        'tourAvailable':hasTour,
        'videotour':videoTour,
        'images':images,
        'isBookmarked':isBookmarked
    }
    return render(request,'properties/show-property.html',context)

def propertyList(request):
    page=request.GET.get('page')
    city_code={
        'Kathmandu':'KTM',
        'Pokhara':'PK',
        'Butwal':'BT',
        'Birtamode':'BTM',
        'Biratnagar':'BTG',
        'Dharan':'DH'
    }
    if request.method=='POST':
        print('at POST')
        type=Category.objects.get(name=request.POST.get('type'))
        city=city_code[request.POST.get('city')]
        address=request.POST.get('address')
        minPrice=request.POST.get('min-price')
        maxPrice=request.POST.get('max-price')
        try:
            property_list=Property.objects.filter(status='OS',category=type,city=city,address__icontains=address).filter(price__range=(minPrice,maxPrice)).order_by('price')
        except:
            messages.error(request,'fill all the information correctly')
            return redirect('prpperties-list')
        if len(property_list)==0:
            print('not found any')
            return render(request,'properties/empty-page.html')
        else:
            paginator=Paginator(property_list,per_page=15)
            page_object=paginator.get_page(page)
            context={'properties':page_object,'total_pages':paginator.page_range}
            return render(request,'properties/property-list.html',context) 

    properties=Property.objects.filter(status='OS').order_by('price')
    if len(properties)==0:
        return render(request,'properties/empty-page.html')
    else:
        paginator=Paginator(properties,per_page=15)
        page_object=paginator.get_page(page)
        context={'properties':page_object,'total_pages':paginator.page_range}
        print(page)
        return render(request,'properties/property-list.html',context)

def cancelPorpertyCreation(request,pk):
    temp_property=Property.objects.get(id=pk)
    temp_property.delete()
    Kitchen.objects.filter(property__isnull=True).delete()
    Bathroom.objects.filter(property__isnull=True).delete()
    Bedroom.objects.filter(property__isnull=True).delete()
    return redirect('create-property')
@login_required(login_url='/user-login')
def addVideo(request,pk):
    print('inside add video view')
    if request.method=='POST':
        form=VideoForm(request.POST,request.FILES)
        if form.is_valid():
            print('Image form is valid')
            video=form.save()
            property=Property.objects.get(id=pk)
            video.property=property
            video.save()
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
    
@login_required(login_url='/user-login')
def addImages(request,pk):
   
    if request.method=='POST':
        property=Property.objects.get(id=pk)
        if request.FILES.get('imageFile') is None:
            messages.error(request,'please choose at least one image')
            context={'property':property}
            return render(request,'properties/add-rooms.html',context)
        print('Image form is valid')
       
        bedroom=Bedroom.objects.get(property=property)
        property.featured_image=request.FILES.get('imageFile')
        
        property.save()
        bedImage=BedroomImage.objects.create(bedroom=bedroom,image=request.FILES.get('imageFile'))
        bedImage.save()
        context={'property':property}
        messages.success(request,"image added successfully")
        return render(request,'properties/add-rooms.html',context)
        
@login_required(login_url='/user-login')
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
            bathroom.save()
            bedroom=Bedroom.objects.create(numbers=room_number[str(property.category)],property=property)
            bedroom.save()
            form=BedroomImageForm()
            context={'form':form,'property':property}
            return render(request,'properties/add-rooms.html',context)
        else:
            messages.error(request,'Please fill the details correctly')
            context={'form':PropertyForm()}
            return render(request,'properties/create-properties.html',context)

@login_required(login_url='/user-login')
def addBathroom(request,pk):
    if request.method=='POST':
        form=KitchenForm(request.POST,request.FILES)
        if form.is_valid():
            print('kitchen form is valid')
            kitchen=form.save()
            property=Property.objects.get(id=pk)
            kitchen.property=property
            kitchen.save()
            form=BathroomForm()
            context={'property':property,'form':form}
            return render(request,'properties/add-bathroom.html',context)
        else:
            messages.error(request,'Please fill the details correctly')
            context={'form':PropertyForm()}
            return render(request,'properties/create-properties.html',context)

@login_required(login_url='/user-login')
def addKitchen(request):
    if request.method=='POST':
        form=PropertyForm(request.POST)
        if form.is_valid():
            agent=getAgentFromUser(request.user)
            saved_property=form.save()
            saved_property.agent=agent
            saved_property.save()
            form=KitchenForm()
            context={'property':saved_property,'form':form}
            return render(request,'properties/add-kitchen.html',context)
        else:
            messages.error(request,'Please fill the details correctly')
            context={'form':form}
            return render(request,'properties/create-properties.html',context)

@login_required(login_url='/user-login')
def createProperty(request):
    if getAgentFromUser(request.user) is None:
        messages.error(request,'You must be  registered agent to post properties.')
        return redirect('/')
    form=PropertyForm()
    context={'form':form}
    return render(request,'properties/create-properties.html',context)
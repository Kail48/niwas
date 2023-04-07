from django.db import models
from user.models import AgentUserProfile,TenantUserProfile
from django.core.validators import MaxValueValidator

import uuid
# Create your models here.

class Category(models.Model):
    
    TYPE_CHOICES=(
        ('SR','Single Room'),
        ('DR','Double Room'),
        ('1BHK','One bedroom, hall and Kitchen'),
        ('2BHK','Two bedroom, hall and Kitchen'),
        ('3BHK','Three bedroom, hall and Kitchen'),
        ('4BHK','four bedroom, hall and Kitchen'),
        )
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name=models.CharField(max_length=5,choices=TYPE_CHOICES,default='1BHK')
    def __str__(self) -> str:
        return self.name


    
class Property(models.Model):
    CITY_CHOICES=(
    ('KTM','Kathmandu'),
    ('PK','Pokhara'),
    ('BT','Butwal'),
    ('BTM','Birtamode'),
    ('BTG','Biratnagar'),
    ('DH','Dharan'),
)
    PARKING_CHOICES=(
        ('NONE','None'),
        ('2W','Two Wheeler'),
        ('4W','Four Wheeler'),
    )
    WATER_CHOICES=(
        ('NONE','None'),
        ('A','Anytime'),
        ('B','Boring Water'),
        ('T','Tank Water'),
    )
    STATUS_CHOICES=(
        ('OS','On sale'),
        ('S','Sold'),
    )
    title=models.CharField(max_length=200)
    status=models.CharField(max_length=5,choices=STATUS_CHOICES,default='OS')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    description=models.TextField(null=True,blank=True)
    featured_image=models.ImageField(blank=True,upload_to='image/',default='image/city.jpeg')
    created=models.DateTimeField(auto_now_add=True)
    agent=models.ForeignKey(AgentUserProfile,on_delete=models.CASCADE,null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    city=models.CharField(max_length=5,choices=CITY_CHOICES,default='KTM')
    address=models.CharField(max_length=200,null=True)
    parking=models.CharField(max_length=5,choices=PARKING_CHOICES,default='1BHK')
    water=models.CharField(max_length=5,choices=WATER_CHOICES,default='NONE')
    views=models.IntegerField(default=0,blank=True)
    reservations=models.IntegerField(default=0,blank=True)
    def __str__(self) -> str:
        return self.title

    def add_view(self):
        self.views+=1
    
    def add_booking(self):
        self.reservations+=1
    
class Kitchen(models.Model):
    TYPE_CHOICES=(
        ('N','Not Available'),
        ('SEP','Separated'),
        ('AT','Attached')
    )

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    type=models.CharField(max_length=5,choices=TYPE_CHOICES,default='SEP')
    property=models.ForeignKey(Property,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='image/',blank=True,default='image/noimage.png')

class Bathroom(models.Model):
    TYPE_CHOICES=(
        ('SHR','Shared'),
        ('SEP','Separated')
    )
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    property=models.ForeignKey(Property,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=5,choices=TYPE_CHOICES,default='SEP')
    image=models.ImageField(upload_to='image/',blank=True,default='image/noimage.png')

class Bedroom(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    numbers=models.PositiveIntegerField(default=1, validators=[MaxValueValidator(100)],null=True)
    property=models.ForeignKey(Property,on_delete=models.CASCADE,null=True)


class BedroomImage(models.Model):
     id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
     bedroom=models.ForeignKey(Bedroom,on_delete=models.CASCADE)
     image=models.ImageField(upload_to='image/')

     def __str__(self):
        return str(self.image)

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='video/', null=True, blank=True,verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)
class VideoTour(models.Model):
    name= models.CharField(max_length=500)
    property=models.ForeignKey(Property,on_delete=models.CASCADE,null=True)
    videofile= models.FileField(upload_to='video/', null=True, blank=True,verbose_name="")

    def __str__(self):
        return str(self.videofile)

class Bookings(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created=models.DateTimeField(auto_now_add=True)
    tenant=models.ForeignKey(TenantUserProfile,on_delete=models.PROTECT)
    property=models.ForeignKey(Property,on_delete=models.PROTECT)
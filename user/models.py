from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import uuid
# Create your models here.

class CustomUser(AbstractUser):
    TYPE_CHOICES=(
        ('A','Agent'),
        ('T','Tenant'),
        ('N','Not assigned'),
    )
    type=models.CharField(max_length=5,choices=TYPE_CHOICES,default='N')
    def __str__(self):
        return self.username
#
class AgentUserProfile(models.Model):
     user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
     profile_picture=models.ImageField(blank=True,upload_to='image/',default='image/user.png')
     name=models.CharField(max_length=200,blank=True,null=True)
     user_name=models.CharField(max_length=200,blank=True,null=True)
     phone_number = PhoneNumberField(blank=True)
     email=models.EmailField(max_length=500,blank=True,null=True)
     created=models.DateTimeField(auto_now_add=True)
     id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

     def __str__(self):
        return str(self.user_name)


class TenantUserProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    user_name=models.CharField(max_length=200,blank=True,null=True)
    phone_number = PhoneNumberField(blank=True)
    email=models.EmailField(max_length=500,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.user_name)



    
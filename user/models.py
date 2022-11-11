from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
#
class AgentUserProfile(models.Model):
     user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
     name=models.CharField(max_length=200,blank=True,null=True)
     user_name=models.CharField(max_length=200,blank=True,null=True)
     email=models.EmailField(max_length=500,blank=True,null=True)
     created=models.DateTimeField(auto_now_add=True)
     id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

     def __str__(self):
        return str(self.user_name)


class TenantUserProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    user_name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=500,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.user_name)



    
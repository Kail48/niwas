from user.models import *
from .models import *

def getAgentFromUser(user):
    profile=None
    try:
        profile=AgentUserProfile.objects.get(user=user)
    except:
        return None
    
    return profile

def isOwnerProfile(user,owner_profile):
    return user==owner_profile.user

def getTenantFromUser(user):
    profile=None
    try:
        profile=TenantUserProfile.objects.get(user=user)
    except:
        return None
    
    return profile
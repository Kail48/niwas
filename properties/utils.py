from user.models import *
from .models import *

def getAgentFromUser(user):
    profile=None
    try:
        profile=AgentUserProfile.objects.get(user=user)
    except:
        return None
    
    return profile

def isOwner(user,owner_profile):
    return user==owner_profile.user
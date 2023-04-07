import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")

# your imports, e.g. Django models

from properties.models import *
from user.models import AgentUserProfile
import random
price_range=range(5000,30000)
agent=AgentUserProfile.objects.get(name='agent1')
city_list=['KTM','PK','BTG','DH','BT','BTM']
category_name_list=['SR','DR','1BHK','2BHK','3BHK','4BHK']
address_list=['hattiban','maitidevi','ratnapark','baneshwor','kalanki','koteshwor']
parking_list=['NONE','2W','4W']
for i in range(0,50):
 p=Property(agent=agent,city=random.choice(city_list),category=random.choice(c_list),address=random.choice(address_list),parking=random.choice(parking_list),price=random.randrange(5000.00,30000.00),title='property'+str(i))
 p.save()

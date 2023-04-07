from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Property)
admin.site.register(Category)
admin.site.register(Kitchen)
admin.site.register(Bathroom)
admin.site.register(Bedroom)
admin.site.register(BedroomImage)
admin.site.register(VideoTour)
admin.site.register(Bookings)


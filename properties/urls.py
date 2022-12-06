
from django.urls import path
from . import views

urlpatterns = [
    path('is-working/',views.isWorking,name='is-working'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('tenant-register/',views.tenantRegister,name="tenant-register"),
    path('agent-register/',views.agentRegister,name="agent-register"),
    path('',views.welcomePage,name="welcome-page"),

]

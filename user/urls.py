
from django.urls import path
from . import views

urlpatterns = [
    path('user-login/',views.userLogin,name="user-login"),
    
    path('tenant-register/',views.tenantRegister,name="tenant-register"),
    path('agent-register/',views.agentRegister,name="agent-register"),
    path('',views.welcomePage,name="welcome-page"),
    path('social/signup/',views.signupRedirect,name="signup-redirect"),
    path('logout-user/',views.logOutUser,name="logout-user"),
    path('google-login-portal/',views.googleLoginPortal,name='google-login-portal'),

]

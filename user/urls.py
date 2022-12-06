
from django.urls import path
from . import views

urlpatterns = [
    path('user-login/',views.userLogin,name="user-login"),
    path('new-user-register/',views.newUserRegister,name="new-user-register"),
    path('',views.welcomePage,name="welcome-page"),
    path('social/signup/',views.signupRedirect,name="signup-redirect"),
    path('logout-user/',views.logOutUser,name="logout-user"),
    path('google-login-portal/',views.googleLoginPortal,name='google-login-portal'),
    path('create-new-agent',views.createNewAgent,name='create-new-agent'),
    path('create-new-tenant',views.createNewTenant,name='create-new-tenant'),
]

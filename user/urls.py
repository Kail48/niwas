
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
    path('complete-tenant-profile/<str:pk>',views.completeTenantProfile,name='complete-tenant-profile'),
    path('test-template',views.testTemplate,name='test-template'),
    path('view-agent-profile/',views.viewAgentProfile,name='view-agent-profile'),
    path('view-bookings/',views.viewBookings,name='view-bookings'),
    path('view-tenant-profile/',views.viewTenantProfile,name='view-tenant-profile'),
    path('view-profile/',views.viewProfile,name='view-profile'),
    path('complete-agent-profile/<str:pk>',views.completeAgentProfile,name='complete-agent-profile'),
]

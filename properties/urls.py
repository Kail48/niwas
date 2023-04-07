
from django.urls import path
from . import views

urlpatterns = [
    path('create-property',views.createProperty,name='create-property'),
    path('add-kitchen',views.addKitchen,name='add-kitchen'),
    path('add-bathroom/<str:pk>',views.addBathroom,name='add-bathroom'),
     path('delete-property/<str:pk>',views.deleteProperty,name='delete-property'),
    path('add-room/<str:pk>',views.addRooms,name='add-room'),
    path('add-images/<str:pk>',views.addImages,name='add-images'),
    path('add-video/<str:pk>',views.addVideo,name='add-video'),
    path('get-images/',views.getImages,name='get-images'),
    path('properties-list/',views.propertyList,name='properties-list'),
    path('cancel-property-creation/<str:pk>',views.cancelPorpertyCreation,name='cancel-property-creation'),
    path('show-property/<str:pk>',views.showProperty,name='show-property'),
    path('book-property/<str:pk>',views.bookProperty,name='book-property'),
     path('delete-booking/<str:pk>',views.deleteBooking,name='delete-booking'),
]

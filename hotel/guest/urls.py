from django.urls import path
from guest.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home',HomeView.as_view(),name="home"),
    path('room/<str:rd>',RoomView.as_view(),name="room"),
    path('roomdet/<int:room_id>',RoomDetailsView.as_view(),name="det"),
    path('booking/<int:room_id>',BookingView.as_view(),name="booking"),
    path('bookedlist',BookedListView.as_view(),name="blist"),
    path('cancelbooking/<int:bid>',cancelbooking,name="cancel"),
    path('gallery',GalleryView.as_view(),name="gal")





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.contrib import messages

from django.views.generic import TemplateView,DetailView,ListView
from website.models import Rooms,Booking
from django.core.mail import send_mail


# Create your views here.
class HomeView(TemplateView):
    template_name="home.html"

class RoomView(ListView):
    template_name="rooms.html"
    queryset=Rooms.objects.all()
    context_object_name="data"

    def get_queryset(self) -> QuerySet[Any]:
        qs=super().get_queryset()
        qs=qs.filter(type=self.kwargs.get('rd'))
        return qs
    
       
class RoomDetailsView(DetailView):
    template_name="room_detail.html"
    queryset=Rooms.objects.all()
    pk_url_kwarg="room_id"
    context_object_name="room"




class BookingView(TemplateView):
    template_name = "booking.html"

    def post(self, request, *args, **kwargs):
        try:
            rid = kwargs.get('room_id')
            room = Rooms.objects.get(id=rid)
            guest = request.user
            arrival = request.POST.get('arr')
            add = request.POST.get('address')
            ph = request.POST.get('phone')
            no_of_guests = int(request.POST.get('guests'))  
            no_of_days = int(request.POST.get('days', 1))  
            room.save()
            booking = Booking.objects.create(room=room,guest=guest,address=add,phone=ph,check_in_date=arrival,number_of_guests=no_of_guests,number_of_days=no_of_days)
            subject = "Booking Confirmation - Cozy Heaven"
            msg = (
                f"Dear {guest.first_name},\n\n"
                f"Greetings from Cozy Heaven!\n\n"
                f"We are delighted to confirm your booking for the room '{room.title}'. Here are the details of your stay:\n\n"
                f"Booking Details:\n"
                f"- Guest Name: {guest.first_name}\n"
                f"- Check-in Date: {booking.check_in_date}\n"
                f"- Number of Days: {booking.number_of_days}\n"
                f"- Room Type: {room.title}\n"
                f"- Number of Guests: {booking.number_of_guests}\n\n"
                f"If you have any questions or need further assistance, please do not hesitate to contact us.\n\n"
                f"We look forward to welcoming you to Cozy Heaven and wish you a pleasant stay!\n\n"
                f"Warm regards,\n"
                f"Cozy Heaven"
            )
            from_email = "rishika242003@gmail.com"
            to_email = [guest.email]
            send_mail(subject, msg, from_email, to_email)
            messages.success(request, "Your Booking is Successful!!")
            return redirect('home')
        except Exception as e:
            print(e)
            messages.error(request, "Booking Failed")
            return redirect('home')

class BookedListView(ListView):
    template_name="booked_list.html"
    queryset=Booking.objects.all()
    context_object_name="booked"

    def get_queryset(self) -> QuerySet[Any]:
        qs=super().get_queryset()
        qs=qs.filter(guest=self.request.user)
        return qs

def cancelbooking(request,*args,**kwargs):
    try:
        bid=kwargs.get('bid')
        booked=Booking.objects.get(id=bid)
        subject = "Room Booking Cancellation Acknowledgment"
        msg = (
            f"Dear {booked.guest.first_name},\n\n"
            f"We regret to inform you that your booking for the room '{booked.room.title}' has been successfully cancelled.\n\n"
            f"Here are the details of your cancelled booking:\n"
            f"- Room Title: {booked.room.title}\n"
            f"- Check-in Date: {booked.check_in_date}\n"
            f"- Number of Guests: {booked.number_of_guests}\n\n"
            f"If you have any questions or need further assistance, please do not hesitate to contact us.\n\n"
            f"Thank you for considering Cozy Heaven, and we hope to welcome you in the future.\n\n"
            f"Warm regards,\n"
            f"Cozy Heaven"
        )
        fr_om="rishika242003@gmail.com"
        to_ad=[booked.guest.email]

        send_mail(subject,msg,fr_om,to_ad)
        booked.delete()
        messages.success(request,"Booking cancelled!")
        return redirect('blist')
    except Exception as e:
        messages.error(request,e)
        return redirect('blist')
    

class GalleryView(TemplateView):
    template_name="gallery.html"

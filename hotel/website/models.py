from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Rooms(models.Model):
    title=models.CharField(max_length=100)
    rent=models.PositiveBigIntegerField()
    image1=models.ImageField(upload_to='room_img')
    image2 = models.ImageField(upload_to='room_img',blank=True, null=True)
    image3 = models.ImageField(upload_to='room_img', blank=True, null=True)
    image4 = models.ImageField(upload_to='room_img', blank=True, null=True)
    image5 = models.ImageField(upload_to='room_img', blank=True, null=True)
    
    
    options=(
        ("standard room","standard room"),
        ("deluxe room","deluxe room"),
        ("suite room","suite room"),
        ("connecting room","connecting room")
                       
    )
    type=models.CharField(max_length=100,choices=options)
    description=models.CharField(max_length=1000,default='')
    amenities=models.TextField(max_length=1000,default='')
    bathroom=models.TextField(max_length=1000,default='')
    special_features=models.TextField(max_length=1000,default='')
    policies=models.TextField(max_length=1000,default='')
    additional_info=models.TextField(max_length=1000,default='')
    def __str__(self):
        return self.title


class Booking(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    guest=models.ForeignKey(User,on_delete=models.CASCADE)
    check_in_date=models.DateField(default=timezone.now)
    number_of_days=models.IntegerField(default=1)
    number_of_guests = models.PositiveIntegerField(blank=True,null=True)
    status_opt=(
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending')
    )
    status=models.CharField(max_length=200,default="confirmed",choices=status_opt)
    address=models.CharField(max_length=500)
    phone=models.PositiveIntegerField()
    
    @property
    def total_rent(self):
        trent=self.room.rent*self.number_of_days
        return trent




    

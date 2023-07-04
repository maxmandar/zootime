from django.shortcuts import render, redirect
from .models import Ride, Booking
from .forms import BookingForm
from decimal import Decimal
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings


# def booking_view(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST, request=request)  # Pass the request object to the form
#         if form.is_valid():
#             booking = form.save()
#             # Apply a 5% discount to the ride's price
#             booking.ride.price *= Decimal('0.95')
#             booking.ride.save()
#             # messages.success(request, 'Booking successful!')
#             return render(request, 'booking/booking_confirmation.html', {'booking': booking})  
#     else:
#         form = BookingForm(request=request)  # Pass the request object to the form

#     rides = Ride.objects.all()
#     return render(request, 'booking/booking_form.html', {'form': form ,'rides': rides})


# def booking_view(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save()  # The final price with discount is now saved with the booking
#             return render(request, 'booking/booking_confirmation.html', {'booking': booking})
#     else:
#         form = BookingForm()

#     rides = Ride.objects.all()
#     return render(request, 'booking/booking_form.html', {'form': form, 'rides': rides})


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # Save the form data but don't commit to the database yet
            ride = booking.ride
            quantity = booking.quantity

            # Apply a 5% discount to the ride's price and calculate the final price
            discounted_price = ride.price * quantity * Decimal('0.95')
            booking.final_price = discounted_price

            booking.save()  # Now save the booking with the final price

             # Send email notification to the developer
            subject = f'Zoo Time New Booking Notification - Booking ID: {booking.id}'
            message = f'A new booking has been made.\n\nBooking ID: {booking.id}\nRide: {ride.name}\nQuantity: {quantity}\nTotal Price: {discounted_price}'
            recipient_list = [settings.DEVELOPER_EMAIL]  # Replace with your email address
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

            # Send email confirmation to the user
            user_subject = f'Zoo Time Booking Confirmation - Booking ID: {booking.id}'
            user_message = f'Thank you for your booking.\n\nBooking ID: {booking.id}\nRide: {ride.name}\nQuantity: {quantity}\nTotal Price: {discounted_price}'
            user_recipient = booking.email
            send_mail(user_subject, user_message, settings.DEFAULT_FROM_EMAIL, [user_recipient])


            return render(request, 'booking/booking_confirmation.html', {'booking': booking})
    else:
        form = BookingForm()

    rides = Ride.objects.all()
    return render(request, 'booking/booking_form.html', {'form': form, 'rides': rides})
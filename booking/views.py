from django.shortcuts import render, redirect
from .models import Ride, Booking
from .forms import BookingForm
from decimal import Decimal
from django.contrib import messages

# def booking_view(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save()
#             # Apply a 5% discount to the ride's price
#             booking.ride.price *= Decimal('0.95')
#             booking.ride.save()
#             return render(request, 'booking/booking_confirmation.html', {'booking': booking})
#     else:
#         form = BookingForm()
#     return render(request, 'booking/booking_form.html', {'form': form})



def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request=request)  # Pass the request object to the form
        if form.is_valid():
            booking = form.save()
            # Apply a 5% discount to the ride's price
            booking.ride.price *= Decimal('0.95')
            booking.ride.save()
            # messages.success(request, 'Booking successful!')
            return render(request, 'booking/booking_confirmation.html', {'booking': booking})  
    else:
        form = BookingForm(request=request)  # Pass the request object to the form

    return render(request, 'booking/booking_form.html', {'form': form})
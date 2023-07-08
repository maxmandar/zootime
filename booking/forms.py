from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Ride, Booking
from decimal import Decimal


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'ride', 'quantity']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email address is required.")
        # Add your email validation logic here if needed
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not full_name:
            raise forms.ValidationError("Full name is required.")
        # Add your full name validation logic here if needed
        return full_name

    def clean(self):
        cleaned_data = super().clean()
        ride = cleaned_data.get("ride")
        quantity = cleaned_data.get("quantity")

        if ride and quantity:
            # Apply a 5% discount to the ride's price
            discounted_price = ride.price * quantity * Decimal('0.95')
            self.cleaned_data["final_price"] = discounted_price
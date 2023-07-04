from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Ride, Booking
from decimal import Decimal


# class BookingForm(forms.ModelForm):
#     email_confirmation = forms.EmailField(required=True)

#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)  # Store the request object
#         super().__init__(*args, **kwargs)

#     class Meta:
#         model = Booking
#         fields = ['full_name', 'email', 'email_confirmation', 'ride', 'quantity']

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('email')
#         email_confirmation = cleaned_data.get('email_confirmation')

#         if email != email_confirmation:
#             raise forms.ValidationError("Emails must match.")

#         return cleaned_data

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.save()

#         # Access the request object and display a success message
#         if self.request:
#             messages.success(self.request, 'Booking successful!')

#         return instance
    
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
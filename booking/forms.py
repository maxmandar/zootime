from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Ride, Booking

# class BookingForm(forms.ModelForm):
#     email_confirmation = forms.EmailField(required=True)

#     class Meta:
#         model = Booking
#         fields = ['full_name', 'email', 'email_confirmation', 'ride', 'quantity']

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('email')
#         email_confirmation = cleaned_data.get('email_confirmation')

#         if email != email_confirmation:
#             raise ValidationError("Emails must match.")

#         return cleaned_data

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.save()

#         # Display a success message
#         messages.success(self.request, 'Booking successful!')

#         return instance


class BookingForm(forms.ModelForm):
    email_confirmation = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Store the request object
        super().__init__(*args, **kwargs)

    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'email_confirmation', 'ride', 'quantity']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        email_confirmation = cleaned_data.get('email_confirmation')

        if email != email_confirmation:
            raise forms.ValidationError("Emails must match.")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()

        # Access the request object and display a success message
        if self.request:
            messages.success(self.request, 'Booking successful!')

        return instance
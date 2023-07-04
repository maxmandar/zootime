from django.shortcuts import render
from django.core.mail import send_mail

from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST['fullname']
        email = request.POST['email']
        inquiry = request.POST['inquiry']
        
        # Validation can be added here

        # Send an email with the inquiry
        send_mail(
            f'Inquiry from {name}',
            inquiry,
            email,
            ['zoo.time.contact@gmail.com'], 
        )
        
        messages.success(request, 'Your message has been sent. Thank you for contacting us.')

    return render(request, 'contact/contact.html')

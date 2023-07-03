from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ElectronicRide

def homepage_view(request):
    rides = ElectronicRide.objects.all()
    return render(request, 'homepage/homepage.html', {'rides': rides})

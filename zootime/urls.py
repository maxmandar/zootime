from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('booking/', include('booking.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('developer/', include('developer.urls')),
    # path('', include('website.urls')),
]

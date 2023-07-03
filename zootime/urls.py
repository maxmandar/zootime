from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('booking/', include('booking.urls')),
    # path('', include('website.urls')),
]

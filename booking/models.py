from django.db import models
from django.core.validators import MinValueValidator

class Ride(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return f"{self.name} for ${self.price}"


class Booking(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    booking_time = models.DateTimeField(auto_now_add=True)
    final_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)  # New field for storing the final price after discount

    def __str__(self):
        return f"Booking for {self.ride.name} by {self.full_name}"
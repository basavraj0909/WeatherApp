from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather in {self.city}"

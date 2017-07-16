from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30, default="", blank=False)
    last_name = models.CharField(max_length=30, default="", blank=False)
    company = models.CharField(max_length=50, default="None", blank=False)

    def __str__(self):
        return format(self.last_name) + ", " + format(self.first_name)

from django.db import models
from django.urls import reverse

class user(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('users:user_detail', args=[str(self.id)])

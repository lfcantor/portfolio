from django.db import models
from django.urls import reverse
from users.models import user

class food(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('foods:food_detail', args=[str(self.id)])


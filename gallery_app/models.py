from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class GalleryInfo(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    artist = models.CharField(max_length=32)
    restored = models.BooleanField(default=False)
    description = models.CharField(max_length=64)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.artist
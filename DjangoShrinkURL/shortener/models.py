from django.db import models
from django.contrib.auth.models import User 

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = generate_code()  # TO DO: Define this function later
        super().save(*args, **kwargs)

    def __str__(self):
        return self.original_url

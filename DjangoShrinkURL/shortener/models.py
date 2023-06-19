import uuid
from django.db import models
from django.contrib.auth.models import User 

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    times_visited = models.IntegerField(default=0)  # New field here

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.generate_code()
        super().save(*args, **kwargs)
    
    def generate_code(self):
        self.short_url = str(uuid.uuid4())[:8]

    def __str__(self):
        return self.original_url

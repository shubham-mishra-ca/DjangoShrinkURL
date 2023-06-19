import uuid
from django.db import models
from django.contrib.auth.models import User 


class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    times_visited = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_code()
        super().save(*args, **kwargs)
    
    @staticmethod
    def generate_code():
        new_uuid = uuid.uuid4()
        return str(new_uuid)[:8] 
    
    def __str__(self):
        return self.original_url

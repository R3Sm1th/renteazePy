from django.db import models
from datetime import datetime
# Create your models here.
class Agent(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.first_name

from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#ForeignKey=link to another model, to create a recursive relation
    title=models.CharField(max_length=1000)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.

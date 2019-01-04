from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # getting published_date from database and saving it
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    # getting data from database and returning its title
    def __str__(self):
        return self.title

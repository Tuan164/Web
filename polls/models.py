from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=100)

    def get_topic(self):
        return self.topic
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link

class Feedback(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = RichTextField()
    time = models.DateTimeField(auto_now_add=True)

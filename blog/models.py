from django.db import models
from django.utils import timezone

# class is a special keyword that indicates that we are defining an object.
# Post is the name of our model.
# models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database
# Each model is a Python class that subclasses django.db.models.Model.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # text with a limited number of characters.
    title = models.CharField(max_length=200)
    #long text without a limit.
    text = models.TextField() 
    #date and time.
    created_date = models.DateTimeField( 
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




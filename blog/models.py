from django.db import models
from django.conf import settings
from django.utils import timezone

#class is  a keyword that indicates we are defining an object.
#Post is name of our model, always strt class name with CAP
#models.Model means that Post is a Django model, so Django knows tht it should be saved in database
#models.charfield = to define text with limited number of characters
#models.TExtField = long text w/o limit
#models.DateTimeField = date and time
#models.foreignkey = link to other model
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
    
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Events(models.Model):
    event_name = models.CharField(max_length=150,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    year = models.IntegerField(blank=True,null=True)
    month = models.CharField(max_length=50,blank=True,null=True)
    date = models.IntegerField(blank=True,null=True)
    body = models.CharField(max_length=1000,blank=True,null=True)
    slug = models.SlugField(null=True,blank=True,max_length=200)

    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.event_name)

            has_slug = Events.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count+=1
                slug = slugify(self.event_name) + '-' + str(count)
                has_slug = Events.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args,**kwargs)
from django.db import models
from django.utils.text import slugify
# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='blogs/',null=True,blank=True)

    slug = models.SlugField(unique=True,null=True, blank=True)

    def __str__(self):

        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
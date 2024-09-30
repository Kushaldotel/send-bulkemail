from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=200)
    short_description = models.TextField(null=True, blank=True)
    description = CKEditor5Field('Description', config_name='default')
    banner_image = models.ImageField(upload_to='blogs/',null=True,blank=True)

    slug = models.SlugField(unique=True,null=True, blank=True)

    def __str__(self):

        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
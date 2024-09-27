from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Services(models.Model):

    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = CKEditor5Field('Description', config_name='default')
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    banner_image = models.ImageField(upload_to='services/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
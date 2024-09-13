from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    suscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = "Users Information"
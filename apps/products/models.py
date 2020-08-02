from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class ProductOne(models.Model):
    title = models.CharField(_('Title'), max_length=255)

    def __str__(self):
        return f"{self.title}"

class ProductTwo(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    
    def __str__(self):
        return f"{self.title}"
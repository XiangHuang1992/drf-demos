from django.db import models


# Create your models here.
class Toy(models.Model):
    create = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    toy_category = models.CharField(max_length=20, blank=False, default='')
    release_date = models.DateTimeField()
    was_include_in_home = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

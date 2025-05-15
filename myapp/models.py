from django.db import models

# Create your models here.
from django.db import models

class TodoappModel(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


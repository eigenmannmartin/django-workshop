from django.db import models


class Todo(models.Model):
    description = models.CharField(max_length=1000)
    created     = models.DateTimeField(editable=False, auto_now_add=True)
    modified    = models.DateTimeField(editable=False, auto_now=True)
    collection  = models.ForeignKey('Collection', on_delete=models.CASCADE)
    done        = models.BooleanField(default=False)


class Collection(models.Model):
    name        = models.CharField(max_length=200)
    created     = models.DateTimeField(editable=False, auto_now_add=True)
    modified    = models.DateTimeField(editable=False, auto_now=True)
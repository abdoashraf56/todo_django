from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=70)
    user = models.ForeignKey(User, null = True , on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Todo(models.Model):
    user = models.ForeignKey(User, null = True , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    endAt = models.DateTimeField(blank=True, null=True)
    finish = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.name

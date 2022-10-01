from django.db import models


class Fibonacci(models.Model):
    id = models.AutoField(primary_key=True)
    index = models.IntegerField()
    value = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

from django.db import models


class ResultRecord(models.Model):
    id = models.AutoField(primary_key=True)
    method = models.CharField(max_length=256)
    index = models.IntegerField()
    value = models.BigIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}, {self.method}, {self.index} -> {self.value} ({self.created})"

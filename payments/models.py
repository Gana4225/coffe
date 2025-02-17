from django.db import models

class coff(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField(default=0)
    pid = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name
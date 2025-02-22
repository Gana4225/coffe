from django.db import models

class coff(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField(default=0)
    pid = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class cofffdata(models.Model):
    name = models.CharField(max_length=200,null=False)
    image = models.ImageField(upload_to="images/",blank=True,null=True)
    price = models.IntegerField(default=0,null=False)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.name
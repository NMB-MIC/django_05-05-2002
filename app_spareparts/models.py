from django.db import models

# Create your models here.
class Sparepart(models.Model):

    name = models.CharField(max_length=50)
    part_number = models.CharField(max_length=50,null=True,unique=True)
    qty = models.PositiveIntegerField()
    maker = models.CharField(max_length=50)
    registered_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'media/images/',unique=True)

    def __str__(self):
        return self.name
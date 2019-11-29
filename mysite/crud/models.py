from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField (max_length=225)
    nim = models.IntegerField()

    class Meta:
        ordering = ['-id']
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Aktyor(models.Model):
    ism = models.CharField(max_length=255)
    davlat = models.CharField(max_length=200, blank=True, null=True)
    jins = models.CharField(max_length=10, choices=(('Erkak', 'Erkak'), ('Ayol', 'Ayol')))
    t_sana = models.DateField()

    def __str__(self):
        return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=200)
    yil = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
    aktyorlar = models.ManyToManyField(Aktyor)

    def __str__(self):
        return self.nom

class Tarif(models.Model):
    nom = models.CharField(max_length=200)
    narx = models.FloatField(validators=[MinValueValidator(0)])
    izoh = models.TextField(blank=True, null=True)
    davomiylik = models.DurationField()

    def __str__(self):
        return self.nom

class Izoh(models.Model):
    matn = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    baho = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        r = f"{self.user.username}"
        if self.matn:
            r += f": {self.matn}"
        return r



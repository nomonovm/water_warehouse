from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

ISH_VAQTI_CHOICES = (('08:00 - 12:30', '08:00 - 12:30'), ('12:30 - 18:00', '12:30 - 18:00'))


class Suv(models.Model):
    brend = models.CharField(max_length=222)
    narx = models.FloatField(validators=[MinValueValidator(0.0)])
    litr = models.FloatField(validators=[MinValueValidator(0.0)])
    batafsil = models.TextField(blank=True, null=True)


class Mijoz(models.Model):
    ism = models.CharField(max_length=222)
    tel = models.CharField(max_length=15, blank=True, null=True, unique=True)
    manzil = models.CharField(max_length=222, blank=True, null=True)
    qarz = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)


class Sotuvchi(AbstractUser):
    yosh = models.IntegerField(validators=[MinValueValidator(18)], null=True, blank=True)
    ish_vaqti = models.CharField(max_length=20, choices=ISH_VAQTI_CHOICES)


class Haydovchi(models.Model):
    ism = models.CharField(max_length=255)
    tel = models.CharField(max_length=15, unique=True)
    ish_vaqti = models.CharField(max_length=20, choices=ISH_VAQTI_CHOICES)


class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
    miqdor = models.FloatField(validators=[MinValueValidator(0.0)])
    narxi = models.FloatField(validators=[MinValueValidator(0.0)])

    class Meta:
        ordering = ['-created_at']
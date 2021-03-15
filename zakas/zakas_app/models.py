from django.db import models

# Create your models here.
class mahsulotlar(models.Model):
    nomi = models.CharField(max_length=100)
    rasmi = models.ImageField(upload_to='mahsulotlar')
    narxi = models.IntegerField()
    
    def __str__(self):
        return self.nomi
    
class yetishtirilayotgan_mahsulotlar(models.Model):
    rasmi = models.ImageField(upload_to='yetishtirilayotgan_mahsulotlar')
    nomi = models.CharField(max_length=100)
    sana = models.DateField()
    malumot = models.TextField()
    
    def __str__(self):
        return self.nomi
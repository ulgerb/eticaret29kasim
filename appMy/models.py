from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı (Satıcı)"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    title = models.CharField(("Ürün Adı"), max_length=50)
    text = models.TextField(("Açıklama"), max_length=500)
    image = models.FileField(("Fotoğraf"), upload_to="", max_length=100)
    price = models.FloatField(("Fiyat"),default=0)
    stok = models.IntegerField(("Stok"), default=0)
    date_now = models.DateField(("Tarih"), auto_now_add=True)
    likes = models.FloatField(("Beğeni Ortalaması"), default=0)

    def __str__(self):
        return self.title


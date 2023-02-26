from django.db import models
from django.template.defaultfilters import slugify
import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey("Category", verbose_name=("Kategori"), on_delete=models.CASCADE)
    name = models.CharField(("Adı"), max_length=75)
    desc = models.CharField(("Açıklama"), max_length=255, default='')
    price = models.DecimalField(("Fiyatı"), max_digits=5, decimal_places=2)
    productaci = models.BooleanField(("Acılı var mı ?"), default=False, blank=True, null=True,)
    image = models.FileField(("Fotoğraf"), max_length=100)
    slug = models.SlugField(("Slug"), blank= True, null=True)
    is_active = models.BooleanField(("Satışta mı?"))
    offer = models.BooleanField(("Kampanya var mı?"), default=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.replace("ı", "i"))
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
class Shopper(models.Model):
    name = models.CharField(("Ad soyad"), max_length=120)
    phone = models.CharField(("Telefon"), max_length=120)
    city = models.CharField(("Şehir"), max_length=120)
    town = models.CharField(("İlçe"), max_length=120)
    suburb = models.CharField(("Mahalle"), max_length=120)
    street = models.CharField(("Cadde"), max_length=120)
    homeno = models.CharField(("Bina no"), max_length=120)
    homename = models.CharField(("Bina Adı"), max_length=120)
    productdetail = models.CharField(("Ürün detayı"), max_length=255)
    odemeturu = models.BooleanField(("Nakit mi?"), default=True)
    productlist = models.ManyToManyField("Product", verbose_name=("Sipariş Listesi"))
    date_now = models.DateField(("Sipariş Tarihi"), auto_now_add=True, blank=True, null=True)
    time_now = models.TimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    finished = models.BooleanField(("Teslim Edildi"), default=False)
    total = models.DecimalField(("Toplam Tutar"), max_digits=5, decimal_places=2, default=0)
    alindi = models.BooleanField(("Sipariş alındı mesajı"), default = False, blank=True, null=True)
    teslim = models.BooleanField(("Teslim edildi mesajı"), default = False, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Cari(models.Model):
    ciro = models.DecimalField(("ciro"), max_digits=9, decimal_places=2, default=0)
    date_now = models.DateField(("Tarih"), auto_now_add=True, blank=True, null=True, db_index=True, unique=True)
    time_now = models.TimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    month = models.IntegerField(("Ay"), default=datetime.datetime.now().month)
    
class Daire(models.Model):
    kebaplar = models.IntegerField(("Kebaplar"), default=0,blank=True, null=True)
    pideler = models.IntegerField(("Pideler"), default=0,blank=True, null=True)
    diger = models.IntegerField(("Diğer"), default=0,blank=True, null=True)
    month = models.IntegerField(("Ay"), default=datetime.datetime.now().month)
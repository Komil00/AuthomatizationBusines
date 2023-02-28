from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Zavod(models.Model):
    name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?998?\d{9}$', message="Phone number must be entered in the format: '+998********'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
     
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ("Zavod")
        verbose_name_plural = ("Zavodlar")

class Mahsulot(models.Model):
    name = models.CharField(max_length=200)
    ishlab_chiqarilgan_korxona = models.ForeignKey(Zavod, on_delete=models.CASCADE, related_name='ishlab_chiqarilgan_korxona')
    ishlab_chiqarilgan_sana = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Mahsulot")
        verbose_name_plural = ("Mahsulots")
    
class Client(models.Model):
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?998?\d{9}$', message="Phone number must be entered in the format: '+998********'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")

class ClientQarzlari(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_to_clientqarzlari')
    mahsulot_nomi = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='mahsulot_nomi_to_clientqarzlari')
    mahsulot_soni = models.FloatField()
    bitta_mahsulot_narxi = models.FloatField()
    qarz_berish_vaqti = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("ClientQarzlari")
        verbose_name_plural = ("ClientQarzlari")  

class OlganMahsulot(models.Model):
    zavod_nomi = models.ForeignKey(Zavod, models.CASCADE, related_name='zavod_to_olganmahsulot')
    mahsulot_nomi = models.ForeignKey(Mahsulot, models.CASCADE, related_name='mahsulot_to_olganmahsulot')
    mahsulot_soni = models.FloatField()
    bitta_mahsulot_narxi = models.FloatField()
    olgan_vaqt = models.DateField(auto_now=True)

    def __str__(self):
        return self.mahsulot_nomi.name
    
    class Meta:
        verbose_name = ("OlganMahsulot")
        verbose_name_plural = ("OlganMahsulotlar")  

class Tarqatish(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_to_tarqatish')
    mahsulot_nomi = models.ForeignKey(Mahsulot, models.CASCADE, related_name='mahsulot_to_tarqatish')
    mahsulot_soni = models.FloatField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_to_tarqatish')
    tarqatgan_vaqti = models.DateField(auto_now=True)
    bitta_mahsulot_narxi = models.FloatField()

    def __str__(self):
        return self.client.name
    
    class Meta:
        verbose_name = ("Tarqatish")
        verbose_name_plural = ("Tarqatishlar")  

from django.db import models

class Skladnik(models.Model):
    nazwa = models.CharField(max_length=20)
    #ilosc = models.DecimalField(decimal_places=2, default=1,max_digits=3)
    #jednostka_miary = models.CharField(choices=[("SZT","szt."),("KG","kg"),("G","g"),("ML","ml.")], default="SZT.",max_length=40)
    #test zmian = tess 
class PozycjaMenu(models.Model):
    nazwa = models.CharField(max_length=40)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    data_edytowania = models.DateTimeField(auto_now=True)
    cena = models.DecimalField(default=0, decimal_places=2,max_digits=3)
    skladniki = models.ManyToManyField(Skladnik)




from django.contrib import admin
from .models import Pneumatiky,Vozidlo,Zakaznik,ZakaznikVozidloRelation,TypServis,TypVozidla,TypZakaznik,Sklad,ServisPracovnik,ServisZaznam

admin.site.register(Pneumatiky)
admin.site.register(Vozidlo)
admin.site.register(Zakaznik)
admin.site.register(ZakaznikVozidloRelation)
admin.site.register(TypServis)
admin.site.register(TypVozidla)
admin.site.register(TypZakaznik)
admin.site.register(Sklad)
admin.site.register(ServisPracovnik)
admin.site.register(ServisZaznam)


# Register your models here.

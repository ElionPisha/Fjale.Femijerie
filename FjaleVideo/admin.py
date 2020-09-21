from django.contrib import admin
from .models import Poezi, Prozeperralla, Tregimedhenovela, Romane, Dramatizimperralla, Dramatizimtregime, Dramatizimfilmavizatimore, Dramatizimedrama, Krijimeabetare, Krijimelirimi

# Register your models here.

# Poezi
admin.site.register(Poezi)

#Proze
admin.site.register(Prozeperralla)
admin.site.register(Tregimedhenovela)
admin.site.register(Romane)

#Dramatizim
admin.site.register(Dramatizimperralla)
admin.site.register(Dramatizimtregime)
admin.site.register(Dramatizimfilmavizatimore)
admin.site.register(Dramatizimedrama)   

#  Krijime
admin.site.register(Krijimeabetare)
admin.site.register(Krijimelirimi)
 


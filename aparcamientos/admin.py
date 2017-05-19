from django.contrib import admin

# Register your models here.

from aparcamientos.models import Aparcamiento
from aparcamientos.models import Comentario
from aparcamientos.models import Preferencia
from aparcamientos.models import Seleccione

admin.site.register(Aparcamiento)
admin.site.register(Comentario)
admin.site.register(Preferencia)
admin.site.register(Seleccione)

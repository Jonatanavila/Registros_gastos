from django.contrib import admin

from .models import Categoria
from .models import Gasto
admin.site.register(Categoria)
admin.site.register(Gasto)

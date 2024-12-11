from django.contrib import admin
from .models import Advogado, Caso

@admin.register(Advogado)
class AdvogadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

@admin.register(Caso)
class CasoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_abertura', 'advogado')

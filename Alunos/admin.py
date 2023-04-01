from django.contrib import admin
from .models import Alunos

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular', 'cidade')  # Adiciona as colunas 'nome', 'email', 'celular' e 'cidade' na lista de exibição
    list_filter = ['sala']  # Adiciona 'cidade' na lista de filtros

admin.site.register(Alunos, AlunosAdmin)
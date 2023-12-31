from django.contrib import admin
from .models import Aluno,Cidade,Curso

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display=('nome_aluno','endereco','email')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display=('nome_curso',)

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display=('nome_cidade','sigla_estado',)



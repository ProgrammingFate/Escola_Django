from django.contrib import admin
from .models import Avaliacao, Nota, Frequencia

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turma_disciplina', 'tipo', 'bimestre', 'data', 'peso')
    list_filter = ('tipo', 'bimestre', 'data')
    search_fields = ('nome', 'turma_disciplina__disciplina__nome', 'turma_disciplina__turma__nome')
    date_hierarchy = 'data'

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'avaliacao', 'valor', 'data_lancamento')
    list_filter = ('avaliacao__bimestre', 'avaliacao__turma_disciplina__disciplina')
    search_fields = ('aluno__first_name', 'aluno__last_name', 'avaliacao__nome')
    date_hierarchy = 'data_lancamento'

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'turma_disciplina', 'data', 'presente')
    list_filter = ('presente', 'data', 'turma_disciplina__disciplina')
    search_fields = ('aluno__first_name', 'aluno__last_name')
    date_hierarchy = 'data'

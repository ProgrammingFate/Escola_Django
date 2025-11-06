from django.contrib import admin
from .models import Turma, Disciplina, TurmaDisciplina

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'serie', 'turno', 'ano_letivo', 'total_alunos')
    list_filter = ('serie', 'turno', 'ano_letivo')
    search_fields = ('nome',)
    filter_horizontal = ('alunos',)
    
    def total_alunos(self, obj):
        return obj.alunos.count()
    total_alunos.short_description = 'Total de Alunos'

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria', 'cor')
    search_fields = ('nome',)

@admin.register(TurmaDisciplina)
class TurmaDisciplinaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'disciplina', 'professor')
    list_filter = ('turma__serie', 'disciplina')
    search_fields = ('turma__nome', 'disciplina__nome', 'professor__first_name', 'professor__last_name')

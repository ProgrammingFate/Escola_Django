from django.urls import path
from . import views

urlpatterns = [
    path('minhas-notas/', views.minhas_notas, name='minhas_notas'),
    path('lancar-notas/<int:turma_disciplina_id>/', views.lancar_notas, name='lancar_notas'),
    path('frequencia/', views.frequencia_aluno, name='frequencia_aluno'),
]

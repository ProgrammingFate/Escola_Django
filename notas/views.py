from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from .models import Nota, Avaliacao, Frequencia
from escola.models import TurmaDisciplina

@login_required
def minhas_notas(request):
    """Visualizar notas do aluno logado"""
    if request.user.perfil.tipo != 'aluno':
        messages.error(request, 'Acesso permitido apenas para alunos.')
        return redirect('dashboard')
    
    notas = Nota.objects.filter(aluno=request.user).select_related('avaliacao__turma_disciplina__disciplina')
    
    # Agrupar por bimestre e disciplina
    notas_por_bimestre = {}
    for bim in range(1, 5):
        notas_bim = notas.filter(avaliacao__bimestre=bim)
        notas_por_bimestre[bim] = notas_bim
    
    context = {
        'notas_por_bimestre': notas_por_bimestre,
    }
    return render(request, 'notas/minhas_notas.html', context)

@login_required
def lancar_notas(request, turma_disciplina_id):
    """Lançar notas (apenas professores)"""
    if request.user.perfil.tipo != 'professor':
        messages.error(request, 'Acesso permitido apenas para professores.')
        return redirect('dashboard')
    
    turma_disciplina = get_object_or_404(TurmaDisciplina, pk=turma_disciplina_id, professor=request.user)
    avaliacoes = Avaliacao.objects.filter(turma_disciplina=turma_disciplina)
    alunos = turma_disciplina.turma.alunos.all()
    
    context = {
        'turma_disciplina': turma_disciplina,
        'avaliacoes': avaliacoes,
        'alunos': alunos,
    }
    return render(request, 'notas/lancar_notas.html', context)

@login_required
def frequencia_aluno(request):
    """Visualizar frequência do aluno"""
    if request.user.perfil.tipo != 'aluno':
        messages.error(request, 'Acesso permitido apenas para alunos.')
        return redirect('dashboard')
    
    frequencias = Frequencia.objects.filter(aluno=request.user).select_related('turma_disciplina__disciplina')
    
    context = {
        'frequencias': frequencias,
    }
    return render(request, 'notas/frequencia_aluno.html', context)

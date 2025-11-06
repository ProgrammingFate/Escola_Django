from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Turma, Disciplina, TurmaDisciplina

def home(request):
    """Página inicial do sistema"""
    return render(request, 'escola/home.html')

@login_required
def dashboard(request):
    """Dashboard principal - redireciona baseado no tipo de usuário"""
    user_tipo = request.user.perfil.tipo
    
    if user_tipo == 'aluno':
        return dashboard_aluno(request)
    elif user_tipo == 'professor':
        return dashboard_professor(request)
    else:
        return dashboard_admin(request)

@login_required
def dashboard_aluno(request):
    """Dashboard do aluno"""
    turmas = request.user.turmas_aluno.all()
    context = {
        'turmas': turmas,
    }
    return render(request, 'escola/dashboard_aluno.html', context)

@login_required
def dashboard_professor(request):
    """Dashboard do professor"""
    disciplinas = TurmaDisciplina.objects.filter(professor=request.user)
    context = {
        'disciplinas': disciplinas,
    }
    return render(request, 'escola/dashboard_professor.html', context)

@login_required
def dashboard_admin(request):
    """Dashboard do administrador"""
    total_alunos = Turma.objects.values_list('alunos', flat=True).distinct().count()
    total_professores = TurmaDisciplina.objects.values_list('professor', flat=True).distinct().count()
    total_turmas = Turma.objects.count()
    total_disciplinas = Disciplina.objects.count()
    
    context = {
        'total_alunos': total_alunos,
        'total_professores': total_professores,
        'total_turmas': total_turmas,
        'total_disciplinas': total_disciplinas,
    }
    return render(request, 'escola/dashboard_admin.html', context)

@login_required
def turma_detalhe(request, pk):
    """Detalhes de uma turma"""
    turma = get_object_or_404(Turma, pk=pk)
    disciplinas = turma.disciplinas.all()
    
    context = {
        'turma': turma,
        'disciplinas': disciplinas,
    }
    return render(request, 'escola/turma_detalhe.html', context)

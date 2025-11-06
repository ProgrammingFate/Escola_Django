from django.db import models
from django.contrib.auth.models import User

class Turma(models.Model):
    SERIE_CHOICES = (
        ('6ano', '6º Ano'),
        ('7ano', '7º Ano'),
        ('8ano', '8º Ano'),
        ('9ano', '9º Ano'),
        ('1em', '1º Ano EM'),
        ('2em', '2º Ano EM'),
        ('3em', '3º Ano EM'),
    )
    
    nome = models.CharField(max_length=100)
    serie = models.CharField(max_length=10, choices=SERIE_CHOICES)
    ano_letivo = models.IntegerField(default=2025)
    turno = models.CharField(max_length=20, choices=(
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('noturno', 'Noturno'),
    ))
    alunos = models.ManyToManyField(User, related_name='turmas_aluno', blank=True, limit_choices_to={'perfil__tipo': 'aluno'})
    
    def __str__(self):
        return f"{self.nome} - {self.get_serie_display()} ({self.ano_letivo})"
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['serie', 'nome']

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    carga_horaria = models.IntegerField(help_text="Carga horária semanal")
    cor = models.CharField(max_length=7, default='#007bff', help_text="Cor em hexadecimal")
    icone = models.CharField(max_length=50, blank=True, help_text="Nome do ícone FontAwesome")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['nome']

class TurmaDisciplina(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='disciplinas')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='disciplinas_lecionadas', limit_choices_to={'perfil__tipo': 'professor'})
    
    def __str__(self):
        return f"{self.disciplina.nome} - {self.turma.nome} - Prof. {self.professor.get_full_name() if self.professor else 'Sem professor'}"
    
    class Meta:
        verbose_name = 'Disciplina da Turma'
        verbose_name_plural = 'Disciplinas das Turmas'
        unique_together = ['turma', 'disciplina']

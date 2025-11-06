from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from escola.models import TurmaDisciplina

class Avaliacao(models.Model):
    TIPO_CHOICES = (
        ('prova', 'Prova'),
        ('trabalho', 'Trabalho'),
        ('atividade', 'Atividade'),
        ('participacao', 'Participação'),
    )
    
    turma_disciplina = models.ForeignKey(TurmaDisciplina, on_delete=models.CASCADE, related_name='avaliacoes')
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    data = models.DateField()
    peso = models.DecimalField(max_digits=3, decimal_places=1, default=1.0, validators=[MinValueValidator(0.1)])
    bimestre = models.IntegerField(choices=[(1, '1º Bimestre'), (2, '2º Bimestre'), (3, '3º Bimestre'), (4, '4º Bimestre')])
    
    def __str__(self):
        return f"{self.nome} - {self.turma_disciplina.disciplina.nome} ({self.bimestre}º Bim)"
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-data']

class Nota(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='notas')
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notas', limit_choices_to={'perfil__tipo': 'aluno'})
    valor = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(10)])
    observacao = models.TextField(blank=True)
    data_lancamento = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.aluno.get_full_name()} - {self.avaliacao.nome}: {self.valor}"
    
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        unique_together = ['avaliacao', 'aluno']
        ordering = ['-data_lancamento']

class Frequencia(models.Model):
    turma_disciplina = models.ForeignKey(TurmaDisciplina, on_delete=models.CASCADE, related_name='frequencias')
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='frequencias', limit_choices_to={'perfil__tipo': 'aluno'})
    data = models.DateField()
    presente = models.BooleanField(default=True)
    justificativa = models.TextField(blank=True)
    
    def __str__(self):
        status = "Presente" if self.presente else "Ausente"
        return f"{self.aluno.get_full_name()} - {self.turma_disciplina.disciplina.nome} ({self.data}): {status}"
    
    class Meta:
        verbose_name = 'Frequência'
        verbose_name_plural = 'Frequências'
        unique_together = ['turma_disciplina', 'aluno', 'data']
        ordering = ['-data']

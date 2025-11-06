from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from escola.models import Turma, Disciplina, TurmaDisciplina
from notas.models import Avaliacao, Nota, Frequencia
from usuarios.models import Perfil
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de exemplo'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populando banco de dados...')
        
        # Criar superusuário admin
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@escola.com',
                password='admin123',
                first_name='Administrador',
                last_name='Sistema'
            )
            admin.perfil.tipo = 'admin'
            admin.perfil.save()
            self.stdout.write(self.style.SUCCESS('✓ Superusuário criado: admin/admin123'))
        
        # Criar professores
        professores_data = [
            ('prof.joao', 'João', 'Silva', 'joao@escola.com'),
            ('prof.maria', 'Maria', 'Santos', 'maria@escola.com'),
            ('prof.carlos', 'Carlos', 'Oliveira', 'carlos@escola.com'),
            ('prof.ana', 'Ana', 'Costa', 'ana@escola.com'),
            ('prof.pedro', 'Pedro', 'Souza', 'pedro@escola.com'),
        ]
        
        professores = []
        for username, first_name, last_name, email in professores_data:
            if not User.objects.filter(username=username).exists():
                prof = User.objects.create_user(
                    username=username,
                    password='senha123',
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                prof.perfil.tipo = 'professor'
                prof.perfil.save()
                professores.append(prof)
                self.stdout.write(self.style.SUCCESS(f'✓ Professor criado: {username}/senha123'))
            else:
                professores.append(User.objects.get(username=username))
        
        # Criar alunos
        alunos_nomes = [
            ('Lucas', 'Pereira'), ('Julia', 'Almeida'), ('Rafael', 'Rodrigues'),
            ('Beatriz', 'Fernandes'), ('Gabriel', 'Martins'), ('Larissa', 'Carvalho'),
            ('Felipe', 'Ribeiro'), ('Amanda', 'Barbosa'), ('Thiago', 'Gomes'),
            ('Camila', 'Dias'), ('Bruno', 'Araújo'), ('Isabela', 'Cardoso'),
            ('Mateus', 'Freitas'), ('Letícia', 'Monteiro'), ('Vinicius', 'Rocha'),
        ]
        
        alunos = []
        for idx, (first_name, last_name) in enumerate(alunos_nomes, 1):
            username = f'aluno{idx}'
            if not User.objects.filter(username=username).exists():
                aluno = User.objects.create_user(
                    username=username,
                    password='senha123',
                    first_name=first_name,
                    last_name=last_name,
                    email=f'{username}@escola.com'
                )
                aluno.perfil.tipo = 'aluno'
                aluno.perfil.save()
                alunos.append(aluno)
                self.stdout.write(self.style.SUCCESS(f'✓ Aluno criado: {username}/senha123'))
            else:
                alunos.append(User.objects.get(username=username))
        
        # Criar disciplinas
        disciplinas_data = [
            ('Matemática', 'Estudo de números, operações e geometria', 5, '#3b82f6', 'calculator'),
            ('Português', 'Língua Portuguesa e Literatura', 5, '#ef4444', 'book'),
            ('História', 'História do Brasil e do Mundo', 3, '#f59e0b', 'landmark'),
            ('Geografia', 'Geografia Física e Humana', 3, '#10b981', 'globe'),
            ('Ciências', 'Ciências Naturais', 4, '#8b5cf6', 'flask'),
            ('Inglês', 'Língua Inglesa', 2, '#06b6d4', 'language'),
            ('Educação Física', 'Atividades Físicas e Esportivas', 2, '#f97316', 'running'),
            ('Arte', 'Artes Visuais e Música', 2, '#ec4899', 'palette'),
        ]
        
        disciplinas = []
        for nome, desc, carga, cor, icone in disciplinas_data:
            disc, created = Disciplina.objects.get_or_create(
                nome=nome,
                defaults={
                    'descricao': desc,
                    'carga_horaria': carga,
                    'cor': cor,
                    'icone': icone
                }
            )
            disciplinas.append(disc)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Disciplina criada: {nome}'))
        
        # Criar turmas
        turmas_data = [
            ('7º A', '7ano', 'matutino'),
            ('7º B', '7ano', 'vespertino'),
            ('8º A', '8ano', 'matutino'),
            ('9º A', '9ano', 'matutino'),
        ]
        
        turmas = []
        for nome, serie, turno in turmas_data:
            turma, created = Turma.objects.get_or_create(
                nome=nome,
                defaults={
                    'serie': serie,
                    'ano_letivo': 2025,
                    'turno': turno
                }
            )
            
            # Adicionar alunos às turmas (dividir alunos entre turmas)
            alunos_por_turma = len(alunos) // len(turmas_data)
            inicio = len(turmas) * alunos_por_turma
            fim = inicio + alunos_por_turma
            turma.alunos.set(alunos[inicio:fim])
            
            turmas.append(turma)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Turma criada: {nome}'))
        
        # Atribuir disciplinas às turmas com professores
        for turma in turmas:
            for idx, disciplina in enumerate(disciplinas):
                professor = professores[idx % len(professores)]
                td, created = TurmaDisciplina.objects.get_or_create(
                    turma=turma,
                    disciplina=disciplina,
                    defaults={'professor': professor}
                )
                if created:
                    self.stdout.write(f'  → {disciplina.nome} atribuída ao Prof. {professor.get_full_name()}')
        
        # Criar algumas avaliações e notas de exemplo
        self.stdout.write('\nCriando avaliações e notas...')
        for turma in turmas[:2]:  # Apenas para as 2 primeiras turmas
            turma_discs = TurmaDisciplina.objects.filter(turma=turma)[:3]  # 3 disciplinas
            
            for td in turma_discs:
                # Criar avaliações para o 1º bimestre
                for i in range(2):  # 2 avaliações por disciplina
                    avaliacao, created = Avaliacao.objects.get_or_create(
                        turma_disciplina=td,
                        nome=f'Prova {i+1}' if i == 0 else 'Trabalho 1',
                        defaults={
                            'tipo': 'prova' if i == 0 else 'trabalho',
                            'data': date.today() - timedelta(days=30-i*10),
                            'peso': 2.0 if i == 0 else 1.0,
                            'bimestre': 1,
                            'descricao': f'Avaliação de {td.disciplina.nome}'
                        }
                    )
                    
                    if created:
                        # Criar notas para cada aluno da turma
                        for aluno in turma.alunos.all():
                            nota_valor = round(random.uniform(5.0, 10.0), 2)
                            Nota.objects.get_or_create(
                                avaliacao=avaliacao,
                                aluno=aluno,
                                defaults={'valor': nota_valor}
                            )
        
        self.stdout.write(self.style.SUCCESS('\n✅ Banco de dados populado com sucesso!'))
        self.stdout.write('\n📚 CREDENCIAIS DE ACESSO:')
        self.stdout.write('━' * 50)
        self.stdout.write('👤 ADMIN:      admin / admin123')
        self.stdout.write('👨‍🏫 PROFESSOR:  prof.joao / senha123')
        self.stdout.write('🎓 ALUNO:      aluno1 / senha123')
        self.stdout.write('━' * 50)

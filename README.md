# 🎓 Sistema Escolar Django

Sistema completo de gestão escolar desenvolvido com Django, incluindo sistema de login diferenciado para professores e alunos, gerenciamento de notas, frequência e muito mais!

## 🚀 Características

### Para Alunos
- ✅ Visualizar notas por bimestre e disciplina
- ✅ Acompanhar frequência nas aulas
- ✅ Dashboard personalizado
- ✅ Perfil com foto e informações pessoais

### Para Professores
- ✅ Lançar notas e avaliações
- ✅ Gerenciar turmas e disciplinas
- ✅ Controlar frequência dos alunos
- ✅ Dashboard com visão geral das disciplinas

### Para Administradores
- ✅ Painel administrativo completo
- ✅ Gestão de usuários, turmas e disciplinas
- ✅ Relatórios e estatísticas
- ✅ Controle total do sistema

## 🎨 Design

- Interface moderna e responsiva com Bootstrap 5
- Gradientes e animações suaves
- Ícones Font Awesome
- Cores vibrantes e chamativas
- Design inspirado em sites educacionais brasileiros

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Virtualenv (recomendado)

## 🛠️ Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/ProgrammingFate/Escola_Django.git
cd Escola_Django
```

2. **Crie e ative o ambiente virtual:**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows
```

3. **Instale as dependências:**
```bash
pip install django pillow django-crispy-forms crispy-bootstrap5
```

4. **Execute as migrações:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Popule o banco de dados com dados de exemplo:**
```bash
python manage.py popular_db
```

6. **Inicie o servidor:**
```bash
python manage.py runserver
```

7. **Acesse o sistema:**
```
http://localhost:8000
```

## 🔐 Credenciais de Acesso

### Administrador
- **Usuário:** admin
- **Senha:** admin123

### Professor
- **Usuário:** prof.joao
- **Senha:** senha123

### Aluno
- **Usuário:** aluno1
- **Senha:** senha123

## 📁 Estrutura do Projeto

```
Escola_Django/
├── escola/                 # App principal (turmas, disciplinas)
│   ├── models.py          # Modelos Turma, Disciplina, TurmaDisciplina
│   ├── views.py           # Views e dashboards
│   └── admin.py           # Configuração do admin
├── usuarios/              # App de usuários e perfis
│   ├── models.py          # Modelo Perfil
│   ├── forms.py           # Formulários de registro e perfil
│   └── views.py           # Views de autenticação
├── notas/                 # App de notas e frequência
│   ├── models.py          # Modelos Nota, Avaliacao, Frequencia
│   ├── views.py           # Views de notas
│   └── admin.py           # Admin de notas
├── templates/             # Templates HTML
│   ├── base.html          # Template base
│   ├── escola/            # Templates da escola
│   ├── usuarios/          # Templates de usuários
│   └── notas/             # Templates de notas
├── static/                # Arquivos estáticos (CSS, JS, imagens)
└── media/                 # Arquivos de upload (fotos de perfil)
```

## 🎯 Funcionalidades Principais

### Sistema de Autenticação
- Login diferenciado por tipo de usuário (aluno, professor, admin)
- Registro de novos usuários
- Perfis personalizados com foto

### Gestão Acadêmica
- Cadastro de turmas e disciplinas
- Atribuição de professores às disciplinas
- Matrícula de alunos em turmas

### Sistema de Notas
- Criação de avaliações (provas, trabalhos, atividades)
- Lançamento de notas por bimestre
- Visualização do boletim completo

### Controle de Frequência
- Registro de presença/ausência
- Justificativas de faltas
- Relatório de frequência

## 🎨 Tecnologias Utilizadas

- **Backend:** Django 5.2
- **Frontend:** Bootstrap 5, Font Awesome, Google Fonts
- **Banco de Dados:** SQLite (desenvolvimento)
- **Forms:** Django Crispy Forms com Bootstrap 5
- **Upload de Imagens:** Pillow

## 📊 Modelos de Dados

### Perfil
- Tipo de usuário (aluno, professor, admin)
- Foto de perfil
- Dados pessoais (telefone, CPF, endereço, data de nascimento)

### Turma
- Nome, série, turno
- Ano letivo
- Alunos matriculados

### Disciplina
- Nome, descrição
- Carga horária
- Cor e ícone personalizados

### Avaliação
- Nome, tipo (prova, trabalho, etc.)
- Data, peso, bimestre
- Disciplina e turma

### Nota
- Aluno, avaliação
- Valor (0 a 10)
- Observações

### Frequência
- Aluno, disciplina, data
- Presente/ausente
- Justificativa

## 🔧 Comandos Úteis

### Criar superusuário
```bash
python manage.py createsuperuser
```

### Coletar arquivos estáticos
```bash
python manage.py collectstatic
```

### Limpar banco e repopular
```bash
rm db.sqlite3
python manage.py migrate
python manage.py popular_db
```

## 📝 Próximas Funcionalidades

- [ ] Sistema de mensagens entre professores e alunos
- [ ] Calendário de provas e eventos
- [ ] Geração de PDF para boletins
- [ ] Gráficos de desempenho
- [ ] Sistema de notificações
- [ ] API REST para integração mobile

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto é open source e está disponível sob a licença MIT.

## 👨‍💻 Desenvolvedor

Sistema desenvolvido para demonstração de conceitos de Django e desenvolvimento web.

---

**Desenvolvido com ❤️ e Django**

# 🎯 GUIA RÁPIDO DE USO

## 🚀 Como Iniciar

1. **Iniciar o servidor:**
```bash
python manage.py runserver
```

2. **Acessar o sistema:**
```
http://localhost:8000
```

## 🔐 CREDENCIAIS PARA TESTE

### 👤 Administrador
- Usuário: **admin**
- Senha: **admin123**
- Acesso: Painel administrativo completo

### 👨‍🏫 Professor  
- Usuário: **prof.joao** (ou prof.maria, prof.carlos, prof.ana, prof.pedro)
- Senha: **senha123**
- Acesso: Dashboard do professor, lançamento de notas

### 🎓 Aluno
- Usuário: **aluno1** (até aluno15)
- Senha: **senha123**
- Acesso: Visualizar notas e frequência

## 📱 NAVEGAÇÃO DO SISTEMA

### Página Inicial (/)
- Apresentação do sistema
- Informações sobre funcionalidades
- Links para login e registro

### Dashboard (/dashboard/)
- **Alunos:** Ver turmas, atalhos para notas e frequência
- **Professores:** Ver disciplinas que leciona, lançar notas
- **Admin:** Estatísticas gerais, acesso rápido ao painel

### Minhas Notas (/notas/minhas-notas/)
- Visualização de notas por bimestre
- Notas coloridas por desempenho (verde≥7, amarelo≥5, vermelho<5)

### Frequência (/notas/frequencia/)
- Lista de presenças e ausências
- Filtrado por disciplina

### Perfil (/usuarios/perfil/)
- Editar dados pessoais
- Upload de foto de perfil
- Atualizar informações de contato

### Admin (/admin/)
- Gestão completa de:
  - Usuários e perfis
  - Turmas e disciplinas
  - Notas e avaliações
  - Frequência

## 🎨 RECURSOS VISUAIS

### Design Moderno
- ✨ Gradientes coloridos
- 🎯 Ícones Font Awesome
- 📱 Totalmente responsivo
- 🌈 Cores vibrantes por disciplina

### Elementos Interativos
- Cards com hover effect
- Botões com animações
- Badges coloridos para notas
- Alertas estilizados

## 📊 FLUXO DE TRABALHO

### Para Administradores:
1. Login no sistema
2. Acesso ao painel admin (/admin/)
3. Criar turmas, disciplinas e usuários
4. Atribuir professores às disciplinas
5. Matricular alunos nas turmas

### Para Professores:
1. Login no sistema
2. Ver disciplinas no dashboard
3. Criar avaliações pelo admin
4. Lançar notas dos alunos
5. Registrar frequência

### Para Alunos:
1. Login no sistema
2. Ver turmas no dashboard
3. Consultar notas por bimestre
4. Verificar frequência
5. Atualizar perfil

## 🔧 PERSONALIZAÇÕES

### Adicionar Nova Disciplina
1. Acesse /admin/escola/disciplina/
2. Clique em "Adicionar disciplina"
3. Preencha nome, descrição, carga horária
4. Escolha uma cor (hex) e ícone (Font Awesome)

### Criar Avaliação
1. Acesse /admin/notas/avaliacao/
2. Clique em "Adicionar avaliação"
3. Selecione turma/disciplina
4. Defina tipo, data, peso e bimestre

### Lançar Nota
1. Acesse /admin/notas/nota/
2. Clique em "Adicionar nota"
3. Selecione avaliação e aluno
4. Insira o valor (0 a 10)

## 🎯 DICAS

✅ Use o comando `python manage.py popular_db` para resetar dados de exemplo

✅ Cores das disciplinas podem ser personalizadas em hexadecimal (#RRGGBB)

✅ Ícones disponíveis em: https://fontawesome.com/icons

✅ Upload de fotos aceita JPG, PNG, GIF

✅ Notas devem estar entre 0 e 10

✅ Cada tipo de usuário vê um dashboard diferente

## 🆘 PROBLEMAS COMUNS

### Erro ao fazer upload de foto
- Certifique-se que a pasta `media/perfis/` existe
- Verifique se o Pillow está instalado: `pip install pillow`

### Página não encontrada (404)
- Verifique se o servidor está rodando
- Confirme a URL correta

### Erro de permissão
- Verifique se está logado
- Confirme o tipo de usuário (aluno/professor/admin)

### Banco de dados vazio
- Execute: `python manage.py popular_db`

## 📞 SUPORTE

Para mais informações, consulte o README.md principal do projeto.

---

**Sistema pronto para uso! 🚀**

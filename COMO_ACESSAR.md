# 🚀 ACESSE O SISTEMA AGORA!

## ✅ Sistema está rodando!

O servidor Django está ativo e pronto para uso.

## 🌐 Como Acessar

### 1. Abra seu navegador web

### 2. Digite um dos seguintes endereços:

```
http://localhost:8000
```
ou
```
http://127.0.0.1:8000
```

## 🔐 Faça Login com:

### 👤 ADMINISTRADOR
```
Usuário: admin
Senha: admin123
```
**Acesso a:** Tudo! Painel admin, gestão completa do sistema

---

### 👨‍🏫 PROFESSOR
```
Usuário: prof.joao
Senha: senha123
```
**Outros professores:** prof.maria, prof.carlos, prof.ana, prof.pedro

**Acesso a:** Dashboard professor, lançar notas, ver turmas

---

### 🎓 ALUNO
```
Usuário: aluno1
Senha: senha123
```
**Outros alunos:** aluno2, aluno3... até aluno15

**Acesso a:** Ver notas, frequência, turmas

---

## 📱 Páginas Principais

### Página Inicial
```
http://localhost:8000/
```
Interface atraente com apresentação do sistema

### Dashboard
```
http://localhost:8000/dashboard/
```
Dashboard personalizado conforme tipo de usuário

### Minhas Notas (Aluno)
```
http://localhost:8000/notas/minhas-notas/
```
Boletim completo por bimestre

### Frequência (Aluno)
```
http://localhost:8000/notas/frequencia/
```
Histórico de presenças e ausências

### Perfil
```
http://localhost:8000/usuarios/perfil/
```
Editar informações pessoais e foto

### Painel Admin
```
http://localhost:8000/admin/
```
Gestão completa (apenas admin)

---

## 🎯 Passo a Passo Recomendado

### 1. TESTE COMO ALUNO
1. Acesse: `http://localhost:8000`
2. Clique em **"Entrar"**
3. Login: `aluno1` / Senha: `senha123`
4. Explore o dashboard do aluno
5. Veja suas notas em **"Minhas Notas"**
6. Confira a frequência
7. Edite seu perfil

### 2. TESTE COMO PROFESSOR
1. Faça logout
2. Login: `prof.joao` / Senha: `senha123`
3. Veja as disciplinas que leciona
4. Clique em **"Lançar Notas"**
5. Veja as turmas e alunos

### 3. TESTE COMO ADMIN
1. Faça logout
2. Login: `admin` / Senha: `admin123`
3. Veja as estatísticas no dashboard
4. Acesse o painel admin em `/admin/`
5. Explore a gestão de:
   - Usuários
   - Turmas
   - Disciplinas
   - Notas
   - Avaliações
   - Frequência

---

## 🛑 Para Parar o Servidor

Pressione `Ctrl + C` no terminal onde o servidor está rodando

## ▶️ Para Reiniciar o Servidor

```bash
python manage.py runserver
```

---

## 💡 Dicas Importantes

### ✅ O sistema já vem com dados de exemplo!
- 15 alunos cadastrados
- 5 professores
- 4 turmas
- 8 disciplinas
- Notas e avaliações de exemplo

### ✅ Você pode:
- Criar novos usuários
- Adicionar turmas e disciplinas
- Lançar novas notas
- Registrar frequência
- Upload de fotos de perfil

### ✅ Painel Admin é poderoso!
Use-o para:
- Gerenciar todos os dados
- Criar avaliações
- Atribuir professores
- Matricular alunos

---

## 🎨 Recursos Visuais

O sistema conta com:
- 🌈 **Design moderno** com gradientes coloridos
- 📱 **Totalmente responsivo** (funciona em celular)
- ⚡ **Animações suaves** em hover
- 🎯 **Badges coloridos** para notas
- 📊 **Ícones intuitivos** Font Awesome
- 🖼️ **Upload de fotos** de perfil

---

## 📚 Documentação

Consulte os seguintes arquivos para mais informações:

- **README.md** - Documentação completa
- **GUIA_USO.md** - Guia detalhado de uso
- **RESUMO_PROJETO.md** - Resumo do que foi desenvolvido
- **DESIGN_SISTEMA.md** - Informações sobre o design

---

## 🆘 Problemas?

### Servidor não inicia?
```bash
cd /home/lucas-dev/Desktop/projects/Escola_Django
python manage.py runserver
```

### Página não carrega?
- Verifique se o servidor está rodando
- Confirme o endereço: `http://localhost:8000`
- Tente outro navegador

### Erro ao fazer login?
- Verifique as credenciais
- Use: `admin/admin123` ou `aluno1/senha123`

### Quer resetar os dados?
```bash
rm db.sqlite3
python manage.py migrate
python manage.py popular_db
```

---

## 🎓 APROVEITE O SISTEMA!

O **Sistema Escolar** está completo e funcional!

Explore todas as funcionalidades e veja como um sistema educacional
moderno e profissional funciona.

**Bons estudos e boa gestão! 📚✨**

---

🌐 **ACESSE AGORA:** http://localhost:8000

---

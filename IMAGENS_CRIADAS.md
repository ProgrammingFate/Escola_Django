# 🎨 Imagens Criadas para o Sistema Escolar

## ✅ Imagens Geradas Automaticamente

Foram criadas **10 imagens** modernas para dar vida ao sistema:

### 📸 Imagens Principais

1. **`banner_home.jpg`** (1920x800px)
   - Banner principal da página inicial
   - Design moderno com elementos geométricos
   - Cores: Azul (#0ea5e9) e Roxo (#8b5cf6)
   - Local: Hero section da home

2. **`quadra_esportes.jpg`** (1200x600px)
   - Imagem representando esportes e atividades
   - Ícone: 🏀
   - Cor principal: Azul
   - Uso: Galeria da home

3. **`estudantes.jpg`** (1200x600px)
   - Representa aprendizado moderno
   - Ícone: 📚
   - Cor principal: Verde (#10b981)
   - Uso: Galeria da home

4. **`tecnologia.jpg`** (1200x600px)
   - Tecnologia e inovação
   - Ícone: 💻
   - Cor principal: Roxo (#8b5cf6)
   - Uso: Galeria da home

5. **`biblioteca.jpg`** (1200x600px)
   - Biblioteca digital
   - Ícone: 📖
   - Cor principal: Laranja (#f59e0b)
   - Uso: Galeria da home

### 🎯 Cards de Atividades (600x600px cada)

6. **`card_esportes.jpg`**
   - Ícone: 🏃
   - Cor: Azul (#0ea5e9)
   
7. **`card_artes.jpg`**
   - Ícone: 🎨
   - Cor: Roxo (#8b5cf6)
   
8. **`card_ciencias.jpg`**
   - Ícone: 🔬
   - Cor: Verde (#10b981)
   
9. **`card_musica.jpg`**
   - Ícone: 🎵
   - Cor: Laranja (#f59e0b)

### 👤 Perfil

10. **`default.jpg`** (400x400px)
    - Imagem padrão de perfil
    - Ícone de usuário estilizado
    - Fundo azul circular
    - Usado quando usuário não tem foto

## 📁 Estrutura de Pastas

```
media/
├── escola/          # Imagens do sistema
│   ├── banner_home.jpg
│   ├── quadra_esportes.jpg
│   ├── estudantes.jpg
│   ├── tecnologia.jpg
│   ├── biblioteca.jpg
│   ├── card_esportes.jpg
│   ├── card_artes.jpg
│   ├── card_ciencias.jpg
│   └── card_musica.jpg
└── perfis/          # Fotos de perfil
    └── default.jpg
```

## 🎨 Características das Imagens

- **Design Moderno**: Elementos geométricos e gradientes
- **Cores Consistentes**: Paleta do sistema (azul, verde, roxo, laranja)
- **Alta Qualidade**: Salvas em JPEG com 95% de qualidade
- **Otimizadas**: Tamanhos adequados para web
- **Responsivas**: Funcionam bem em diferentes telas

## 🚀 Onde São Usadas

### Home Page (`/`)
- Banner no hero section
- Galeria de 4 imagens grandes
- 4 cards de atividades extracurriculares

### Perfis de Usuário
- Imagem default quando não há foto personalizada
- Dashboards de alunos, professores e admin

## 💡 Como Substituir por Imagens Reais

Se você quiser usar imagens reais (fotos da sua escola), siga estes passos:

1. **Tire fotos** ou use imagens de IA de:
   - Quadra de esportes
   - Alunos estudando
   - Laboratórios/tecnologia
   - Biblioteca

2. **Dimensões recomendadas**:
   - Banner: 1920x800px
   - Galeria: 1200x600px
   - Cards: 600x600px
   - Perfil: 400x400px (quadrado)

3. **Substitua** os arquivos em `media/escola/` mantendo os mesmos nomes

4. **Otimize** as imagens para web (use ferramentas como TinyPNG)

## 🎯 Recomendações para Fotos com IA

Use esses prompts em ferramentas como **Leonardo.ai**, **Midjourney** ou **DALL-E**:

### Quadra de Esportes
```
Modern school sports court, students playing basketball, 
vibrant blue and green colors, professional photography, 
bright lighting, 4k, ultra detailed, realistic
```

### Estudantes
```
Diverse group of students studying together in modern library,
natural lighting, contemporary design, laptops and books,
warm atmosphere, professional photography, 4k
```

### Tecnologia
```
Modern computer lab, students working on laptops,
high-tech equipment, purple and blue ambient lighting,
futuristic design, professional photography, 4k
```

### Biblioteca
```
Contemporary school library with digital resources,
wooden shelves with books, students reading,
warm orange lighting, cozy atmosphere, 4k
```

## ✨ Efeitos Visuais Aplicados

As imagens têm efeitos especiais no CSS:

- **Hover zoom**: Imagem aumenta 15% ao passar o mouse
- **Parallax suave**: Rotação leve de 2°
- **Shadow dinâmico**: Sombra azul ao hover
- **Transições suaves**: 0.6s de animação
- **Overlay gradiente**: Texto legível sobre imagens

## 🔧 Script de Criação

Para recriar ou modificar as imagens, execute:

```bash
python criar_imagens.py
```

O script usa **Pillow (PIL)** para gerar as imagens programaticamente.

---

**Feito com ❤️ para tornar o sistema escolar mais visual e atrativo!**

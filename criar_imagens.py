"""
Script para criar imagens INCRÍVEIS e MODERNAS para o sistema escolar
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Criar diretórios
os.makedirs('media/perfis', exist_ok=True)
os.makedirs('media/escola', exist_ok=True)

def criar_imagem_perfil_default():
    """Cria uma imagem de perfil padrão moderna"""
    size = 400
    img = Image.new('RGB', (size, size), color='#0f172a')
    draw = ImageDraw.Draw(img)
    
    # Círculo azul de fundo
    circle_margin = 50
    draw.ellipse(
        [circle_margin, circle_margin, size-circle_margin, size-circle_margin],
        fill='#0ea5e9'
    )
    
    # Desenhar ícone de usuário simplificado
    # Cabeça
    head_radius = 60
    head_center = size // 2
    draw.ellipse(
        [head_center-head_radius, 120, head_center+head_radius, 240],
        fill='white'
    )
    
    # Corpo (semicírculo)
    body_width = 140
    body_height = 120
    draw.ellipse(
        [head_center-body_width, 220, head_center+body_width, 220+body_height*2],
        fill='white'
    )
    
    img.save('media/perfis/default.jpg', 'JPEG', quality=95)
    print("✅ Imagem de perfil default criada!")

def criar_imagem_moderna(nome, cor_principal, cor_secundaria, titulo, emoji):
    """Cria imagens modernas e atrativas com gradientes e formas geométricas"""
    width, height = 1200, 800
    
    # Criar imagem base
    img = Image.new('RGB', (width, height), color='#0f172a')
    draw = ImageDraw.Draw(img)
    
    # Criar gradiente de fundo simulado com retângulos
    for i in range(height):
        # Interpolação de cor
        ratio = i / height
        # Converter hex para RGB
        r1, g1, b1 = int(cor_principal[1:3], 16), int(cor_principal[3:5], 16), int(cor_principal[5:7], 16)
        r2, g2, b2 = int(cor_secundaria[1:3], 16), int(cor_secundaria[3:5], 16), int(cor_secundaria[5:7], 16)
        
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        
        draw.rectangle([(0, i), (width, i+1)], fill=(r, g, b))
    
    # Adicionar formas geométricas decorativas
    # Círculos grandes com transparência simulada (mais claros)
    overlay_color = tuple(int(c * 1.2) if int(c * 1.2) < 255 else 255 for c in [r1, g1, b1])
    draw.ellipse([800, -100, 1300, 400], fill=overlay_color, outline=None)
    draw.ellipse([-200, 500, 300, 1000], fill=overlay_color, outline=None)
    
    # Círculos menores
    lighter_color = tuple(int(c * 1.4) if int(c * 1.4) < 255 else 255 for c in [r1, g1, b1])
    draw.ellipse([150, 100, 350, 300], fill=lighter_color, outline=None)
    draw.ellipse([900, 550, 1050, 700], fill=lighter_color, outline=None)
    
    # Adicionar overlay escuro para contraste do texto
    overlay = Image.new('RGBA', (width, height), (15, 23, 42, 180))
    img_rgba = img.convert('RGBA')
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    img = img_rgba.convert('RGB')
    draw = ImageDraw.Draw(img)
    
    try:
        # Fontes
        font_emoji = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 180)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
    except:
        font_emoji = ImageFont.load_default()
        font_title = ImageFont.load_default()
    
    # Desenhar emoji grande centralizado
    emoji_bbox = draw.textbbox((0, 0), emoji, font=font_emoji)
    emoji_width = emoji_bbox[2] - emoji_bbox[0]
    emoji_height = emoji_bbox[3] - emoji_bbox[1]
    emoji_x = (width - emoji_width) // 2
    emoji_y = (height - emoji_height) // 2 - 50
    
    # Sombra do emoji
    draw.text((emoji_x + 5, emoji_y + 5), emoji, fill=(0, 0, 0, 100), font=font_emoji)
    # Emoji principal
    draw.text((emoji_x, emoji_y), emoji, fill='white', font=font_emoji)
    
    # Título na parte inferior
    title_bbox = draw.textbbox((0, 0), titulo, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    title_y = height - 150
    
    # Sombra do título
    draw.text((title_x + 3, title_y + 3), titulo, fill=(0, 0, 0), font=font_title)
    # Título principal
    draw.text((title_x, title_y), titulo, fill='white', font=font_title)
    
    img.save(f'media/escola/{nome}.jpg', 'JPEG', quality=98)
    print(f"✅ Imagem {titulo} criada!")

def criar_banner_home_incrivel():
    """Cria um banner INCRÍVEL para a home"""
    width, height = 1920, 1080
    
    # Gradiente azul vibrante
    img = Image.new('RGB', (width, height), color='#0f172a')
    draw = ImageDraw.Draw(img)
    
    # Criar gradiente diagonal
    for i in range(height):
        ratio = i / height
        # Do azul escuro para azul claro
        r = int(14 + (56 - 14) * ratio)
        g = int(165 + (191 - 165) * ratio)
        b = int(233 + (243 - 233) * ratio)
        draw.rectangle([(0, i), (width, i+1)], fill=(r, g, b))
    
    # Formas geométricas grandes
    draw.ellipse([1200, -200, 2200, 800], fill='#38bdf8', outline=None)
    draw.ellipse([-300, 600, 700, 1600], fill='#0284c7', outline=None)
    draw.ellipse([800, 300, 1400, 900], fill='#0ea5e9', outline=None)
    
    # Overlay para texto
    overlay = Image.new('RGBA', (width, height), (15, 23, 42, 150))
    img_rgba = img.convert('RGBA')
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    img = img_rgba.convert('RGB')
    draw = ImageDraw.Draw(img)
    
    try:
        font_huge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 140)
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)
    except:
        font_huge = ImageFont.load_default()
        font_large = ImageFont.load_default()
    
    # Texto principal
    text1 = "EDUCAÇÃO"
    text2 = "DO FUTURO"
    text3 = "Sistema Completo de Gestão Escolar"
    
    # Sombras e textos
    draw.text((102, 352), text1, fill=(0, 0, 0), font=font_huge)
    draw.text((100, 350), text1, fill='white', font=font_huge)
    
    draw.text((102, 502), text2, fill=(0, 0, 0), font=font_huge)
    draw.text((100, 500), text2, fill='#0ea5e9', font=font_huge)
    
    draw.text((102, 702), text3, fill=(0, 0, 0), font=font_large)
    draw.text((100, 700), text3, fill='#cbd5e1', font=font_large)
    
    img.save('media/escola/banner_home.jpg', 'JPEG', quality=98)
    print("✅ Banner incrível da home criado!")

if __name__ == '__main__':
    print("🎨 Criando imagens INCRÍVEIS para o sistema escolar...\n")
    
    criar_imagem_perfil_default()
    print()
    
    # Criar imagens modernas da escola
    print("📸 Criando imagens da escola...")
    criar_imagem_moderna('quadra_esportes', '#0ea5e9', '#0284c7', '⚽ ESPORTES', '🏀')
    criar_imagem_moderna('estudantes', '#10b981', '#059669', '📚 ESTUDOS', '👨‍🎓')
    criar_imagem_moderna('tecnologia', '#8b5cf6', '#7c3aed', '💻 TECH', '🖥️')
    criar_imagem_moderna('biblioteca', '#f59e0b', '#d97706', '📖 LIVROS', '📚')
    print()
    
    criar_banner_home_incrivel()
    print()
    
    # Criar cards de atividades
    print("🎯 Criando cards de atividades...")
    atividades = [
        ('card_esportes', '🏃', 'ESPORTES', '#0ea5e9', '#0284c7'),
        ('card_artes', '🎨', 'ARTES', '#8b5cf6', '#7c3aed'),
        ('card_ciencias', '🔬', 'CIÊNCIAS', '#10b981', '#059669'),
        ('card_musica', '🎵', 'MÚSICA', '#f59e0b', '#d97706'),
    ]
    
    for nome, emoji, titulo, cor1, cor2 in atividades:
        size = 800
        img = Image.new('RGB', (size, size), color='#0f172a')
        draw = ImageDraw.Draw(img)
        
        # Gradiente circular
        center = size // 2
        for radius in range(size // 2, 0, -10):
            ratio = radius / (size // 2)
            r1, g1, b1 = int(cor1[1:3], 16), int(cor1[3:5], 16), int(cor1[5:7], 16)
            r2, g2, b2 = int(cor2[1:3], 16), int(cor2[3:5], 16), int(cor2[5:7], 16)
            
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            
            draw.ellipse([center-radius, center-radius, center+radius, center+radius], fill=(r, g, b))
        
        try:
            font_emoji = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 200)
            font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 70)
        except:
            font_emoji = ImageFont.load_default()
            font_text = ImageFont.load_default()
        
        # Emoji
        emoji_bbox = draw.textbbox((0, 0), emoji, font=font_emoji)
        emoji_width = emoji_bbox[2] - emoji_bbox[0]
        emoji_x = (size - emoji_width) // 2
        draw.text((emoji_x + 3, 203), emoji, fill=(0, 0, 0, 100), font=font_emoji)
        draw.text((emoji_x, 200), emoji, fill='white', font=font_emoji)
        
        # Título
        title_bbox = draw.textbbox((0, 0), titulo, font=font_text)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (size - title_width) // 2
        draw.text((title_x + 2, 502), titulo, fill=(0, 0, 0), font=font_text)
        draw.text((title_x, 500), titulo, fill='white', font=font_text)
        
        img.save(f'media/escola/{nome}.jpg', 'JPEG', quality=98)
        print(f"✅ Card {titulo} criado!")
    
    print()
    print("✨ TODAS AS IMAGENS INCRÍVEIS FORAM CRIADAS!")
    print("\n📁 Localizações:")
    print("   - Perfil default: media/perfis/default.jpg")
    print("   - Imagens da escola: media/escola/")
    print("\n🎨 As imagens agora estão MUITO mais bonitas e modernas!")

    """Cria uma imagem de perfil padrão moderna"""
    size = 400
    img = Image.new('RGB', (size, size), color='#0f172a')
    draw = ImageDraw.Draw(img)
    
    # Círculo azul de fundo
    circle_margin = 50
    draw.ellipse(
        [circle_margin, circle_margin, size-circle_margin, size-circle_margin],
        fill='#0ea5e9'
    )
    
    # Desenhar ícone de usuário simplificado
    # Cabeça
    head_radius = 60
    head_center = size // 2
    draw.ellipse(
        [head_center-head_radius, 120, head_center+head_radius, 240],
        fill='white'
    )
    
    # Corpo (semicírculo)
    body_width = 140
    body_height = 120
    draw.ellipse(
        [head_center-body_width, 220, head_center+body_width, 220+body_height*2],
        fill='white'
    )
    
    img.save('media/perfis/default.jpg', 'JPEG', quality=95)
    print("✅ Imagem de perfil default criada!")

def criar_imagem_hero(nome, cor_fundo, cor_acento, texto, icone_texto):
    """Cria imagens hero modernas para a home"""
    width, height = 1200, 600
    img = Image.new('RGB', (width, height), color=cor_fundo)
    draw = ImageDraw.Draw(img)
    
    # Adicionar formas geométricas modernas
    # Círculos decorativos
    draw.ellipse([800, 100, 1000, 300], fill=cor_acento, outline=None)
    draw.ellipse([100, 350, 250, 500], fill=cor_acento, outline=None)
    
    # Retângulos com transparência simulada (mais escuros)
    overlay_color = '#1e293b'
    draw.rectangle([0, 0, 600, height], fill=overlay_color)
    
    # Gradiente simulado com linhas
    for i in range(0, height, 10):
        alpha = int(255 * (i / height))
        color_value = f'#{alpha:02x}{alpha:02x}{alpha:02x}'
        
    try:
        # Tentar usar fonte do sistema
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
    
    # Adicionar texto
    draw.text((50, 200), icone_texto, fill='white', font=font_large)
    draw.text((50, 300), texto, fill='white', font=font_medium)
    
    img.save(f'media/escola/{nome}.jpg', 'JPEG', quality=95)
    print(f"✅ Imagem {nome} criada!")

def criar_imagens_escola():
    """Cria imagens modernas para a escola"""
    
    # Imagem 1: Quadra de Esportes
    criar_imagem_hero(
        'quadra_esportes',
        '#0f172a',
        '#0ea5e9',
        'Esportes e Atividades',
        '🏀'
    )
    
    # Imagem 2: Estudantes
    criar_imagem_hero(
        'estudantes',
        '#1e293b',
        '#10b981',
        'Aprendizado Moderno',
        '📚'
    )
    
    # Imagem 3: Tecnologia
    criar_imagem_hero(
        'tecnologia',
        '#0f172a',
        '#8b5cf6',
        'Tecnologia e Inovação',
        '💻'
    )
    
    # Imagem 4: Biblioteca
    criar_imagem_hero(
        'biblioteca',
        '#1e293b',
        '#f59e0b',
        'Biblioteca Digital',
        '📖'
    )

def criar_banner_home():
    """Cria banner principal para a home"""
    width, height = 1920, 800
    img = Image.new('RGB', (width, height), color='#0f172a')
    draw = ImageDraw.Draw(img)
    
    # Elementos decorativos modernos
    # Círculos grandes
    draw.ellipse([1200, -100, 1800, 500], fill='#0ea5e9', outline=None)
    draw.ellipse([-200, 400, 400, 1000], fill='#8b5cf6', outline=None)
    
    # Círculos médios
    draw.ellipse([800, 500, 1000, 700], fill='#10b981', outline=None)
    
    # Overlay escuro
    draw.rectangle([0, 0, 900, height], fill='#0f172a')
    
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    except:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
    
    # Texto
    draw.text((100, 250), "Sistema Escolar", fill='white', font=font_title)
    draw.text((100, 360), "Moderno", fill='#0ea5e9', font=font_title)
    draw.text((100, 500), "Educação de qualidade com tecnologia", fill='#94a3b8', font=font_subtitle)
    
    img.save('media/escola/banner_home.jpg', 'JPEG', quality=95)
    print("✅ Banner da home criado!")

def criar_cards_atividades():
    """Cria imagens para cards de atividades"""
    atividades = [
        ('card_esportes', '🏃', 'Esportes', '#0ea5e9'),
        ('card_artes', '🎨', 'Artes', '#8b5cf6'),
        ('card_ciencias', '🔬', 'Ciências', '#10b981'),
        ('card_musica', '🎵', 'Música', '#f59e0b'),
    ]
    
    for nome, emoji, titulo, cor in atividades:
        size = 600
        img = Image.new('RGB', (size, size), color='#1e293b')
        draw = ImageDraw.Draw(img)
        
        # Círculo de fundo
        margin = 100
        draw.ellipse([margin, margin, size-margin, size-margin], fill=cor)
        
        # Círculo interno
        inner_margin = 150
        draw.ellipse([inner_margin, inner_margin, size-inner_margin, size-inner_margin], fill='white')
        
        try:
            font_emoji = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 120)
            font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
        except:
            font_emoji = ImageFont.load_default()
            font_text = ImageFont.load_default()
        
        # Emoji centralizado
        draw.text((size//2 - 60, size//2 - 80), emoji, fill=cor, font=font_emoji)
        
        img.save(f'media/escola/{nome}.jpg', 'JPEG', quality=95)
        print(f"✅ Card {titulo} criado!")

if __name__ == '__main__':
    print("🎨 Criando imagens para o sistema escolar...\n")
    
    criar_imagem_perfil_default()
    print()
    
    criar_imagens_escola()
    print()
    
    criar_banner_home()
    print()
    
    criar_cards_atividades()
    print()
    
    print("✨ Todas as imagens foram criadas com sucesso!")
    print("\n📁 Localizações:")
    print("   - Perfil default: media/perfis/default.jpg")
    print("   - Imagens da escola: media/escola/")

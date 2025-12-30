"""
Script para criar imagens realistas para o sistema escolar
Usando técnicas avançadas de geração de imagens com gradientes e composições
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os
import random

# Criar diretório se não existir
os.makedirs('media/escola', exist_ok=True)
os.makedirs('media/perfis', exist_ok=True)

def criar_gradiente_realista(width, height, cores):
    """Cria gradiente suave e realista"""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    for y in range(height):
        # Interpolação suave entre cores
        ratio = y / height
        if ratio < 0.5:
            r = int(cores[0][0] + (cores[1][0] - cores[0][0]) * (ratio * 2))
            g = int(cores[0][1] + (cores[1][1] - cores[0][1]) * (ratio * 2))
            b = int(cores[0][2] + (cores[1][2] - cores[0][2]) * (ratio * 2))
        else:
            r = int(cores[1][0] + (cores[2][0] - cores[1][0]) * ((ratio - 0.5) * 2))
            g = int(cores[1][1] + (cores[2][1] - cores[1][1]) * ((ratio - 0.5) * 2))
            b = int(cores[1][2] + (cores[2][2] - cores[1][2]) * ((ratio - 0.5) * 2))
        
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return image

def adicionar_textura(image):
    """Adiciona textura para parecer mais realista"""
    width, height = image.size
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Adicionar pontos aleatórios para textura
    for _ in range(width * height // 100):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        alpha = random.randint(5, 20)
        draw.point((x, y), fill=(255, 255, 255, alpha))
    
    return Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')

def criar_quadra_esportiva():
    """Cria imagem de quadra esportiva"""
    width, height = 1200, 800
    
    # Cores de quadra (verde do campo)
    cores = [(34, 139, 34), (50, 205, 50), (34, 139, 34)]
    img = criar_gradiente_realista(width, height, cores)
    draw = ImageDraw.Draw(img)
    
    # Linhas da quadra (brancas)
    line_color = (255, 255, 255)
    line_width = 8
    
    # Linhas laterais
    draw.rectangle([100, 100, width-100, height-100], outline=line_color, width=line_width)
    
    # Linha central
    draw.line([(width//2, 100), (width//2, height-100)], fill=line_color, width=line_width)
    
    # Círculos centrais
    center_x, center_y = width//2, height//2
    for radius in [80, 150]:
        draw.ellipse([center_x-radius, center_y-radius, center_x+radius, center_y+radius], 
                     outline=line_color, width=line_width)
    
    # Áreas de gol
    for x in [100, width-300]:
        draw.rectangle([x, height//2-100, x+200, height//2+100], 
                      outline=line_color, width=line_width)
    
    # Adicionar textura
    img = adicionar_textura(img)
    
    # Aplicar blur suave para efeito fotográfico
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    
    # Ajustar contraste
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.3)
    
    img.save('media/escola/quadra_esportes.jpg', 'JPEG', quality=95)
    print("✅ Quadra esportiva criada")

def criar_estudantes():
    """Cria imagem de ambiente de estudos"""
    width, height = 1200, 800
    
    # Cores de biblioteca/sala (tons quentes)
    cores = [(101, 67, 33), (139, 90, 43), (210, 180, 140)]
    img = criar_gradiente_realista(width, height, cores)
    draw = ImageDraw.Draw(img)
    
    # Criar "mesas" com livros
    for i in range(5):
        x = 150 + i * 200
        y = 250 + (i % 2) * 150
        
        # Mesa (retângulo escuro)
        draw.rectangle([x, y, x+150, y+200], fill=(139, 69, 19))
        
        # "Livros" empilhados
        cores_livros = [(255, 200, 100), (100, 150, 255), (255, 100, 100), (100, 255, 150)]
        for j in range(4):
            livro_y = y + 150 - j*30
            draw.rectangle([x+20, livro_y, x+130, livro_y+25], 
                          fill=cores_livros[j % len(cores_livros)])
    
    # Adicionar "pessoas" (formas abstratas)
    for i in range(6):
        x = 100 + i * 180
        y = 150 if i % 2 == 0 else 320
        
        # Cabeça
        draw.ellipse([x, y, x+40, y+40], fill=(255, 220, 177))
        
        # Corpo
        draw.rectangle([x+5, y+35, x+35, y+90], fill=(random.choice([
            (0, 100, 200), (200, 50, 50), (50, 150, 50), (150, 50, 150)
        ])))
    
    # Adicionar textura
    img = adicionar_textura(img)
    
    # Blur e contraste
    img = img.filter(ImageFilter.GaussianBlur(radius=1.5))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    
    # Ajustar brilho
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.1)
    
    img.save('media/escola/estudantes.jpg', 'JPEG', quality=95)
    print("✅ Estudantes criada")

def criar_tecnologia():
    """Cria imagem de laboratório de tecnologia"""
    width, height = 1200, 800
    
    # Cores tech (azul escuro para claro)
    cores = [(10, 25, 47), (14, 165, 233), (56, 189, 248)]
    img = criar_gradiente_realista(width, height, cores)
    draw = ImageDraw.Draw(img)
    
    # Criar "computadores" em fileiras
    for row in range(3):
        for col in range(5):
            x = 100 + col * 220
            y = 150 + row * 220
            
            # Monitor
            draw.rectangle([x, y, x+180, y+140], fill=(30, 30, 30), outline=(200, 200, 200), width=3)
            
            # Tela (azul brilhante)
            draw.rectangle([x+10, y+10, x+170, y+110], fill=(0, 150, 255))
            
            # Adicionar "código" na tela
            for line in range(5):
                line_y = y + 20 + line * 18
                line_width = random.randint(50, 140)
                draw.rectangle([x+20, line_y, x+20+line_width, line_y+12], 
                              fill=(255, 255, 255))
            
            # Base do monitor
            draw.rectangle([x+70, y+140, x+110, y+160], fill=(50, 50, 50))
            
            # Teclado
            draw.rectangle([x+20, y+165, x+160, y+190], fill=(40, 40, 40), outline=(100, 100, 100), width=2)
    
    # Adicionar "luzes" no ambiente
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    for _ in range(10):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(30, 80)
        draw_overlay.ellipse([x, y, x+size, y+size], 
                            fill=(100, 200, 255, 30))
    
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    # Adicionar textura
    img = adicionar_textura(img)
    
    # Blur leve
    img = img.filter(ImageFilter.GaussianBlur(radius=0.8))
    
    # Aumentar saturação para efeito tech
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.5)
    
    img.save('media/escola/tecnologia.jpg', 'JPEG', quality=95)
    print("✅ Tecnologia criada")

def criar_biblioteca():
    """Cria imagem de biblioteca"""
    width, height = 1200, 800
    
    # Cores de biblioteca (marrom para bege)
    cores = [(52, 39, 30), (101, 67, 33), (222, 184, 135)]
    img = criar_gradiente_realista(width, height, cores)
    draw = ImageDraw.Draw(img)
    
    # Criar estantes de livros
    for shelf in range(5):
        shelf_y = 100 + shelf * 140
        
        # Estante (madeira)
        draw.rectangle([50, shelf_y, width-50, shelf_y+120], 
                      fill=(139, 90, 43), outline=(101, 67, 33), width=4)
        
        # Prateleiras
        for nivel in range(3):
            nivel_y = shelf_y + 10 + nivel * 35
            draw.rectangle([55, nivel_y, width-55, nivel_y+30], 
                          fill=(160, 110, 60), outline=(101, 67, 33), width=2)
            
            # Livros nas prateleiras
            x_pos = 70
            while x_pos < width - 70:
                livro_width = random.randint(15, 40)
                cor_livro = random.choice([
                    (178, 34, 34), (70, 130, 180), (60, 179, 113),
                    (255, 165, 0), (147, 112, 219), (220, 20, 60)
                ])
                
                # Livro
                draw.rectangle([x_pos, nivel_y+2, x_pos+livro_width, nivel_y+28], 
                              fill=cor_livro, outline=(0, 0, 0), width=1)
                
                # Detalhes do livro (lombada)
                if livro_width > 20:
                    draw.line([(x_pos+5, nivel_y+2), (x_pos+5, nivel_y+28)], 
                             fill=(0, 0, 0), width=1)
                
                x_pos += livro_width + random.randint(2, 8)
    
    # Adicionar "pessoas" lendo
    for i in range(3):
        x = 200 + i * 350
        y = 600
        
        # Pessoa sentada (forma simplificada)
        draw.ellipse([x, y, x+50, y+50], fill=(255, 220, 177))
        draw.rectangle([x+10, y+45, x+40, y+100], fill=(0, 100, 150))
        
        # Livro aberto
        draw.rectangle([x+50, y+60, x+120, y+90], fill=(255, 255, 200), outline=(0, 0, 0), width=2)
        draw.line([(x+85, y+60), (x+85, y+90)], fill=(0, 0, 0), width=2)
    
    # Adicionar textura
    img = adicionar_textura(img)
    
    # Blur e ajustes
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    
    img.save('media/escola/biblioteca.jpg', 'JPEG', quality=95)
    print("✅ Biblioteca criada")

def criar_banner_home():
    """Cria banner principal"""
    width, height = 1920, 600
    
    # Gradiente azul profissional
    cores = [(15, 23, 42), (14, 165, 233), (56, 189, 248)]
    img = criar_gradiente_realista(width, height, cores)
    draw = ImageDraw.Draw(img)
    
    # Adicionar formas geométricas modernas
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    # Círculos decorativos
    for i in range(8):
        x = random.randint(-100, width)
        y = random.randint(-100, height)
        size = random.randint(100, 300)
        alpha = random.randint(10, 40)
        draw_overlay.ellipse([x, y, x+size, y+size], 
                            fill=(255, 255, 255, alpha))
    
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    # Adicionar textura
    img = adicionar_textura(img)
    
    # Blur e melhorias
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.3)
    
    img.save('media/escola/banner_home.jpg', 'JPEG', quality=95)
    print("✅ Banner home criado")

def criar_cards():
    """Cria imagens para os cards"""
    cards = [
        ('aprendizado_moderno', [(75, 0, 130), (138, 43, 226), (186, 85, 211)]),
        ('ensino_qualidade', [(178, 34, 34), (220, 20, 60), (255, 99, 71)]),
        ('infraestrutura', [(0, 100, 0), (34, 139, 34), (50, 205, 50)]),
        ('tecnologia_avancada', [(0, 71, 171), (0, 119, 182), (3, 169, 244)])
    ]
    
    for nome, cores in cards:
        width, height = 800, 600
        img = criar_gradiente_realista(width, height, cores)
        
        # Adicionar formas abstratas
        draw = ImageDraw.Draw(img)
        for _ in range(15):
            x = random.randint(0, width-200)
            y = random.randint(0, height-200)
            size = random.randint(50, 150)
            shape_type = random.choice(['circle', 'square'])
            
            if shape_type == 'circle':
                draw.ellipse([x, y, x+size, y+size], 
                           fill=(255, 255, 255, 30) if random.random() > 0.5 else None,
                           outline=(255, 255, 255), width=3)
            else:
                draw.rectangle([x, y, x+size, y+size],
                             fill=None, outline=(255, 255, 255), width=3)
        
        # Adicionar textura
        img = adicionar_textura(img)
        
        # Blur e melhorias
        img = img.filter(ImageFilter.GaussianBlur(radius=1.5))
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.2)
        
        img.save(f'media/escola/card_{nome}.jpg', 'JPEG', quality=95)
        print(f"✅ Card {nome} criado")

def criar_perfil_default():
    """Cria imagem de perfil padrão"""
    size = 400
    img = Image.new('RGB', (size, size), (14, 165, 233))
    draw = ImageDraw.Draw(img)
    
    # Círculo para cabeça
    center = size // 2
    head_radius = 80
    draw.ellipse([center-head_radius, center-head_radius-50, 
                  center+head_radius, center+head_radius-50], 
                 fill=(255, 220, 177))
    
    # Corpo (semicírculo)
    body_radius = 120
    draw.ellipse([center-body_radius, center+20, 
                  center+body_radius, center+20+body_radius*2], 
                 fill=(30, 58, 138))
    
    # Adicionar textura
    img = adicionar_textura(img)
    
    img.save('media/perfis/default.jpg', 'JPEG', quality=95)
    print("✅ Perfil default criado")

if __name__ == '__main__':
    print("🎨 Criando imagens realistas para o sistema escolar...\n")
    
    criar_banner_home()
    criar_quadra_esportiva()
    criar_estudantes()
    criar_tecnologia()
    criar_biblioteca()
    criar_cards()
    criar_perfil_default()
    
    print("\n✨ TODAS AS IMAGENS REALISTAS FORAM CRIADAS COM SUCESSO!")
    print("📁 Verifique a pasta media/escola/ para ver as imagens")

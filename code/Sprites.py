import pygame
import random
import os  # Necessário para achar as pastas de imagem com segurança
from config import LARGURA, ALTURA, VERMELHO_PERIGO, DOURADO

# --- Lógica de carregamento de imagens ---
# Pega o caminho da pasta onde este arquivo 'sprites.py' está
pasta_principal = os.path.dirname(__file__)
pasta_assets = os.path.join(pasta_principal, 'assets')
pasta_imagens = os.path.join(pasta_assets, 'imagens')

# Carrega as imagens e prepara para transparência (.convert_alpha())
# Nota: Se o arquivo não existir, o pygame dará erro ao executar.
try:
    img_mago = pygame.image.load(os.path.join(pasta_imagens, 'mago.png')).convert_alpha()
    img_espada = pygame.image.load(os.path.join(pasta_imagens, 'espada.png')).convert_alpha()
    # Placeholder caso você não tenha imagem de moeda ainda:
    if os.path.exists(os.path.join(pasta_imagens, 'moeda.png')):
        img_moeda = pygame.image.load(os.path.join(pasta_imagens, 'moeda.png')).convert_alpha()
    else:
        img_moeda = None # Usaremos o desenho vetorial se não houver imagem
except pygame.error as e:
    print(f"Erro ao carregar imagens. Verifique se a pasta 'assets/imagens' existe e contém 'mago.png' e 'espada.png'.")
    print(f"Erro detalhado: {e}")
    pygame.quit()
    import sys; sys.exit()


class Jogador:
    def __init__(self):
        # Tamanho lógico da colisão (pode ser diferente do tamanho da imagem, mas vamos manter igual por enquanto)
        self.largura, self.altura = 50, 60 # Magos costumam ser mais altos que largos
        
        # AJUSTE DA IMAGEM: Redimensiona a imagem carregada para o tamanho que queremos no jogo
        self.image = pygame.transform.scale(img_mago, (self.largura, self.altura))
        
        # O Rect agora é criado baseado no tamanho da imagem redimensionada
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 70
        
        self.velocidade = 7
        # self.cor não é mais necessária

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < LARGURA: self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.top > 0: self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.bottom < ALTURA: self.rect.y += self.velocidade

    def desenhar(self, superficie):
        # MUDA de draw.rect para BLIT
        # Blit 'desenha' uma imagem (source) sobre outra (target) na posição do rect
        superficie.blit(self.image, self.rect)


class Inimigo:
    def __init__(self):
        # Espadas podem ser finas e longas
        self.largura, self.altura = 25, 50 
        
        # AJUSTE DA IMAGEM
        self.image = pygame.transform.scale(img_espada, (self.largura, self.altura))
        
        self.x = random.randint(0, LARGURA - self.largura)
        self.velocidade = random.randint(4, 8) # Espadas caindo podem ser rápidas
        
        # Define o Rect com base na imagem
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = -70 # Começa um pouco mais acima por ser mais alta
        # self.cor não é mais necessária

    def cair(self):
        self.rect.y += self.velocidade

    def desenhar(self, superficie):
        # MUDA para BLIT
        superficie.blit(self.image, self.rect)


class Item:
    def __init__(self):
        self.largura, self.altura = 30, 30
        
        # AJUSTE DA IMAGEM (com verificação se a imagem existe)
        if img_moeda:
            self.image = pygame.transform.scale(img_moeda, (self.largura, self.altura))
            self.rect = self.image.get_rect()
        else:
            self.image = None
            self.rect = pygame.Rect(0, 0, self.largura, self.altura) # Rect vazio se não houver imagem
            
        self.x = random.randint(0, LARGURA - self.largura)
        self.velocidade = random.randint(3, 7)
        self.rect.x = self.x
        self.rect.y = -50
        self.cor = DOURADO # Mantemos a cor para o placeholder

    def cair(self):
        self.rect.y += self.velocidade

    def desenhar(self, superficie):
        if self.image:
            # Desenha imagem
            superficie.blit(self.image, self.rect)
        else:
            # Mantém o desenho vetorial antigo se não houver imagem
            pygame.draw.ellipse(superficie, self.cor, self.rect)
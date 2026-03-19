import pygame
import random
import os
from config import LARGURA, ALTURA

# --- CONFIGURAÇÃO DE CAMINHOS ---
caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_raiz = os.path.abspath(os.path.join(caminho_atual, ".."))
pasta_imagens = os.path.join(caminho_raiz, 'assets', 'imagens')

def carregar_img(nome, largura, altura):
    caminho_completo = os.path.join(pasta_imagens, nome)
    try:
        # Carregamos a imagem simples primeiro
        imagem = pygame.image.load(caminho_completo)
        # Se o pygame já iniciou a tela, usamos o convert_alpha para performance
        if pygame.display.get_init():
            imagem = imagem.convert_alpha()
        return pygame.transform.scale(imagem, (largura, altura))
    except Exception as e:
        print(f"Erro ao carregar {nome}: {e}")
        temp = pygame.Surface((largura, altura))
        temp.fill((255, 0, 255))
        return temp

class Jogador:
    def __init__(self):
        # Carregamos a imagem aqui dentro, no momento em que o jogador nasce
        self.image = carregar_img('mago.png', 50, 60)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 70
        self.velocidade = 7

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < LARGURA: self.rect.x += self.velocidade
        
    def desenhar(self, superficie):
        superficie.blit(self.image, self.rect)

class Inimigo:
    def __init__(self):
        self.image = carregar_img('espada.png', 25, 50)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA - self.rect.width)
        self.rect.y = -70
        self.velocidade = random.randint(4, 9)

    def cair(self):
        self.rect.y += self.velocidade

    def desenhar(self, superficie):
        superficie.blit(self.image, self.rect)

class Item:
    def __init__(self):
        self.image = carregar_img('moeda.png', 30, 30)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA - self.rect.width)
        self.rect.y = -50
        self.velocidade = random.randint(3, 6)

    def cair(self):
        self.rect.y += self.velocidade

    def desenhar(self, superficie):
        superficie.blit(self.image, self.rect)
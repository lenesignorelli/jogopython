import pygame
import random
from config import LARGURA, ALTURA, VERMELHO_PERIGO, DOURADO

class Jogador:
    def __init__(self):
        self.largura, self.altura = 50, 50
        self.rect = pygame.Rect(LARGURA // 2, ALTURA - 70, self.largura, self.altura)
        self.velocidade = 7
        self.cor = (255, 0, 0)

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.right < LARGURA: self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.top > 0: self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.bottom < ALTURA: self.rect.y += self.velocidade

    def desenhar(self, superficie):
        pygame.draw.rect(superficie, self.cor, self.rect)

class Inimigo:
    def __init__(self):
        self.largura, self.altura = 40, 40
        self.x = random.randint(0, LARGURA - self.largura)
        self.velocidade = random.randint(5, 10)
        self.rect = pygame.Rect(self.x, -50, self.largura, self.altura)
        self.cor = VERMELHO_PERIGO

    def cair(self):
        self.rect.y += self.velocidade

    def desenhar(self, superficie):
        pygame.draw.rect(superficie, self.cor, self.rect)

class Item:
    def __init__(self):
        self.largura, self.altura = 30, 30
        self.x = random.randint(0, LARGURA - self.largura)
        self.velocidade = random.randint(3, 7)
        self.rect = pygame.Rect(self.x, -50, self.largura, self.altura)
        self.cor = DOURADO

    def cair(self):
        self.rect.y += self.velocidade

    def desenhar(self, superficie):
        pygame.draw.ellipse(superficie, self.cor, self.rect)
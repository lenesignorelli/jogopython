import pygame

# Inicializamos o pygame aqui apenas para poder carregar as fontes
pygame.init()

# Dimensões
LARGURA, ALTURA = 800, 600
FPS = 60

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (50, 150, 200)
VERMELHO_PERIGO = (200, 0, 0)
DOURADO = (255, 215, 0)
CINZA_FUNDO = (30, 30, 30)

# Fontes
FONTE_TITULO = pygame.font.SysFont("Arial", 60, bold=True)
FONTE_TEXTO = pygame.font.SysFont("Arial", 30)

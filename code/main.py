import pygame
import sys
import os
from config import *
from sprites import Jogador, Inimigo, Item
from utils import desenhar_texto

pygame.init()
pygame.mixer.init() # Inicializa o sistema de som
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu Jogo Modular")
clock = pygame.time.Clock()

def menu_principal():
    while True:
        tela.fill(AZUL)
        desenhar_texto(tela, "MEU JOGO INCRÍVEL", FONTE_TITULO, BRANCO, LARGURA//2, 150)
        desenhar_texto(tela, "Setas para mover | ENTER para começar", FONTE_TEXTO, PRETO, LARGURA//2, 400)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN: return

        pygame.display.flip()
        clock.tick(30)

def tela_game_over(pontos):
    while True:
        tela.fill(PRETO)
        desenhar_texto(tela, "GAME OVER", FONTE_TITULO, VERMELHO_PERIGO, LARGURA//2, 200)
        desenhar_texto(tela, f"Pontos: {pontos}", FONTE_TEXTO, BRANCO, LARGURA//2, 300)
        desenhar_texto(tela, "R: Reiniciar | M: Menu", FONTE_TEXTO, BRANCO, LARGURA//2, 450)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r: return "jogar"
                if evento.key == pygame.K_m: return "menu"

        pygame.display.flip()
        clock.tick(30)

def loop_do_jogo():
    img_fundo = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "assets", "imagens", "fundo.png")).convert()
    img_fundo = pygame.transform.scale(img_fundo, (LARGURA, ALTURA))
    # --- CONFIGURAÇÃO DE SONS ---
    pasta_sons = os.path.join(os.path.dirname(__file__), "..", "assets", "sons")
    
    # 1. Música de Fundo (Streaming - não carrega tudo na RAM de uma vez)
    pygame.mixer.music.load(os.path.join(pasta_sons, "musica_fundo.mp3"))
    pygame.mixer.music.set_volume(0.5) # Volume de 0.0 a 1.0
    pygame.mixer.music.play(-1)        # -1 faz a música tocar em loop infinito

    # 2. Efeitos Sonoros (Carregam na RAM para tocar instantaneamente)
    som_moeda = pygame.mixer.Sound(os.path.join(pasta_sons, "som_moeda.wav"))
    game_over = pygame.mixer.Sound(os.path.join(pasta_sons, "game_over.wav"))
    player = Jogador()
    itens, inimigos = [], []
    pontos = 0
    timer_item = timer_inimigo = 0

    while True:
        tela.blit(img_fundo, (0, 0))
        dt = clock.get_time()
        timer_item += dt
        timer_inimigo += dt

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        # Spawns
        if timer_item > 1200:
            itens.append(Item()); timer_item = 0
        if timer_inimigo > 1500:
            inimigos.append(Inimigo()); timer_inimigo = 0

        # Atualização
        teclas = pygame.key.get_pressed()
        player.mover(teclas)

        for item in itens[:]:
            item.cair()
            if player.rect.colliderect(item.rect):
                som_moeda.play()  # Toca o barulhinho da moeda!
                pontos += 1; 
                itens.remove(item)
            elif item.rect.top > ALTURA: itens.remove(item)

        for inimigo in inimigos[:]:
            inimigo.cair()
            if player.rect.colliderect(inimigo.rect):
                pygame.mixer.music.stop() # Para a música de fundo
                game_over.play()            # Toca o som de dano
                pygame.time.delay(500)    # Pequena pausa de 0.5s para o jogador ouvir o som antes da tela mudar
                return tela_game_over(pontos)
            elif inimigo.rect.top > ALTURA: inimigos.remove(inimigo)

        # Desenho
        player.desenhar(tela)
        for i in itens: i.desenhar(tela)
        for e in inimigos: e.desenhar(tela)
        desenhar_texto(tela, f"Pontos: {pontos}", FONTE_TEXTO, BRANCO, 700, 30)

        pygame.display.flip()
        clock.tick(FPS)

# Início do Programa
if __name__ == "__main__":
    while True:
        menu_principal()
        resultado = loop_do_jogo()
        while resultado == "jogar":
            resultado = loop_do_jogo()
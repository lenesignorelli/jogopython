import pygame

def desenhar_texto(superficie_tela, texto, fonte, cor, x, y):
    texto_obj = fonte.render(texto, True, cor)
    retangulo = texto_obj.get_rect(center=(x, y))
    superficie_tela.blit(texto_obj, retangulo)
import pygame
from pathlib import Path

class Cursor:
    def __init__(self):
        cam_pasta = Path(__file__).resolve().parent.parent / "data" / "cursores"
        cam_arte = cam_pasta / "cursor.png"
        self.imagem = pygame.image.load(str(cam_arte)).convert_alpha()

    def desenhar(self, tela):
        pos = pygame.mouse.get_pos()
        tela.blit(self.imagem, pos)

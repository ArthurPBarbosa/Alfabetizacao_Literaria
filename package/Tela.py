import pygame
from pathlib import Path

class Tela:
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((640, 640))
        pygame.display.set_caption("Alfabetização Literária || V.1.0")
        self.fundo = None

    def carregar_fundo(self, nome_fundo):
        pasta_mae = Path(__file__).resolve().parent / "data"
        localizacao_da_arte = str(pasta_mae / "artes" / nome_fundo)
        self.fundo = pygame.image.load(localizacao_da_arte).convert()

    def renderizar_fundo(self):
        if self.fundo:
            self.janela.blit(self.fundo, (0, 0))

    def remover_fundo(self):
        self.fundo = None

    def limpar(self):
        self.janela.fill((0, 0, 0))

    def atualizar(self):
        pygame.display.flip()

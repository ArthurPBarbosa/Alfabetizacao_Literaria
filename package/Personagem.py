import pygame
from pathlib import Path

class Personagem:
    def __init__(self, nome, silaba_certa=None, silabas_erradas=None):
        self.nome = nome
        self.silaba_certa = silaba_certa
        self.silabas_erradas = silabas_erradas or []

        pasta_mae = Path(__file__).resolve().parent.parent
        localizacao_da_arte = str(pasta_mae / "data" / "artes" / f"{nome}.png")
        self.arte_personagem = pygame.image.load(localizacao_da_arte).convert_alpha()

    def exibir(self, tela):
        tela.blit(self.arte_personagem, (170, 60))

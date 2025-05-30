import pygame
from abc import ABC, abstractmethod

def criar_retrato(nome_personagem, raridade):
    if raridade in ["raro", "épico", "lendário"]:
        return RetratoRaro(nome_personagem, raridade)
    return RetratoComum(nome_personagem)

class Retrato(ABC):
    def __init__(self, nome_personagem):
        self.nome = nome_personagem
        self.tipo = "comum"

    @abstractmethod
    def atualizar(self, agora):
        pass

    @abstractmethod
    def exibir(self, tela):
        pass

    @abstractmethod
    def marcar_acerto(self):
        pass

    @abstractmethod
    def destruir(self):
        pass

class RetratoComum(Retrato):
    def __init__(self, nome_personagem):
        super().__init__(nome_personagem)
        imagem = pygame.image.load(f"data/tazos/{self.nome}.png").convert_alpha()
        largura = int(imagem.get_width() / 2.5)
        altura = int(imagem.get_height() / 2.5)
        self.imagem = pygame.transform.smoothscale(imagem, (largura, altura))
        self.x = None
        self.y = None

    def atualizar(self, agora):
        pass 

    def exibir(self, tela):
        self.x = tela.get_width() - self.imagem.get_width() - 20
        self.y = 20
        tela.blit(self.imagem, (self.x, self.y))

    def marcar_acerto(self):
        pass

    def destruir(self):
        pass 

class RetratoRaro(RetratoComum):
    def __init__(self, nome_personagem, tipo):
        super().__init__(nome_personagem)
        self.tipo = tipo

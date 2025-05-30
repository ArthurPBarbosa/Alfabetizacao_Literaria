import pygame
import random
from pathlib import Path

class Musica:
    indice_atual = -1
    musicas_disponiveis = []

    @classmethod
    def carregar_lista_de_musicas(cls):
        if not cls.musicas_disponiveis:
            pasta = Path(__file__).resolve().parent.parent / "data" / "musicas"
            cls.musicas_disponiveis = list(pasta.glob("*.mp3"))
            random.shuffle(cls.musicas_disponiveis)

    def __init__(self):
        self.carregar_lista_de_musicas()

    def escolher_proxima_musica(self):
        musicas = Musica.musicas_disponiveis
        if not musicas:
            return None
        if len(musicas) == 1:
            return str(musicas[0])

        candidatas = [m for i, m in enumerate(musicas) if i != Musica.indice_atual]
        proxima = random.choice(candidatas)
        Musica.indice_atual = musicas.index(proxima)
        return str(proxima)

    def tocar(self, caminho_musica=None):
        if caminho_musica is None:
            caminho_musica = self.escolher_proxima_musica()
        if caminho_musica:
            pygame.mixer.music.load(str(caminho_musica))
            pygame.mixer.music.play(-1)
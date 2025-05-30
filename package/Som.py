import pygame
from pathlib import Path

class Som:
    def __init__(self, nome_do_som):
        cam_som = Path(__file__).resolve().parent.parent / "data" / "sons" / nome_do_som
        self.som = pygame.mixer.Sound(str(cam_som))
        self.som.set_volume(0.5)

    def tocar(self):
        self.som.play()

    def parar(self):
        self.som.stop()

import pygame

class ContadorAcertos:
    def __init__(self, fonte):
        self.fonte = fonte
        self.total = 0

    def incrementar(self):
        self.total += 1

    def exibir(self, janela):
        texto = f"{self.total}"
        letras = list(texto.upper())

        largura_total = sum(self.fonte.render(l, True, (0, 0, 0)).get_width() + 5 for l in letras) - 5
        x = 550 - largura_total // 2 
        y = 120

        for letra in letras:
            cor = (255, 255, 255)
            texto_render = self.fonte.render(letra, True, cor)

            sombra = self.fonte.render(letra, True, (0, 0, 0))
            janela.blit(sombra, (x + 2, y + 2))

            janela.blit(texto_render, (x, y))
            x += texto_render.get_width() + 5

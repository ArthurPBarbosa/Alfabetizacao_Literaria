import pygame

class Botao:
    def __init__(self, fonte, texto, posicao, largura=100, altura=60):
        self.fonte = fonte
        self.texto = texto
        self.posicao = posicao
        self.largura = largura
        self.altura = altura

        self.visivel = True
        self.confirmado = False
        self.selecionado = False

        self.rect = pygame.Rect(posicao[0], posicao[1], largura, altura)
        self.cor_fundo = (255, 255, 255)

    def desenhar(self, tela):
        if not self.visivel:
            return

        pygame.draw.rect(tela, self.cor_fundo, self.rect)
        pygame.draw.rect(tela, (0, 0, 0), self.rect, 3)

        texto_renderizado = self.fonte.render(self.texto, True, (0, 0, 0))
        x = self.rect.x + (self.rect.width - texto_renderizado.get_width()) // 2
        y = self.rect.y + (self.rect.height - texto_renderizado.get_height()) // 2
        tela.blit(texto_renderizado, (x, y))

    def clicado(self, pos):
        return self.visivel and self.rect.collidepoint(pos)

    def destruir(self):
        self.visivel = False
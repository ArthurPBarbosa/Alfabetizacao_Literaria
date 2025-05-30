from .Botao import Botao

class BotaoComum(Botao):
    def desenhar(self, tela):
        if not self.visivel:
            return

        if self.confirmado:
            self.cor_fundo = (0, 0, 255)
        elif self.selecionado:
            self.cor_fundo = (0, 255, 0)
        else:
            self.cor_fundo = (255, 255, 0)

        super().desenhar(tela)
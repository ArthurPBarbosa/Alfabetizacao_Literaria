import sys
import json
import random
import pygame
import math
from pathlib import Path

from PyIgnition.PyIgnition import ParticleEffect
from PyIgnition.constants import DRAWTYPE_CIRCLE

from .Som import Som
from .Tela import Tela
from .Cursor import Cursor
from .Musica import Musica
from .Retrato import criar_retrato
from .BotaoComum import BotaoComum
from .Personagem import Personagem
from .PontosGlobais import PontosGlobais
from .PontosGlobais import pontuacao_global
from .ContadorAcertos import ContadorAcertos



class Jogo:
    def __init__(self):
        
        self.tela = Tela()
        self.retrato = None
        self.rodando = True
        self.ultimo_nome = None
        self.efeito_particulas = None
        self.fonte = pygame.font.SysFont(None, 48)
        self.contador = ContadorAcertos(self.fonte)

        self.cursor = Cursor()
        pygame.mouse.set_visible(False)

        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.3)
        self.musica = Musica()
        self.musica_atual = None
        self.som_acerto = Som("acerto.wav")

        self.botoes_silabas = []
        self.resposta_certa = None
        self.silaba_escolhida = None
        self.tempo_silaba_escolhida = None

        self.acertou = False
        self.tempo_de_espera = 0
        self.letras_digitadas = []
        self.fase_digitacao = False

        self.nomes_com_silaba = self.carregar_nomes()

        self.iniciar_modo()

    def carregar_nomes(self):
        caminho = Path(__file__).resolve().parent.parent / "data" / "dados" / "nomes.json"
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)

    def escolher_personagem(self):
        opcoes = [d for d in self.nomes_com_silaba if d["nome"] != self.ultimo_nome]
        escolhido = random.choice(opcoes)
        self.ultimo_nome = escolhido["nome"]
        personagem = Personagem(escolhido["nome"])
        personagem.silaba = escolhido["silaba_certa"]
        personagem.alternativas = escolhido["silabas_opcoes"]
        return personagem

    def definir_raridade_por_nome(self, nome_retrato):
        if nome_retrato.endswith("_4"):
            return "lendário"
        elif nome_retrato.endswith("_3"):
            return "épico"
        elif nome_retrato.endswith("_2"):
            return "raro"
        else:
            return "comum"

    def escolher_retrato_por_acertos(self):
        if self.contador.total >= 10:
            return "gandalf_4"
        elif self.contador.total >= 6:
            return "gandalf_3"
        elif self.contador.total >= 3:
            return "gandalf_2"
        else:
            return "gandalf"


    def iniciar_modo(self):
        self.personagem = self.escolher_personagem()
        self.tela.fundo = pygame.image.load("data/artes/fundo.png")

        nome_retrato = self.escolher_retrato_por_acertos()
        raridade = self.definir_raridade_por_nome(nome_retrato)
        self.retrato = criar_retrato(nome_retrato, raridade)

        nova_musica = self.musica.escolher_proxima_musica()
        if nova_musica and nova_musica != self.musica_atual:
            self.musica.tocar(nova_musica)
            self.musica_atual = nova_musica

        self.efeito_particulas = ParticleEffect(self.tela.janela, (0, 0), self.tela.janela.get_size())
        tipo = self.retrato.tipo

        if tipo == "raro":
            self.criar_efeito_fogo()
        elif tipo == "épico":
            self.criar_efeito_neve()
        elif tipo == "lendário":
            self.criar_efeito_luz()
        for botao, _ in self.botoes_silabas:
            botao.destruir()
        self.botoes_silabas.clear()

        self.configurar_botoes_silabas()

        self.resposta_certa = self.personagem.silaba
        self.silaba_escolhida = None
        self.tempo_silaba_escolhida = None
        self.letras_digitadas.clear()
        self.fase_digitacao = False
        self.acertou = False
        self.tempo_de_espera = 0

    def configurar_botoes_silabas(self):
        largura_tela = self.tela.janela.get_width()
        espacamento = 130
        y = 470
        x_inicial = (largura_tela - (espacamento * 4)) // 2 + 10
        alternativas = random.sample(self.personagem.alternativas, len(self.personagem.alternativas))

        for i, silaba in enumerate(alternativas):
            x = x_inicial + (i % 4) * espacamento
            y_botao = y + (i // 4) * 80
            botao = BotaoComum(self.fonte, silaba.upper(), (x, y_botao))
            self.botoes_silabas.append((botao, silaba))

    def executar(self):
        while self.rodando:
            pygame.event.pump()
            agora = pygame.time.get_ticks()

            if self.retrato:
                self.retrato.atualizar(agora)

            if self.fase_digitacao:
                if self.acertou and agora - self.tempo_de_espera >= 5000:
                    self.contador.incrementar()
                    self.iniciar_modo()
                else:
                    self.processar_digitacao()
            elif self.silaba_escolhida:
                if agora - self.tempo_silaba_escolhida >= 5000:
                    if self.silaba_escolhida == self.resposta_certa:
                        self.fase_digitacao = True
                        pygame.event.clear(pygame.KEYDOWN)
                        self.letras_digitadas.clear()
                    else:
                        self.resetar_selecao_silaba()
            else:
                self.processar_cliques()

            self.exibir_jogo()
            self.cursor.desenhar(self.tela.janela)
            pygame.display.flip()

        pygame.quit()

    def resetar_selecao_silaba(self):
        self.silaba_escolhida = None
        self.tempo_silaba_escolhida = None
        for botao, _ in self.botoes_silabas:
            botao.selecionado = False
            botao.confirmado = False

    def processar_cliques(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for botao, silaba in self.botoes_silabas:
                    if botao.clicado(pos):
                        if botao.selecionado and not botao.confirmado:
                            botao.confirmado = True
                            self.silaba_escolhida = silaba
                            self.tempo_silaba_escolhida = pygame.time.get_ticks()
                            if silaba == self.resposta_certa:
                                self.som_acerto.tocar()
                                self.retrato.marcar_acerto()
                        elif not botao.selecionado:
                            for outro, _ in self.botoes_silabas:
                                outro.selecionado = False
                                outro.confirmado = False
                            botao.selecionado = True

    def processar_digitacao(self):
        if not self.fase_digitacao:
            return

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    self.letras_digitadas = self.letras_digitadas[:-1]
                elif evento.unicode.isalpha():
                    if len(self.letras_digitadas) < len(self.resposta_certa):
                        self.letras_digitadas.append(evento.unicode.lower())

                    if not self.acertou and ''.join(self.letras_digitadas).lower() == self.resposta_certa.lower():
                        self.acertou = True
                        self.tempo_de_espera = pygame.time.get_ticks()
                        self.som_acerto.tocar()
                        self.retrato.marcar_acerto()
                        pontuacao_global.adicionar(1)
                        print(pontuacao_global.pontos)


    def exibir_jogo(self):
        self.tela.limpar()
        self.tela.renderizar_fundo()
        
        if self.efeito_particulas:
            self.efeito_particulas.Update()
            self.efeito_particulas.Redraw()
        
        self.personagem.exibir(self.tela.janela)
        self.retrato.exibir(self.tela.janela)
        self.contador.exibir(self.tela.janela)

        self.exibir_letras()

        if not self.fase_digitacao:
            for botao, _ in self.botoes_silabas:
                botao.desenhar(self.tela.janela)

    def exibir_letras(self):
        letras = self.compor_letras()
        acertou = ''.join(self.letras_digitadas).lower() == self.personagem.nome.lower()
        largura_total = sum(self.fonte.render(l, True, (0, 0, 0)).get_width() + 5 for l in letras)
        x = (self.tela.janela.get_width() - largura_total) // 2
        y = 415

        for letra in letras:
            cor = (0, 255, 255) if acertou else self.definir_cor(letra.lower())
            texto = self.fonte.render(letra, True, cor)
            for dx in [-1, 1]:
                for dy in [-1, 1]:
                    sombra = self.fonte.render(letra, True, (0, 0, 0))
                    self.tela.janela.blit(sombra, (x + dx, y + dy))
            self.tela.janela.blit(texto, (x, y))
            x += texto.get_width() + 5

    def compor_letras(self):
        nome = self.personagem.nome
        silaba = self.resposta_certa
        idx = nome.find(silaba)

        if self.fase_digitacao and idx != -1:
            prefixo = nome[:idx]
            sufixo = nome[idx + len(silaba):]
            letras_silaba = [l.upper() for l in self.letras_digitadas]
            letras_silaba += ["_"] * (len(silaba) - len(letras_silaba))
            return list(prefixo.upper()) + letras_silaba + list(sufixo.upper())
        else:
            return list(self.nome_oculto().upper())

    def nome_oculto(self):
        nome = self.personagem.nome
        silaba = self.personagem.silaba
        idx = nome.find(silaba)
        if idx != -1:
            if self.silaba_escolhida:
                return nome[:idx] + self.silaba_escolhida + nome[idx + len(silaba):]
            else:
                return nome[:idx] + "_" * len(silaba) + nome[idx + len(silaba):]
        return nome

    def definir_cor(self, letra):
        if letra in "aeiou":
            return (255, 165, 0)
        elif letra in "uh":
            return (255, 255, 0)
        return (0, 255, 0)

    def criar_efeito_firework(self, pos, duracao=60):
        self._criar_efeito_particulas(pos, duracao)

    def criar_efeito_explosao(self, pos, duracao=50):
        self._criar_efeito_particulas(pos, duracao)

    def criar_efeito_anel(self, pos, duracao=60):
        self._criar_efeito_particulas(pos, duracao)

    def _criar_efeito_particulas(self, pos, duracao):
        source = self.efeito_particulas.CreateSource(
            pos=pos,
            initspeed=4.0,
            initdirection=0.0,
            initspeedrandrange=2.0,
            initdirectionrandrange=6.28,
            particlesperframe=20,
            particlelife=duracao,
            drawtype=DRAWTYPE_CIRCLE,
            colour=(255, 200, 50),
            radius=4.0
        )
        for _ in range(3):
            source.Update()

        source.CreateParticleKeyframe(0, colour=(255, 200, 50), radius=4.0)
        source.CreateParticleKeyframe(30, colour=(255, 100, 0), radius=3.0)
        source.CreateParticleKeyframe(60, colour=(0, 0, 0), radius=0.0)
    
    def criar_efeito_fogo(self):
        centro = (560, 80)
        raio = 60
        for _ in range(20):
            angulo = random.uniform(0, 2 * math.pi)
            x = centro[0] + math.cos(angulo) * raio
            y = centro[1] + math.sin(angulo) * raio
            direcao = angulo

            source = self.efeito_particulas.CreateSource(
                pos=(x, y),
                initspeed=2.5,
                initdirection=direcao,
                initspeedrandrange=1.0,
                initdirectionrandrange=0.4,
                particlesperframe=2,
                particlelife=50,
                drawtype=DRAWTYPE_CIRCLE,
                colour=(255, 100, 0),
                radius=1.0
            )
            for _ in range(3):
                source.Update()

    def criar_efeito_neve(self):
        centro = (560, 80)
        raio = 60
        for _ in range(25):
            angulo = random.uniform(0, 2 * math.pi)
            x = centro[0] + math.cos(angulo) * raio
            y = centro[1] + math.sin(angulo) * raio
            direcao = angulo + math.pi

            source = self.efeito_particulas.CreateSource(
                pos=(x, y),
                initspeed=2.5,
                initdirection=direcao,
                initspeedrandrange=1.0,
                initdirectionrandrange=0.4,
                particlesperframe=1,
                particlelife=50,
                drawtype=DRAWTYPE_CIRCLE,
                colour=(180, 220, 255),
                radius=1.0
            )
            for _ in range(3):
                source.Update()

    def criar_efeito_luz(self):
        centro = (560, 80)
        raio = 60
        for _ in range(20):
            angulo = random.uniform(0, 2 * math.pi)
            x = centro[0] + math.cos(angulo) * raio
            y = centro[1] + math.sin(angulo) * raio
            direcao = angulo

            source = self.efeito_particulas.CreateSource(
                pos=(x, y),
                initspeed=0.4,
                initdirection=direcao,
                initspeedrandrange=0.2,
                initdirectionrandrange=0.2,
                particlesperframe=1,
                particlelife=50,
                drawtype=DRAWTYPE_CIRCLE,
                colour=(255, 255, 255),
                radius=2.0
            )
            for _ in range(3):
                source.Update()

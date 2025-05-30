import json
from pathlib import Path

class PontosGlobais:
    def __init__(self, arquivo="pontuacao.json"):
        self.arquivo = Path(arquivo)
        self.pontos = 0
        self.carregar()

    def salvar(self):
        dados = {"pontos": self.pontos}
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f)

    def carregar(self):
        if self.arquivo.exists():
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.pontos = dados.get("pontos", 0)
        else:
            self.pontos = 0

    def adicionar(self, valor):
        self.pontos += valor
        self.salvar()

pontuacao_global = PontosGlobais()
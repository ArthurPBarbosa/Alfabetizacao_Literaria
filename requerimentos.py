import subprocess
import sys
import os

def instalar(pacote):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
        print(f"{pacote} instalado com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Falha ao instalar {pacote}.")

def instalar_dependencias():
    pacotes = {
        "pygame": "pygame"
    }

    for nome_importacao, nome_pip in pacotes.items():
        try:
            __import__(nome_importacao)
            print(f"{nome_importacao} já está instalado.")
        except ImportError:
            print(f"{nome_importacao} não encontrado. Instalando {nome_pip}...")
            instalar(nome_pip)

    if not os.path.exists("nomes.py"):
        print("AVISO: O arquivo 'nomes.py' não foi encontrado no diretório atual.")
    else:
        print("'nomes.py' está presente.")

if __name__ == "__main__":
    instalar_dependencias()
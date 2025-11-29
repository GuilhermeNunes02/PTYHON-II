
from rich.console import Console
from rich.progress import track
import time

console = Console()

def progresso_leitura(texto: str, isArquivo: bool):
    if isArquivo:
        with open(texto) as f:
            linhas = f.readlines()
    else:
        linhas = texto.splitlines()
    for linha in track(linhas, description="Processando..."):
        time.sleep(0.1)
        console.print(linha)

def progresso_fake(texto: str, isArquivo: bool):
    for _ in track(range(20), description="Carregando..."):
        time.sleep(0.05)
    console.print(texto if not isArquivo else open(texto).read())

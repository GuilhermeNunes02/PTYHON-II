
from rich.console import Console
from rich.text import Text

console = Console()

def estilo_colorido(texto: str, isArquivo: bool):
    if isArquivo:
        with open(texto) as f:
            texto = f.read()
    t = Text(texto, style="bold magenta")
    console.print(t)

def estilo_arcoiris(texto: str, isArquivo: bool):
    if isArquivo:
        with open(texto) as f:
            texto = f.read()
    t = Text()
    cores = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    for i, char in enumerate(texto):
        t.append(char, style=cores[i % len(cores)])
    console.print(t)

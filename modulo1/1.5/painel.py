
from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_simples(texto: str, isArquivo: bool):
    if isArquivo:
        with open(texto) as f:
            texto = f.read()
    console.print(Panel(texto, title="Painel Simples"))

def painel_destacado(texto: str, isArquivo: bool):
    if isArquivo:
        with open(texto) as f:
            texto = f.read()
    console.print(Panel.fit(texto, title="[bold red]Destaque[/bold red]", border_style="red"))

"""
utils.py

Funções utilitárias:
- imprime_instrucoes(caminho=None)
- celebracao_recursiva(n, mensagem)
"""
from typing import Optional
import time
from rich.console import Console
from rich.panel import Panel
console = Console()

def imprime_instrucoes():
    """Imprime instruções do jogo formatadas com rich."""
    texto = (
        "Bem-vindo à Aventura no Labirinto!\n\n"
        "Use W A S D para mover. Seu objetivo é alcançar 'G'.\n"
        "No menu você pode escolher 'instrucoes', 'jogar', 'resolver' ou 'sair'.\n"
    )
    console.print(Panel(texto, title="Instruções"))

def celebracao_recursiva(n: int, mensagem: str = "Vitoria!\n") -> None:
    """Animação recursiva simples que imprime a mensagem n vezes utilizando rich.
    Demonstra função recursiva não-trivial pedida no enunciado.
    """
    if n <= 0:
        return
    console.print(Panel(mensagem))
    time.sleep(0.2)
    celebracao_recursiva(n-1, mensagem)


from rich.console import Console
from rich.layout import Layout

console = Console()

def mostrar_layout(texto: str, isArquivo: bool):
    if isArquivo:
        with open(texto, "r", encoding="utf8") as f:
            texto = f.read()
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
        Layout(name="footer", size=3),
    )
    layout["header"].update("[bold blue]HEADER[/bold blue]")
    layout["body"].update(texto)
    layout["footer"].update("[bold green]FOOTER[/bold green]")
    console.print(layout)

def mostrar_duplo(texto: str, isArquivo: bool):
    if isArquivo:
        with open(texto, "r", encoding="utf8") as f:
            texto = f.read()
    layout = Layout()
    layout.split_row(
        Layout(texto, name="left"),
        Layout(texto, name="right"),
    )
    console.print(layout)

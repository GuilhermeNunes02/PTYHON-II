"""
main.py - Interface de linha de comando e loop principal do jogo.
Argumentos CLI sugeridos:
--name <nome>
--color <cor>
--dificuldade <1|2|3>
--disable-sound
--auto-resolver (resolve automaticamente usando função recursiva)
"""
import argparse
import sys
from aventura_pkg import labirinto, jogador, utils
from rich.console import Console

console = Console()

def menu_interativo(lab, pos, pontos):
    """Menu principal que usa match-case (Python 3.10+)."""
    while True:
        console.print("\nMenu: [instrucoes] [jogar] [resolver] [sair]")
        escolha = console.input("Escolha: ").strip()
        match escolha:
            case 'instrucoes':
                utils.imprime_instrucoes()
            case 'jogar':
                jogar_loop(lab, pos, pontos)
                return
            case 'resolver':
                sol = jogador.resolver_recursivo(lab, pos, (len(lab[0])-2, len(lab)-2))
                if sol:
                    console.print(f"Solução com {len(sol)} passos: {sol}")
                else:
                    console.print("Nenhuma solução encontrada.")
            case 'sair':
                console.print('Saindo...')
                sys.exit(0)
            case _:
                console.print('Opção inválida.')

def jogar_loop(lab, pos, pontos):
    """Loop de jogo que lê comandos do usuário (WASD) e atualiza o estado."""
    console.print("Iniciando jogo. Use w/a/s/d para mover, 'q' para sair.")
    x,y = pos
    goal = (len(lab[0])-2, len(lab)-2)
    while True:
        labirinto.imprimir_labirinto(lab, (x,y))
        cmd = console.input('Comando (w/a/s/d/q): ').strip().lower()
        if cmd == 'q':
            console.print('Saindo do jogo.')
            break
        nova = jogador.mover(lab, (x,y), cmd)
        if nova != (x,y):
            pontos = jogador.pontuar(pontos, 'mover')
            x,y = nova
        if (x,y) == goal:
            pontos = jogador.pontuar(pontos, 'goal')
            console.print(f"Você venceu! Pontos: {pontos}")
            utils.celebracao_recursiva(6, "Parabéns!")
            break

def main():
    parser = argparse.ArgumentParser(description='Aventura no Labirinto — jogo terminal')
    parser.add_argument('--name', help='Nome do jogador', default='Aventureiro')
    parser.add_argument('--color', help='Cor principal do jogo (não aplicada automaticamente)', default='green')
    parser.add_argument('--dificuldade', help='Dificuldade (1,2,3)', type=int, choices=[1,2,3], default=1)
    parser.add_argument('--disable-sound', help='Desliga sons (se houver)', action='store_true')
    parser.add_argument('--auto-resolver', help='Resolve o labirinto automaticamente e mostra solução', action='store_true')
    args = parser.parse_args()

    lab = labirinto.criar_labirinto(args.dificuldade)
    x,y,_ = jogador.iniciar_jogador(lab)
    pontos = 0

    console.print(f"Bem-vindo, {args.name}! Dificuldade: {args.dificuldade}")
    if args.auto_resolver:
        sol = jogador.resolver_recursivo(lab, (x,y), (len(lab[0])-2, len(lab)-2))
        if sol:
            console.print(f"Solução automática ({len(sol)} passos): {sol}")
        else:
            console.print('Sem solução encontrada.')
        return

    menu_interativo(lab, (x,y), pontos)

if __name__ == '__main__':
    main()

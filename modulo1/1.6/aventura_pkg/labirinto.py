"""
labirinto.py

Funções:
- criar_labirinto(dificuldade: int) -> list[list[str]]
- imprimir_labirinto(lab: list[list[str]])
"""
from typing import List, Tuple
import random

WALL = "#"
SPACE = " "
PLAYER = "P"
GOAL = "G"

def criar_labirinto(dificuldade: int=1) -> List[List[str]]:
    """Gera um labirinto simples baseado na dificuldade.
    Dificuldade controla o tamanho (1: pequeno, 2: médio, 3: grande).
    Retorna uma matriz (lista de listas) com '#' para paredes e ' ' para caminhos.
    """
    size = {1:9, 2:13, 3:17}.get(dificuldade, 9)
    lab = [[WALL if x==0 or y==0 or x==size-1 or y==size-1 else SPACE for x in range(size)] for y in range(size)]
    # Colocar algumas paredes internas aleatórias
    for _ in range(size * 2):
        x = random.randint(1, size-2)
        y = random.randint(1, size-2)
        lab[y][x] = WALL if random.random() < 0.7 else SPACE
    # Garantir posição inicial e objetivo
    lab[1][1] = SPACE
    lab[size-2][size-2] = GOAL
    return lab

def imprimir_labirinto(lab: List[List[str]], pos: Tuple[int,int]=None) -> None:
    """Imprime o labirinto no terminal.
    Se pos for fornecida, desenha o jogador nessa posição (P).
    """
    for y, row in enumerate(lab):
        line = []
        for x, ch in enumerate(row):
            if pos and (x,y) == pos:
                line.append(PLAYER)
            else:
                line.append(ch)
        print("".join(line))

"""
jogador.py

Contém controle do jogador e pontuação.
Funções principais:
- iniciar_jogador(lab)
- mover(lab, pos, comando)
- pontuar(pontos, evento)
- resolver_recursivo(lab, start, goal) -> list[tuple]
"""
from typing import Tuple, List, Optional
import collections

def iniciar_jogador(lab: List[List[str]]) -> Tuple[int,int,int]:
    """Inicializa o jogador na posição (1,1) e pontuação zero.
    Retorna (x, y, pontos).
    """
    return 1, 1, 0

def _valido(lab: List[List[str]], x: int, y: int) -> bool:
    maxy = len(lab)-1
    maxx = len(lab[0])-1
    if x < 0 or y < 0 or x > maxx or y > maxy:
        return False
    return lab[y][x] != '#'

def mover(lab: List[List[str]], pos: Tuple[int,int], comando: str) -> Tuple[int,int]:
    """Move o jogador de acordo com o comando ('w','a','s','d')."""
    x,y = pos
    comando = comando.lower()
    if comando == 'w':
        nova = (x, y-1)
    elif comando == 's':
        nova = (x, y+1)
    elif comando == 'a':
        nova = (x-1, y)
    elif comando == 'd':
        nova = (x+1, y)
    else:
        nova = (x,y)
    if _valido(lab, *nova):
        return nova
    return (x,y)

def pontuar(pontos: int, evento: str) -> int:
    """Atualiza a pontuação baseada no evento (ex: 'mover','goal')."""
    if evento == 'mover':
        return pontos + 1
    if evento == 'goal':
        return pontos + 50
    return pontos

def resolver_recursivo(lab: List[List[str]], start: Tuple[int,int], goal: Tuple[int,int]) -> Optional[List[Tuple[int,int]]]:
    """Resolve o labirinto retornando uma lista de passos do start até o goal.
    Usa busca em profundidade recursiva (DFS). Retorna None se não achar.
    """
    visited = set()
    path = []

    def dfs(pos):
        if pos in visited:
            return False
        visited.add(pos)
        path.append(pos)
        if pos == goal:
            return True
        x,y = pos
        for dx,dy in [(0,-1),(1,0),(0,1),(-1,0)]:
            nx,ny = x+dx, y+dy
            if 0 <= ny < len(lab) and 0 <= nx < len(lab[0]) and lab[ny][nx] != '#':
                if dfs((nx,ny)):
                    return True
        path.pop()
        return False

    if dfs(start):
        return path.copy()
    return None

"""
aventura_pkg package - jogo Aventura no Labirinto.

Contém os módulos:
- labirinto: criação e impressão do labirinto
- jogador: controle do jogador e pontuação
- utils: utilitários e animações recursivas
"""
from .labirinto import criar_labirinto, imprimir_labirinto
from .jogador import iniciar_jogador, mover, pontuar, resolver_recursivo
from .utils import imprime_instrucoes, celebracao_recursiva

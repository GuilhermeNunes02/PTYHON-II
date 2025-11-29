
import argparse
import layout
import painel
import progresso
import estilo

MODULOS = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo,
}

def main():
    parser = argparse.ArgumentParser(description="Ferramenta de formatação com Rich")
    parser.add_argument("texto", help="Texto a ser exibido OU caminho para arquivo")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento é um arquivo")
    parser.add_argument("-m", "--modulo", choices=MODULOS.keys(), required=True, help="Escolha o módulo")
    parser.add_argument("-f", "--funcao", required=True, help="Função dentro do módulo")
    args = parser.parse_args()
    modulo = MODULOS[args.modulo]
    if not hasattr(modulo, args.funcao):
        raise ValueError(f"Função '{args.funcao}' não encontrada no módulo '{args.modulo}'")
    func = getattr(modulo, args.funcao)
    func(args.texto, args.arquivo)

if __name__ == "__main__":
    main()

# Aventura no Labirinto

Jogo terminal "Aventura no Labirinto".

## Como executar

1. Crie e ative um ambiente virtual:
```
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows
```

2. Instale dependências:
```
pip install -r requirements.txt
```

3. Execute:
```
python main.py --name "Seu Nome" --dificuldade 1
```

Use as opções `--auto-resolver` para ver a solução automática. O menu usa `match-case` (Python 3.10+).

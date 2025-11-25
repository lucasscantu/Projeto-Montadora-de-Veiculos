import json
import os

DB_PATH = "estoque.json"

def carregar_estoque():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r") as f:
        return json.load(f)

def salvar_estoque(veiculos):
    with open(DB_PATH, "w") as f:
        json.dump(veiculos, f, indent=4)

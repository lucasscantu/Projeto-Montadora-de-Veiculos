import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from models.montadora import Montadora

def mostrar_estoque():
    montadora = Montadora()

    print("\n=== ESTOQUE ATUAL ===")
    if not montadora.veiculos:
        print("Nenhum veículo no estoque.")
        return

    for v in montadora.veiculos:
        v.exibir_detalhes()

if __name__ == "__main__":
    mostrar_estoque()

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from models.montadora import Montadora
from models.observer import VendasObserver, QualidadeObserver, EstoqueObserver


if __name__ == "__main__":
    montadora = Montadora()

    montadora.register_observer(VendasObserver())
    montadora.register_observer(QualidadeObserver())
    montadora.register_observer(EstoqueObserver())

    print("=== TESTE DE PRODUÇÃO ===\n")

    montadora.produzir_veiculo("carro", "Toyota Corolla", 2025, 125000, tipo_carro="sedan")
    montadora.produzir_veiculo("moto", "Honda Pop 110i", 2025, 12000, cilindradas=110)
    montadora.produzir_veiculo("caminhao", "VW Delivery", 2025, 280000, capacidade_carga=12)

    montadora.listar_veiculos()

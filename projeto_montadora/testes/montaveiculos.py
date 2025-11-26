import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from models.montadora import Montadora
from models.observer import VendasObserver, QualidadeObserver, EstoqueObserver

if __name__ == "__main__":
    montadora = Montadora()

    montadora.register_observer(VendasObserver())
    montadora.register_observer(QualidadeObserver())
    montadora.register_observer(EstoqueObserver())

    montadora.produzir_veiculo("carro", "Toyota Corolla", 2025, 125000, tipo_carro="sedan")
    montadora.produzir_veiculo("carro", "Volkswagen Gol", 2025, 78000, tipo_carro="hatch")
    montadora.produzir_veiculo("moto", "Honda Pop 110i", 2025, 12000, cilindradas=110)

    montadora.listar_veiculos()

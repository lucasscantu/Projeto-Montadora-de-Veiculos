import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from models.montadora import Montadora
from models.observer import VendasObserver, QualidadeObserver, EstoqueObserver
from models.vendas import SistemaVendas

if __name__ == "__main__":
    # Criar a montadora
    montadora = Montadora()

    # Registrar observers
    montadora.register_observer(VendasObserver())
    montadora.register_observer(QualidadeObserver())
    montadora.register_observer(EstoqueObserver())

    print("\n=== PRODUZINDO VEÍCULOS ===\n")
    montadora.produzir_veiculo("carro", "Toyota Corolla", 2025, 125000, tipo_carro="sedan")
    montadora.produzir_veiculo("carro", "Volkswagen Gol", 2025, 78000, tipo_carro="hatch")
    montadora.produzir_veiculo("moto", "Honda Pop 110i", 2025, 12000, cilindradas=110)

    print("\n=== ESTOQUE ATUAL ===\n")
    montadora.listar_veiculos()

    # Sistema de vendas
    sistema = SistemaVendas(montadora)

    print("\n=== REALIZANDO VENDAS ===\n")
    sistema.vender_veiculo("Toyota Corolla")
    sistema.vender_veiculo("Honda Pop 110i")

    print("\n=== RELATÓRIO DE VENDAS ===\n")
    sistema.exibir_relatorio()

    print("\n=== ESTOQUE APÓS AS VENDAS ===\n")
    montadora.listar_veiculos()

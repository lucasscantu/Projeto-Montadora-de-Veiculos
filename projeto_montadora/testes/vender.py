from models.montadora import Montadora
from models.vendas import SistemaVendas

if __name__ == "__main__":
    montadora = Montadora()
    sistema = SistemaVendas(montadora)

    sistema.vender_veiculo("Toyota Corolla")
    sistema.vender_veiculo("Volkswagen Gol")

    sistema.exibir_relatorio()

    print("\n=== ESTOQUE APÓS VENDAS ===")
    montadora.listar_veiculos()

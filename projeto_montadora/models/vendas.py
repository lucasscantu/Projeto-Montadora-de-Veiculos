from models.montadora import Montadora
from models.estoque import salvar_estoque

class SistemaVendas:
    def __init__(self, montadora: Montadora):
        self.montadora = montadora
        self.receita_total = 0.0
        self.vendidos = []

    def vender_veiculo(self, modelo: str) -> bool:
        for v in self.montadora.veiculos:
            if v.modelo.lower() == modelo.lower():
                preco = v.calcular_preco_final()
                self.receita_total += preco
                self.vendidos.append(v)

                # Remove do estoque
                self.montadora.veiculos.remove(v)

                # 🔥 IMPORTANTE: salva o novo estoque no JSON
                self.montadora._salvar_dados()

                print(f"\n🚗 Veículo vendido: {v}")
                print(f"💰 Receita gerada: R$ {preco:,.2f}")
                return True

        print(f"\n❌ Veículo '{modelo}' não encontrado no estoque.")
        return False

    def exibir_relatorio(self):
        print("\n=== RELATÓRIO DE VENDAS ===")
        print(f"Total arrecadado: R$ {self.receita_total:,.2f}")
        print(f"Veículos vendidos: {len(self.vendidos)}")

        for v in self.vendidos:
            print(f"- {v.modelo} ({v.ano})")

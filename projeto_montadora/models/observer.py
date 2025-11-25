from abc import ABC, abstractmethod
from models.veiculo import Veiculo

class Observer(ABC):
    @abstractmethod
    def update(self, veiculo: Veiculo) -> None:
        pass

class VendasObserver(Observer):
    def update(self, veiculo: Veiculo) -> None:
        print(f"DEPARTAMENTO DE VENDAS → Novo veículo pronto: {veiculo} | "
              f"Valor de venda: R$ {veiculo.calcular_preco_final():,.2f}")

class QualidadeObserver(Observer):
    def update(self, veiculo: Veiculo) -> None:
        print(f"CONTROLE DE QUALIDADE → Veículo {veiculo} encaminhado para inspeção final.")

class EstoqueObserver(Observer):
    def update(self, veiculo: Veiculo) -> None:
        print(f"ESTOQUE → {veiculo} adicionado ao pátio.")

from models.veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, modelo: str, ano: int, preco_base: float, capacidade_carga: float):
        super().__init__(modelo, ano, preco_base)
        self._capacidade_carga = capacidade_carga

    def exibir_detalhes(self) -> None:
        print(f"Caminhão: {self.modelo} ({self.ano}) | {self._capacidade_carga}t | Preço final: R$ {self.calcular_preco_final():,.2f}")

    def calcular_preco_final(self) -> float:
        base = self._preco_base
        if self._capacidade_carga <= 20:
            return base + (self._capacidade_carga * 12_000)
        elif self._capacidade_carga <= 40:
            return base + (self._capacidade_carga * 15_000)
        else:
            return base + (self._capacidade_carga * 18_000)

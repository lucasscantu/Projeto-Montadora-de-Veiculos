from models.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo: str, ano: int, preco_base: float, cilindradas: int):
        super().__init__(modelo, ano, preco_base)
        self._cilindradas = cilindradas

    def exibir_detalhes(self) -> None:
        print(f"Moto: {self.modelo} ({self.ano}) | {self._cilindradas}cc | Preço final: R$ {self.calcular_preco_final():,.2f}")

    def calcular_preco_final(self) -> float:
        base = self._preco_base
        if self._cilindradas <= 300:
            return base * 1.08
        elif self._cilindradas <= 600:
            return base * 1.15
        else:
            return base * 1.25

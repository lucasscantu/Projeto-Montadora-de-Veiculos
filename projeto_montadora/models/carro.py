from models.veiculo import Veiculo
from enum import Enum

class TipoCarro(str, Enum):
    SEDAN = "sedan"
    HATCH = "hatch"
    PICKUP = "pickup"

class Carro(Veiculo):
    def __init__(self, modelo: str, ano: int, preco_base: float, tipo: TipoCarro):
        super().__init__(modelo, ano, preco_base)
        self._tipo = tipo

    @property
    def tipo(self) -> TipoCarro:
        return self._tipo

    def exibir_detalhes(self) -> None:
        tipo_formatado = self._tipo.value.upper()
        print(f"Carro {tipo_formatado}: {self.modelo} ({self.ano}) | Preço final: R$ {self.calcular_preco_final():,.2f}")

    def calcular_preco_final(self) -> float:
        base = self._preco_base
        if self._tipo == TipoCarro.PICKUP:
            return base * 1.35
        elif self._tipo == TipoCarro.SEDAN:
            return base * 1.28
        else:
            return base * 1.20

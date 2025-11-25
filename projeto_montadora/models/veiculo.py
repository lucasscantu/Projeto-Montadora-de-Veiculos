from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo: str, ano: int, preco_base: float):
        self._modelo = modelo
        self._ano = ano
        self._preco_base = preco_base

    @property
    def modelo(self) -> str:
        return self._modelo

    @property
    def ano(self) -> int:
        return self._ano

    @abstractmethod
    def exibir_detalhes(self) -> None:
        pass

    @abstractmethod
    def calcular_preco_final(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self._modelo} ({self._ano})"

from models.veiculo import Veiculo
from models.carro import Carro, TipoCarro
from models.caminhao import Caminhao
from models.moto import Moto

class VeiculoFactory:
    @staticmethod
    def criar_veiculo(tipo: str, modelo: str, ano: int, preco_base: float, **kwargs) -> Veiculo:
        tipo = tipo.lower()

        if tipo == "carro":
            tipo_carro = kwargs.get("tipo_carro", "hatch")
            return Carro(
                modelo=modelo,
                ano=ano,
                preco_base=preco_base,
                tipo=TipoCarro(tipo_carro)
            )

        elif tipo == "caminhao":
            return Caminhao(modelo, ano, preco_base, kwargs.get("capacidade_carga", 20))

        elif tipo == "moto":
            return Moto(modelo, ano, preco_base, kwargs.get("cilindradas", 250))

        else:
            raise ValueError(f"Tipo de veículo desconhecido: {tipo}")

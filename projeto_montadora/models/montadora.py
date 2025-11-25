from typing import List
from models.veiculo import Veiculo
from models.observer import Observer
from models.factory import VeiculoFactory
from models.estoque import carregar_estoque, salvar_estoque

class Montadora:
    def __init__(self):
        self.veiculos: List[Veiculo] = []
        self.observers: List[Observer] = []
        self._carregar_dados()

    def _carregar_dados(self):
        dados = carregar_estoque()
        for d in dados:
            v = VeiculoFactory.criar_veiculo(**d)
            self.veiculos.append(v)

    def _salvar_dados(self):
        dados = []
        for v in self.veiculos:
            dados.append({
                "tipo": v.__class__.__name__.replace("Carro", "carro").lower().replace("moto", "moto").replace("caminhao", "caminhao"),
                "modelo": v.modelo,
                "ano": v.ano,
                "preco_base": v._preco_base,
                "tipo_carro": getattr(v, "_tipo", None).value if hasattr(v, "_tipo") else None,
                "cilindradas": getattr(v, "_cilindradas", None),
                "capacidade_carga": getattr(v, "_capacidade_carga", None)
            })
        salvar_estoque(dados)

    def register_observer(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def notify_observers(self, veiculo: Veiculo):
        for observer in self.observers:
            observer.update(veiculo)

    def produzir_veiculo(self, tipo: str, modelo: str, ano: int, preco_base: float, **kwargs) -> Veiculo:
        dados = {"tipo": tipo, "modelo": modelo, "ano": ano, "preco_base": preco_base, **kwargs}
        veiculo = VeiculoFactory.criar_veiculo(**dados)

        self.veiculos.append(veiculo)
        self._salvar_dados()

        print(f"Veículo {modelo} montado com sucesso!")
        self.notify_observers(veiculo)
        return veiculo

    def listar_veiculos(self):
        print("\n=== VEÍCULOS NO ESTOQUE ===")
        for v in self.veiculos:
            v.exibir_detalhes()

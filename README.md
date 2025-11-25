# 🚗 Sistema de Montadora — UML, Factory, Observer e Modelos de Veículos

Este repositório contém o diagrama UML completo representando a arquitetura de um sistema de produção de veículos utilizando:

✔ Herança e Polimorfismo  
✔ Enum para controle de tipos  
✔ Factory Pattern (criação centralizada de veículos)  
✔ Observer Pattern (departamentos notificados)  
✔ Camadas de Vendas e Estoque  

---

## 📐 Diagrama UML (PlantUML)

```plantuml
@startuml
skinparam monochrome true
skinparam shadowing false
skinparam classAttributeIconSize 0
skinparam nodesep 70
skinparam ranksep 90
skinparam dpi 300

enum TipoCarro {
  SEDAN
  HATCH
  PICKUP
}

abstract class Veiculo {
  -_modelo : str
  -_ano : int
  -_preco_base : float
  --
  +modelo : str <<property>>
  +ano : int <<property>>
  +{abstract} exibir_detalhes() : void
  +{abstract} calcular_preco_final() : float
  +__str__() : str
}

class Carro {
  -_tipo : TipoCarro
  --
  +tipo : TipoCarro <<property>>
  +exibir_detalhes() : void
  +calcular_preco_final() : float
}

class Moto {
  -_cilindradas : int
  --
  +exibir_detalhes() : void
  +calcular_preco_final() : float
}

class Caminhao {
  -_capacidade_carga : float
  --
  +exibir_detalhes() : void
  +calcular_preco_final() : float
}

Veiculo <|-- Carro
Veiculo <|-- Moto
Veiculo <|-- Caminhao
Carro o--> TipoCarro

class VeiculoFactory {
  {static} +criar_veiculo(tipo: str, modelo: str, ano: int, preco_base: float, **kwargs) : Veiculo
}

VeiculoFactory ..> Carro : <<create>>
VeiculoFactory ..> Moto : <<create>>
VeiculoFactory ..> Caminhao : <<create>>

interface Observer {
  +update(veiculo : Veiculo) : void
}

class VendasObserver {
  +update(veiculo : Veiculo) : void
}

class EstoqueObserver {
  +update(veiculo : Veiculo) : void
}

class QualidadeObserver {
  +update(veiculo : Veiculo) : void
}

Observer <|.. VendasObserver
Observer <|.. EstoqueObserver
Observer <|.. QualidadeObserver

class Montadora {
  -_veiculos : List<Veiculo>
  -_observers : List<Observer>
  -_estoque : dict
  -_vendas : List<Veiculo>
  --
  +register_observer(observer : Observer)
  +notify_observers(veiculo : Veiculo)
  +produzir_veiculo(...)
  +listar_veiculos()
  +mostrar_estoque()
  +mostrar_vendas()
}

Montadora o--> "0..*" Veiculo
Montadora o--> "0..*" Observer
Montadora ..> VeiculoFactory

note right of Montadora::notify_observers
  Quando um veículo é produzido,
  todos os departamentos são notificados.
  → Padrão Observer
end note

note right of VeiculoFactory
  Criação centralizada dos veículos
  → Padrão Factory
end note

@enduml

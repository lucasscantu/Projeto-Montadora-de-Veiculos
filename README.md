# 🚗 Sistema de Montadora — UML, Factory, Observer e Modelos de Veículos

Este repositório contém o diagrama UML completo representando a arquitetura de um sistema de produção de veículos utilizando:

✔ Herança e Polimorfismo  
✔ Enum para controle de tipos  
✔ Factory Pattern (criação centralizada de veículos)  
✔ Observer Pattern (departamentos notificados)  
✔ Camadas de Vendas e Estoque  

---

## 🏗️ Estrutura e Aplicação do Factory Method

O padrão Factory Method é utilizado para isolar a lógica de criação de objetos (`Veiculo`) do código que os utiliza. Isso garante que o sistema siga o Princípio da Aberto/Fechado (OCP), sendo **aberto para extensão** (novos veículos) e **fechado para modificação** (lógica de montagem existente).



| Componente (Padrão) | Classe/Interface (Projeto) | Papel no Projeto |
| :--- | :--- | :--- |
| **Produto** | `Veiculo` (Classe Abstrata) | Define a interface comum para todos os veículos que podem ser produzidos. |
| **Produtos Concretos** | `Carro`, `Moto`, `Caminhao` | Implementações específicas do Produto. |
| **Criador** | `Montadora` (Classe Abstrata) | Declara o **Factory Method** (`criarVeiculo`), mas não implementa a lógica de criação específica. |
| **Criadores Concretos** | `MontadoraCarro`, `MontadoraMoto`, `MontadoraCaminhao` | Subclasses que implementam o Factory Method para instanciar e retornar um tipo específico de `Veiculo` (Produto Concreto). |

---

## 📐 Diagrama UML (PlantUML)

![Diagrama UML](./projeto_montadora/diagrama.jpg)

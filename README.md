# 💰 Sistema Bancário em Python com POO

Este projeto é uma simulação aprimorada de um sistema bancário, operado via console e desenvolvido inteiramente em Python. A principal evolução desta versão é a refatoração do código para uma arquitetura robusta baseada em **Programação Orientada a Objetos (POO)**.

Essa mudança permite modelar entidades do mundo real (como Clientes, Contas e Transações) de forma intuitiva e coesa, resultando em um código mais limpo, modular, reutilizável e escalável.

## ✨ Funcionalidades Principais

| Categoria | Funcionalidade | Descrição |
| :--- | :--- | :--- |
| **Operações Financeiras** | **Depósito** | Permite adicionar um valor ao saldo da conta, registrando a operação no histórico. |
| | **Saque** | Realiza um saque com limite de 3 operações diárias e um valor máximo de R$ 500,00 por transação. O sistema valida o saldo antes de aprovar. |
| | **Transferência** | Permite transferir valores de uma conta para outra, validando o saldo disponível na conta de origem e registrando a transação em ambas. |
| | **Extrato** | Exibe um resumo de todas as movimentações (depósitos, saques e transferências) e o saldo atual da conta. |
| **Gerenciamento** | **Novo Usuário** | Cadastra um novo cliente (Pessoa Física) com nome, CPF, data de nascimento e endereço, validando se o CPF já existe. |
| | **Nova Conta** | Cria uma nova conta corrente e a vincula a um usuário já cadastrado. O sistema impede que um mesmo cliente crie mais de uma conta. |
| | **Listar Contas** | Exibe todas as contas criadas, mostrando a agência, o número da conta e o nome do titular. |

## 🏛️ Arquitetura e Conceitos de POO Aplicados

O projeto foi estruturado para aplicar os pilares fundamentais da Programação Orientada a Objetos:

* ### Herança
    A classe `ContaCorrente` herda de `Conta`, e `PessoaFisica` herda de `Cliente`. Isso permite o reaproveitamento de código e a criação de uma hierarquia lógica entre as classes.

* ### Encapsulamento
    Atributos como `_saldo` e `_numero` são protegidos. O acesso a eles é controlado por meio de `properties` (`@property`), garantindo que o estado dos objetos seja consistente e seguro.

* ### Polimorfismo
    O método `sacar()` é um exemplo claro: ele possui uma implementação base na classe `Conta` e é sobrescrito na classe `ContaCorrente` para adicionar regras de negócio específicas (validação de limite e número de saques).

* ### Abstração
    A classe `Transacao` é uma Classe Base Abstrata (ABC) que define um "contrato" para todas as transações do sistema (`Saque`, `Deposito`, `Transferencia`), forçando-as a implementar os métodos `valor` e `registrar`.

## 🚀 Como Executar

1.  Certifique-se de ter o **Python 3** instalado em sua máquina.
2.  Clone este repositório ou baixe os arquivos do projeto.
3.  Abra o terminal na pasta do projeto e execute o arquivo principal:
    ```bash
    python nome_do_seu_arquivo.py
    ```
4.  Siga as instruções apresentadas no menu do console para interagir com o sistema.

## 🔧 Tecnologias Utilizadas

* **Python 3**
* **Biblioteca Padrão do Python:**
    * `datetime` para registrar a data e hora das transações.
    * `abc` para a criação de classes abstratas.
    * `textwrap` para formatação do menu de texto.

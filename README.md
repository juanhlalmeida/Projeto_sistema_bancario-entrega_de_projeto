# 💰 Sistema Bancário em Python UPDATE!!!

Este projeto é uma simulação de um sistema bancário em console, desenvolvido em Python. Ele foi criado para aplicar conceitos de programação estruturada, como funções e o uso de diferentes tipos de argumentos (`positional-only` e `keyword-only`), tornando o código modular, organizado e de fácil manutenção.

---

### 🧠 Funcionalidades e Operações

| Categoria | Funcionalidade | Descrição |
| :--- | :--- | :--- |
| **Operações Financeiras** | Depósito | Permite adicionar um valor ao saldo da conta, registrando a operação no extrato. |
| | Saque | Realiza um saque, com um limite de até 3 saques diários e um valor máximo de R$ 500,00 por saque. O sistema verifica o saldo disponível antes de aprovar a transação. |
| | Extrato | Exibe um resumo de todas as movimentações (depósitos e saques) e o saldo atual da conta. |
| **Gerenciamento de Clientes e Contas** | Novo Usuário | Cadastra um novo cliente com informações como nome, CPF, data de nascimento e endereço. O sistema valida se o CPF já existe. |
| | Buscar Usuário | Permite pesquisar e exibir os dados de um cliente existente a partir de seu CPF. |
| | Nova Conta | Cria uma nova conta corrente e a vincula a um usuário já cadastrado. As contas são sequenciais e a agência é fixa. |
| | Listar Contas | Exibe todas as contas criadas, mostrando a agência, o número da conta e o nome do titular. |

---

### 📋 Regras de Negócio e Melhorias

O sistema agora gerencia **múltiplos usuários e contas de forma independente**, indo além da limitação de um único cliente.

* **Modularidade:** O código foi refatorado para utilizar funções com diferentes tipos de argumentos, o que melhora a legibilidade e a estrutura do projeto.
* **Validação de Dados:** As entradas de CPF são limpas automaticamente, removendo caracteres não numéricos, o que garante a consistência no armazenamento e na busca de dados.
* **Loop de Menu:** O menu principal opera em um loop contínuo, permitindo ao usuário realizar várias operações até que a opção de sair seja selecionada.

---

### 🖥️ Como Executar

Certifique-se de ter o **Python 3** instalado em sua máquina. Para rodar o sistema, basta executar o arquivo `main.py` (ou o nome do seu arquivo principal) no terminal.

```bash
python main.py

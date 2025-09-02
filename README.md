# 💰 Sistema Bancário em Python

Este projeto é uma simulação simples de um sistema bancário desenvolvido em Python, com funcionalidades básicas de **depósito**, **saque** e **extrato**. Ele foi criado como parte de um desafio para aplicar lógica de programação e boas práticas em Python.

---

## 🧠 Funcionalidades

### 1. Depósito
- Permite ao usuário depositar valores **positivos**.
- O valor é somado ao saldo da conta.
- Cada depósito é registrado no **extrato**.

### 2. Saque
- Permite até **3 saques por dia**.
- Cada saque tem um **limite máximo de R$ 500,00**.
- O sistema verifica se há **saldo suficiente** antes de autorizar o saque.
- Saques são registrados no **extrato**.
- Se o valor for maior que o saldo, o sistema exibe a mensagem: `"Saldo insuficiente."`

### 3. Extrato
- Exibe todos os **depósitos e saques realizados**.
- Mostra o **saldo atual** da conta.
- Os valores são formatados no padrão monetário brasileiro: `R$ xxx.xx`.

---

## 📋 Regras de Negócio

- O sistema trabalha com **apenas um usuário** (não há identificação de agência ou número de conta).
- Todas as movimentações são armazenadas em variáveis locais.
- O menu é interativo e funciona em loop até que o usuário escolha a opção de sair.

---

## 🖥️ Como Executar

1. Certifique-se de ter o **Python 3 instalado** em sua máquina.

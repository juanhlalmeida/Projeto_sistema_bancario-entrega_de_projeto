# Menu de operações bancárias
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

# Inicializando as variáveis principais
saldo = 0.0  # Saldo inicial da conta
limite = 500.0  # Limite máximo por saque
extrato = ""  # Histórico de movimentações
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Máximo de saques permitidos por dia

# Loop principal do sistema bancário
while True:
    opcao = input(menu)  # Exibe o menu e aguarda a escolha do usuário

    # Operação de depósito
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor  # Atualiza o saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra no extrato
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Operação de saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        # Verificações antes de permitir o saque
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor excede o limite por saque.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor  # Atualiza o saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra no extrato
            numero_saques += 1  # Atualiza o contador de saques
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Operação de extrato
    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==============================")

    # Encerrar o sistema
    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema bancário. Até logo!")
        break

    # Caso o usuário digite uma opção inválida
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
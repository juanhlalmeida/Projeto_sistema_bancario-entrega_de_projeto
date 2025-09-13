# Importa a biblioteca textwrap, que ajuda a formatar textos.
# Usaremos a função 'dedent' para remover espaços em branco do início de linhas em strings de múltiplas linhas.
import textwrap


# Bloco de Funções do Sistema
# Organizar o código em funções o torna mais legível, reutilizável e fácil de dar manutenção.

def menu():
    """
    Esta função exibe o menu de opções para o usuário e captura a escolha dele.
    Ela não recebe nenhum argumento e retorna a opção digitada pelo usuário.
    """
    # A string de múltiplas linhas (com três aspas) permite criar o menu de forma visualmente organizada.
    menu_texto = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo Usuário
    [bu]\tBuscar Usuário
    [nc]\tNova Conta
    [lc]\tListar Contas
    [q]\tSair
    => """
    # A função textwrap.dedent() remove o espaçamento inicial comum de cada linha do menu.
    # A função input() exibe o menu para o usuário e espera que ele digite algo.
    return input(textwrap.dedent(menu_texto))


def depositar(saldo, valor, extrato, /):
    """
    Função para realizar depósitos.
    Ela recebe os argumentos apenas por posição (positional-only), graças à '/' no final.
    Isso significa que você deve chamá-la assim: depositar(100, 50, "extrato") e não depositar(saldo=100, ...).
    """
    # Verifica se o valor do depósito é positivo.
    if valor > 0:
        # Se for positivo, adiciona o valor ao saldo.
        saldo += valor
        # Adiciona uma nova linha ao extrato, formatando o valor com duas casas decimais.
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        # Se o valor for zero ou negativo, informa uma falha na operação.
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # Retorna o novo saldo e o extrato atualizado.
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Função para realizar saques.
    Ela recebe os argumentos apenas por nome (keyword-only), graças ao '*' no início.
    Isso significa que você deve chamá-la assim: sacar(saldo=100, valor=50, ...).
    """
    # Cria variáveis booleanas para verificar cada uma das regras de saque.
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    # Inicia a verificação das regras.
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    # Verifica se o valor de saque é positivo.
    elif valor > 0:
        # Se todas as regras foram atendidas, subtrai o valor do saldo.
        saldo -= valor
        # Adiciona o saque ao extrato.
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        # Incrementa o contador de saques realizados.
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        # Se o valor informado for inválido (negativo ou zero).
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # AJUSTE FEITO AQUI: Retorna o número de saques atualizado junto com o saldo e extrato.
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    """
    Função para exibir o extrato bancário.
    Recebe 'saldo' por posição e 'extrato' por nome, graças à combinação de '/' e '*'.
    """
    print("\n================ EXTRATO ================")
    # Operador ternário: exibe uma mensagem se o extrato estiver vazio, caso contrário, exibe o extrato.
    print("Não foram realizadas movimentações." if not extrato else extrato)
    # Exibe o saldo atual formatado.
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    """
    Função para cadastrar um novo usuário (cliente).
    """
    cpf = input("Informe o CPF (somente número): ")
    # AJUSTE FEITO AQUI: Limpa o CPF para garantir que apenas dígitos sejam salvos.
    cpf = "".join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF informado já existe na lista de usuários.
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return # 'return' encerra a execução da função aqui.

    # Se o CPF não existe, pede o resto dos dados.
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Adiciona o novo usuário (um dicionário) à lista de usuários.
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    """
    Função auxiliar para buscar um usuário na lista pelo CPF.
    """
    # List comprehension: uma forma concisa de criar uma lista.
    # Aqui, ela cria uma lista com todos os usuários que têm o CPF correspondente.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    # Retorna o primeiro usuário encontrado na lista filtrada, ou 'None' se a lista estiver vazia.
    return usuarios_filtrados[0] if usuarios_filtrados else None


def buscar_usuario_por_cpf(usuarios):
    """
    NOVA FUNÇÃO: Permite buscar e exibir os dados de um usuário pelo CPF.
    """
    cpf = input("Informe o CPF do usuário que deseja buscar: ")
    # Limpa o CPF para garantir uma busca correta.
    cpf = "".join(filter(str.isdigit, cpf))

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Dados do Usuário ---")
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Data de Nascimento: {usuario['data_nascimento']}")
        print(f"Endereço: {usuario['endereco']}")
        print("------------------------")
    else:
        print("\n@@@ Usuário não encontrado! @@@")


def criar_conta(agencia, numero_conta, usuarios):
    """
    Função para criar uma nova conta corrente, vinculando-a a um usuário.
    """
    cpf = input("Informe o CPF do usuário para vincular a conta: ")
    cpf = "".join(filter(str.isdigit, cpf))

    # Busca o usuário pelo CPF.
    usuario = filtrar_usuario(cpf, usuarios)

    # Se o usuário for encontrado, cria a conta.
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        # Retorna um dicionário representando a nova conta.
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    # Se o usuário não for encontrado, exibe uma mensagem de erro.
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    # Retorna None, indicando que a conta não foi criada.
    return None


def listar_contas(contas):
    """
    Função para exibir todas as contas correntes cadastradas.
    """
    # Se não houver contas, exibe uma mensagem e encerra.
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return

    # 'for' é um laço de repetição. Ele vai "passar por" cada item da lista 'contas'.
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    """
    Função principal que executa o programa.
    Ela gerencia o loop do menu e armazena as variáveis principais.
    """
    # Constantes: valores que não mudam durante a execução.
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    # Variáveis: valores que podem mudar.
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    # 'while True' cria um laço infinito. O programa ficará rodando aqui
    # até que encontre um comando 'break'.
    while True:
        # Chama a função menu() e armazena a escolha do usuário na variável 'opcao'.
        opcao = menu()

        # Estrutura de decisão: o programa verifica o valor de 'opcao' e executa o bloco correspondente.
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            # Chama a função depositar e atualiza as variáveis 'saldo' e 'extrato' com os valores retornados.
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            # Chama a função sacar, passando todos os argumentos necessários por nome (keyword).
            # AJUSTE FEITO AQUI: Atualiza também a variável 'numero_saques' com o retorno da função.
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            # Chama a função para exibir o extrato.
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            # Chama a função para criar um novo usuário, passando a lista de usuários.
            criar_usuario(usuarios)

        elif opcao == "bu": # NOVA OPÇÃO
            # Chama a nova função para buscar um usuário.
            buscar_usuario_por_cpf(usuarios)

        elif opcao == "nc":
            # Gera um novo número de conta sequencial.
            numero_conta = len(contas) + 1
            # Chama a função para criar uma nova conta.
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            # Se a função criar_conta retornou uma conta (e não 'None'), adiciona à lista.
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            # Chama a função para listar todas as contas.
            listar_contas(contas)

        elif opcao == "q":
            # Se a opção for 'q', o comando 'break' interrompe o laço 'while True' e encerra o programa.
            break

        else:
            # Se o usuário digitar qualquer outra coisa, exibe uma mensagem de erro.
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# Esta linha executa a função 'main' quando o script Python é iniciado.
main()

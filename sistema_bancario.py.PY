# Importa módulos necessários para o projeto
import textwrap
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime


# Classe que representa um Cliente do banco
class Cliente:
    # Método construtor da classe Cliente
    def __init__(self, endereco):
        self.endereco = endereco  # Atributo para armazenar o endereço do cliente
        self.contas = []  # Lista para armazenar as contas associadas a este cliente

    # Método para realizar uma transação em uma conta específica
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)  # Chama o método que registra a transação na conta

    # Método para adicionar uma nova conta à lista de contas do cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)


# Classe que herda de Cliente e representa uma Pessoa Física
class PessoaFisica(Cliente):
    # Método construtor da classe PessoaFisica
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)  # Chama o construtor da classe pai (Cliente)
        self.nome = nome  # Atributo para o nome do cliente
        self.data_nascimento = data_nascimento  # Atributo para a data de nascimento
        self.cpf = cpf  # Atributo para o CPF do cliente


# Classe base para todas as contas bancárias
class Conta:
    # Método construtor da classe Conta
    def __init__(self, numero, cliente):
        self._saldo = 0  # Saldo inicial da conta (privado)
        self._numero = numero  # Número da conta (privado)
        self._agencia = "0001"  # Número da agência (padrão e privado)
        self._cliente = cliente  # Cliente associado a esta conta (privado)
        self._historico = Historico()  # Objeto para registrar o histórico de transações (privado)

    # Método de classe para criar uma nova instância de conta
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)  # Retorna uma nova instância da classe Conta

    # Property para acessar o saldo de forma segura
    @property
    def saldo(self):
        return self._saldo

    # Property para acessar o número da conta
    @property
    def numero(self):
        return self._numero

    # Property para acessar o número da agência
    @property
    def agencia(self):
        return self._agencia

    # Property para acessar o objeto cliente
    @property
    def cliente(self):
        return self._cliente

    # Property para acessar o histórico de transações
    @property
    def historico(self):
        return self._historico

    # Método para realizar um saque
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque é maior que o saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > 0:
            self._saldo -= valor  # Subtrai o valor do saldo
            print("\n=== Saque realizado com sucesso! ===")
            return True  # Retorna True se o saque foi bem-sucedido
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False  # Retorna False se a operação falhou

    # Método para realizar um depósito
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor  # Adiciona o valor ao saldo
            print("\n=== Depósito realizado com sucesso! ===")
            return True  # Retorna True se o depósito foi bem-sucedido
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False  # Retorna False se a operação falhou


# Classe que herda de Conta e representa uma Conta Corrente
class ContaCorrente(Conta):
    # Método construtor da classe ContaCorrente
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)  # Chama o construtor da classe pai (Conta)
        self._limite = limite  # Limite de valor por saque
        self._limite_saques = limite_saques  # Limite diário de saques

    # Sobrescreve o método sacar para adicionar regras específicas da conta corrente
    def sacar(self, valor):
        # Conta o número de saques já realizados no histórico
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite  # Verifica se o valor excede o limite por saque
        excedeu_saques = numero_saques >= self._limite_saques  # Verifica se o número de saques foi excedido

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite de R$ 500,00. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques diários (3) excedido. @@@")
        else:
            return super().sacar(valor)  # Se tudo estiver ok, chama o método sacar da classe pai

        return False  # Retorna False se a operação falhou

    # Método para retornar uma representação em string do objeto ContaCorrente
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


# Classe para gerenciar o histórico de transações de uma conta
class Historico:
    # Método construtor da classe Historico
    def __init__(self):
        self._transacoes = []  # Lista para armazenar as transações

    # Property para acessar a lista de transações
    @property
    def transacoes(self):
        return self._transacoes

    # Método para adicionar uma nova transação ao histórico
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,  # Nome da classe da transação (Saque, Deposito)
                "valor": transacao.valor,  # Valor da transação
                # AQUI ESTÁ A CORREÇÃO: %S (maiúsculo) para segundos
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


# Classe abstrata para representar uma Transação
class Transacao(ABC):
    # Property abstrata para o valor da transação
    @property
    @abstractmethod
    def valor(self):
        pass

    # Método de classe abstrato para registrar a transação
    @abstractmethod
    def registrar(self, conta):
        pass


# Classe para representar a transação de Saque
class Saque(Transacao):
    # Método construtor
    def __init__(self, valor):
        self._valor = valor

    # Implementação da property valor
    @property
    def valor(self):
        return self._valor

    # Implementação do método registrar
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)  # Tenta realizar o saque na conta

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona ao histórico se o saque for bem-sucedido


# Classe para representar a transação de Depósito
class Deposito(Transacao):
    # Método construtor
    def __init__(self, valor):
        self._valor = valor

    # Implementação da property valor
    @property
    def valor(self):
        return self._valor

    # Implementação do método registrar
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)  # Tenta realizar o depósito na conta

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona ao histórico se o depósito for bem-sucedido

# --- NOVIDADE: Classe para representar a transação de Transferência ---
class Transferencia(Transacao):
    def __init__(self, valor, conta_destino):
        self._valor = valor
        self._conta_destino = conta_destino

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta_origem):
        # Tenta sacar da conta de origem
        if conta_origem.sacar(self.valor):
            # Se o saque for bem-sucedido, deposita na conta de destino
            self._conta_destino.depositar(self.valor)
            # Adiciona a transação ao histórico de ambas as contas
            conta_origem.historico.adicionar_transacao(self)
            # Para o extrato da conta destino, criamos um "depósito por transferência"
            deposito_transferencia = Deposito(self.valor)
            self._conta_destino.historico.adicionar_transacao(deposito_transferencia)
            print("\n=== Transferência realizada com sucesso! ===")
            return True
        
        print("\n@@@ Falha na transferência! Saldo insuficiente na conta de origem. @@@")
        return False

# Função para exibir o menu principal e capturar a escolha do usuário
def menu():
    menu_texto = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [t]\tTransferir
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_texto))


# Função para encontrar um cliente pelo CPF na lista de clientes
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

# Função para buscar uma conta pelo seu número
def buscar_conta_por_numero(numero_conta, contas):
    contas_encontradas = [conta for conta in contas if conta.numero == numero_conta]
    return contas_encontradas[0] if contas_encontradas else None

# Função para recuperar a conta de um cliente
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None

    # Lógica simplificada: retorna a primeira conta do cliente.
    return cliente.contas[0]


# Função para orquestrar a operação de depósito
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    try:
        valor = float(input("Informe o valor do depósito: "))
        transacao = Deposito(valor)
    except ValueError:
        print("\n@@@ Valor inválido! Por favor, insira um número. @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


# Função para orquestrar a operação de saque
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    try:
        valor = float(input("Informe o valor do saque: "))
        transacao = Saque(valor)
    except ValueError:
        print("\n@@@ Valor inválido! Por favor, insira um número. @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

# --- NOVIDADE: Função para orquestrar a operação de transferência ---
def transferir(clientes, contas):
    # Solicita CPF da conta de origem
    cpf_origem = input("Informe o CPF do cliente de origem: ")
    cliente_origem = filtrar_cliente(cpf_origem, clientes)

    if not cliente_origem:
        print("\n@@@ Cliente de origem não encontrado! @@@")
        return

    conta_origem = recuperar_conta_cliente(cliente_origem)
    if not conta_origem:
        return

    # Solicita dados da conta de destino
    try:
        numero_conta_destino = int(input("Informe o número da conta de destino: "))
        conta_destino = buscar_conta_por_numero(numero_conta_destino, contas)
    except ValueError:
        print("\n@@@ Número da conta inválido! Por favor, insira apenas números. @@@")
        return

    if not conta_destino:
        print("\n@@@ Conta de destino não encontrada! @@@")
        return

    # Verifica se a conta de origem e destino não são a mesma
    if conta_origem.numero == conta_destino.numero:
        print("\n@@@ Operação falhou! A conta de origem e destino não podem ser a mesma. @@@")
        return

    # Solicita o valor
    try:
        valor = float(input("Informe o valor a ser transferido: "))
        if valor <= 0:
            print("\n@@@ O valor da transferência deve ser positivo. @@@")
            return
    except ValueError:
        print("\n@@@ Valor inválido! Por favor, insira um número. @@@")
        return
        
    # Cria e registra a transação
    transacao = Transferencia(valor, conta_destino)
    cliente_origem.realizar_transacao(conta_origem, transacao)


# Função para exibir o extrato de uma conta
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            tipo_transacao = transacao['tipo']
            if tipo_transacao == 'Transferencia':
                tipo_transacao = "Transferência Enviada"
            
            extrato += f"\n{transacao['data']} - {tipo_transacao}:\n\tR$ {transacao['valor']:.2f}"


    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


# Função para criar um novo cliente (Pessoa Física)
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


# --- OTIMIZAÇÃO: Função de criar conta aprimorada ---
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    if any(isinstance(conta, ContaCorrente) for conta in cliente.contas):
        print("\n@@@ Este cliente já possui uma conta corrente! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("\n=== Conta criada com sucesso! ===")


# Função para listar todas as contas criadas no sistema
def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return
        
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


# Função principal que executa o programa
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "t":
            transferir(clientes, contas)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema! Saindo...")
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


# Ponto de entrada do script
main()

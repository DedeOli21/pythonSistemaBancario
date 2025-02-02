menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, extrato
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"

def sacar(valor):
    global saldo, extrato, numero_saques
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

def imprimir_extrato():
    global saldo, extrato
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==================================")

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)
        print(f"Deposito realizado! Saldo atual:: R$ {saldo:.2f}")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)
        print(f"\nsaque realizado! Saldo atual: R$ {saldo:.2f}")
    elif opcao == "e":
        imprimir_extrato()
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

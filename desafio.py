from datetime import datetime

# Estado da conta
saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def agora_str():
    return datetime.now().strftime("%d/%m/%Y - %H:%M")

def mostrar_pagina_inicial():
    return (
        "     Marcelo's bank company\n"
        "        Inicio (1)\n"
        "        Créditos (2)\n"
        "        Sair (q)\n"
        "=> "
    )

def mostrar_creditos():
    print(
        "\nCódigo e Design por Marcelo Perotta Campello\n"
        "Obrigado por utilizar o Marcelo's bank company!\n"
    )

def menu_banco():
    return (
        "\n[ d ] Depositar\n"
        "[ s ] Sacar\n"
        "[ e ] Extrato\n"
        "[ q ] Voltar\n"
        "=> "
    )

def Depositar(saldo, extrato):
    try:
        valor = float(input("Digite o valor do depósito: ").replace(",", "."))
    except ValueError:
        print("Valor inválido.")
        return saldo, extrato

    if valor <= 0:
        print("Valor deve ser positivo.")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito de R$ {valor:.2f} em {agora_str()}\n"
    print("Depósito realizado com sucesso.")
    return saldo, extrato

def Sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques diários atingido.")
        return saldo, extrato, numero_saques

    try:
        saque = float(input("Digite o valor do saque: ").replace(",", "."))
    except ValueError:
        print("Valor inválido.")
        return saldo, extrato, numero_saques

    if saque <= 0:
        print("Valor deve ser positivo.")
        return saldo, extrato, numero_saques

    if saque > limite:
        print(f"Valor acima do limite por saque (R$ {limite:.2f}).")
        return saldo, extrato, numero_saques

    if saque > saldo:
        print("Saldo insuficiente.")
        return saldo, extrato, numero_saques

    saldo -= saque
    numero_saques += 1
    extrato += f"Saque de R$ {saque:.2f} em {agora_str()}\n"
    print("Saque realizado com sucesso.")
    return saldo, extrato, numero_saques

# Loop da página inicial
while True:
    opc = input(mostrar_pagina_inicial()).strip().lower()

    if opc == "1":  # entrar no menu do banco
        while True:
            escolha = input(menu_banco()).strip().lower()

            if escolha == "d":
                saldo, extrato = Depositar(saldo, extrato)

            elif escolha == "s":
                saldo, extrato, numero_saques = Sacar(
                    saldo, extrato, numero_saques, LIMITE_SAQUES, limite
                )

            elif escolha == "e":
                print("\n=== Extrato ===")
                print(extrato if extrato else "Sem movimentações.")
                print(f"Saldo atual: R$ {saldo:.2f}")
                print(f"Saques hoje: {numero_saques}/{LIMITE_SAQUES}")

            elif escolha == "q":
                break

            else:
                print("Opção inválida.")

    elif opc == "2":  # créditos
        mostrar_creditos()

    elif opc == "q":  # sair do programa
        print("Encerrando. Até mais!")
        break

    else:
        print("Opção inválida.")

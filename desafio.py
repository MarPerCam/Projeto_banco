from datetime import datetime

agora = datetime.now()
horas = agora.strftime("%H:%M")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>"""
print(menu
      )

saldo = 0
limite= 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depositar")
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor 
        print("Depósito realizado com sucesso")
        
        extrato += (f"Depósito no valor de R$ {valor} {horas}\n")


    elif opcao == "s":
        print("Sacar")
        
        saque = float(input("Digite o valor do saque: "))
        

        if saldo < saque:
            print ("saldo insuficiente")
        
        elif saque < 0 :

            print("saque invalido")

        elif saldo < saque:
            print ("saldo insuficiente")


        elif LIMITE_SAQUES > 0 :
           
            if saque <= limite and saldo >= saque :
                saldo -= saque
                
               


                LIMITE_SAQUES -= 1
                numero_saques += 1

                print("saque realizado com sucesso")

                extrato += (f"Saque no valor de R$ {saque} foi efetuado {horas}\n")



            elif saque > limite:

                print("valor acima do limite")
            
            else:
                print ("Limite de saques atingido")
            
    
    
    elif opcao == "e":
        print("Extrato")
        print(f"Seu saldo atual é de R$ {saldo}")

        print(extrato)
        




    elif opcao == "q":
        break

    else:
        print("Opção inválida")





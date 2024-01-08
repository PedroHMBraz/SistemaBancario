### 3 operações ### Depósito, saque e extrato ###


saldo = 0
quantidade_saque = 0
extrato = f"""
### Extrato ###
"""
menu = f"""
    ======= MENU =======
    d -- Depositar
    s -- Sacar
    e -- Extrato
    q -- Sair
    ====================
"""
print(menu)
opcao = str(input("Digite a letra correspondente a operação desejada: "))

###  Depósito ###
### Deve ser possível depositar valores positivos. Inicialmente, trabalhamos apenas com um usuário
### então não precisamos de identificador como o número de agência e conta bancária.
### Todo depósito deve ser salvo em uma variável e aparecer no extrato


### Saque ###
### O sistema deve permitir no máximo 3 saques diários com limite de R$500,00 por saque

### Extrato ###
### Deve listar todos os depósitos e saques realizados. No fim deve-se mostrar o saldo.


while opcao != 0:  
    if opcao == "d":
        deposito = float(input("Digite o valor de seu depósito: "))
        if deposito > 0:
            print(f"O depósito realizado foi de R$ {deposito}.")
            saldo = saldo + deposito
            print(f"Seu novo saldo é de R$ {saldo}.")
            extrato = extrato + f"Depósito: R$ {deposito:.2f}\n"
        else:
            print(f"Valor digitado de R$ {deposito} é inválido!\nTente novamente.")        
    elif opcao == "s":
        if quantidade_saque < 3:
            saque = float(input("Digite o valor do saque: "))
            if saque > 0 and saque <= 500:
                if saque <= saldo:
                    saldo = saldo - saque
                    print(f"Seu novo saldo é de R$ {saldo}.")
                    quantidade_saque += 1
                    extrato = extrato + f"Saque: R$ {saque:.2f}\n"
                else: 
                    print("Saldo insuficiente\nVerifique seu saldo e tente novamente.")
            else:
                print(f"Valor digitado de R$ {saque} é inválido!\nVerifique o valor digitado.")  
        else: 
            print("Limite de saques diários atingido.")
    elif opcao == "e":
        print(f"Seu extrato é: {extrato}\n")
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Opção desconhecida. Tente novamente!")
    opcao = str(input("Digite a letra correspondente a operação desejada: "))

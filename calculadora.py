import math
operacao = int(input("Calculadora Uninove - Para seguir, informe a operação desejada: \n 1. Adição \n 2. Subtração \n 3. Multiplicação \n 4. Divisão(Resto de Divisão) \n 5. Divisão \n 6. Raíz Quadrada \n 7. Exponenciação \n"))

if operacao >= 1 and operacao <=7:
    
    match operacao:
        case 1:
            num1 = float(input("Digite o primeiro número para realizar a soma:"))
            num2 = float(input("Digite o segundo número para realizar a soma:"))

            soma = num1 + num2
            print("O resultado da soma é: ", soma)
        
        case 2:
            num1 = float(input("Digite o primeiro número para realizar a subtração:"))
            num2 = float(input("Digite o segundo número para realizar a subtração:"))

            subtracao = num1 - num2
            print("O resultado da subtração é: ", subtracao)
        
        case 3:
            num1 = float(input("Digite o primeiro número para realizar a multiplicação:"))
            num2 = float(input("Digite o segundo número para realizar a multiplicação:"))

            multiplicacao = num1 * num2
            print("O resultado da multiplicacao é: ", multiplicacao)

        case 4:
            num1 = float(input("Digite o primeiro número para realizar a divisão (Resto de Divisão):"))
            num2 = float(input("Digite o segundo número para realizar a divisão (Resto de Divisão):"))

            restoDiv = num1 % num2
            print("O resto da divisão é: ", restoDiv)
        
        case 5:
            num1 = float(input("Digite o primeiro número para realizar a divisão:"))
            num2 = float(input("Digite o segundo número para realizar a divisão:"))

            divisao = num1 / num2
            print("O resultado da divisão é: ", divisao)

        case 6:
            num1 = float(input("Digite o número para realizar a raíz quadrada:"))

            raiz = math.sqrt(num1)
            print("A raiz quadrada de ", num1," é: ", raiz)

        case 7:
            num1 = float(input("Digite o número da base da potenciação:"))
            num2 = float(input("Digite o número do expoente :"))

            potencia = num1 ** num2
            print("O resultado da exponenciação é: ", potencia)
else:
    print("Dados Inconsistentes!")
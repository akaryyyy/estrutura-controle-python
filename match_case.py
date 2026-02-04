# Calculadora simples
# String = "texto"
#  int = 10, 20
# float 12.12, 13.13
# boolean = true or false

'''
Qual é a lógica da calculadora?

Precisa de valores (números)

    1. Entrada: 
1. O usuário precisa digitar dois números ou +
2. O usuário precisa falar qual operação math ele vai usar

    2. Processamento:
Realizar as operações matemáticas (+, -, * e /)

    3. Output
Exibir o resultado da operação realizada    
'''

print("Bem vindo a calculadora do Senac")
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
operador = input("Digite o operador: ")

match operador: 
  case "+":
    print("O resultado é: ", primeiro_numero + segundo_numero)
  case "-":
    print("O Resultado é: ", primeiro_numero - segundo_numero)
  case "*":
    print("O Resultado é: ", primeiro_numero * segundo_numero)
  case "/":
    if segundo_numero == 0:
      print("!!! Isso aqui não pode !!!")
    else:   
      print("O Resultado é: ", primeiro_numero / segundo_numero)   
  case _:
    print("Operação Inválida!")  

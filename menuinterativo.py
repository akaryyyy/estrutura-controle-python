print('''   

Menu de atendimento do Senac      

[1] Falar com atendente
[2] Segunda via de boleto
[3] Cancelar serviço
[4] Informações sobre planos
[5] Sair

'''
)

opcao_que_deseja = input("Digite a opção desejada: ")

match opcao_que_deseja:
    case "1" | "Falar com atendente":
        print("Você está em contato com o atendente")

    case "2" | "Segunda via de boleto":
        print("Você está na segunda via de boleto")

    case "3" | "Cancelar serviço":
        print("Você está no cancelamento de serviço")

    case "4" | "Informações sobre planos":
        print("Você está nos informativos de planos")

    case "5" | "Sair":
        print("Você saiu")

    case _:
        print("Opção inválida, insira um número conforme as opções")
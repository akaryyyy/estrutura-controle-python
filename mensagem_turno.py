print("\n Seja bem vindo a central do Senac, por favor prossiga em...\n ")

nome_usuario = input("Digite o seu nome: ")
periodo_curso = input("Digite o seu período: ")

match periodo_curso:
    case "M" | "Manhã":
        print("Bom dia, caro aluno", nome_usuario, "e tenha boas aulas!") 
    case "T" | "Tarde":
        print("Boa tarde, caro aluno", nome_usuario, "e tenha boas aulas!")
    case "N" |  "Noite":
        print("Boa noite, caro aluno", nome_usuario, "e tenha boas aulas!")
    case _:
        print("Selecione o período, caro aluno", nome_usuario)                             
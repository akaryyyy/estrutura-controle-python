print("\nBem vindo ao jogo super hiper mega legal\n")

# 1. Definir XP e nome para o jogador
xp = int(input(" ⭐ Quantos pontos de expêriencia (XP) você tem? ⭐\n"
               "Digite aqui: "))

nome_personagem = input("Digite seu nome: ")

# 2. Classificação do jogador
if xp < 100:
    nivel = "Noob"
elif xp <= 500:
    nivel = "Pro"
else:
    nivel = "Hacker"

print(f"Seu nome é {nome_personagem} e seu nível é {nivel}")     


# 3. Ação do jogador
acao = input(
    "\nEscolha uma ação:\n"
    "A - Atacar\n"
    "D - Defender\n" \
    "F - Fugir\n"
    "Digite sua escolha: "
). upper()

# 4. Resultado das ações
match acao:
    case "A":
        print(f"{nome_personagem} avançou para o ataque! 🤺")
    case "D":
        print(f"{nome_personagem} levantou o escudo! 🛡️")
    case "F":
        print(f"{nome_personagem} fugiu da batalha, seu cagão! 🏃‍♂️‍➡️")
    case _:
        print("Digite uma opção válida.")            

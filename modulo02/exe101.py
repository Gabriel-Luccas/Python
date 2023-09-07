#def função pra verificar idade pra voto 

def idade_voto(idade): 
    if idade > 18:
        return print(f"Com a idade de {idade} voto obrigatorio ")
    elif idade < 18:
        return print(f"COm a idade de {idade} Não pode votar ")
    else:
        return print(f"Com a idade de {idade} voto opcional ")


def linha():
    print("=" * 50)


linha()
print("Veja se Pode Votar ! ")
idade = int(input("Digite sua idade: "))
idade_voto(idade)

lista_pessoas = [{"nome": "Gabriel", "idade": 20}]
lista = [
    "Mostrar Pessoas Cadastradas",
    "Cadastrar novas pessoas",
    "Mostrar Arquivo geral",
    "Sair",
]

arq = "Curso em video.txt"


def Menu(lista):
    print("==" * 50)
    print("Menu de opçoes")
    print("--" * 50)
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print("==" * 50)


# Define a function to validate a name input
def get_valid_name_input():
    while True:
        nome = input("Nome: ")
        if (
            nome.strip() != "" and nome.isalpha()
        ):  # Check if it's not empty and contains only alphabetic characters
            return nome
        else:
            print("Nome inválido. Digite um nome válido.")


def get_valid_age_input():
    while True:
        try:
            idade = int(input("Idade: "))
            if idade >= 1:  # Check if age is a non-negative integer
                return idade
            else:
                print("Idade inválida. Digite uma idade válida.")
        except ValueError:
            print(
                "Idade inválida. Digite uma idade válida (número inteiro não negativo)."
            )


def opcao():
    global lista_pessoas, lista
    while True:
        Menu(lista)
        try:
            escolha = int(input("Sua opção: "))
            if escolha == 1:
                print("Pessoas Cadastradas")
                for pessoa in lista_pessoas:
                    print(f"{pessoa['nome']}  {pessoa['idade']} anos")
            elif escolha == 2:
                try:
                    nome = get_valid_name_input()
                    idade = get_valid_age_input()
                    nova_pessoa = {"nome": nome, "idade": idade}
                    lista_pessoas.append(nova_pessoa)
                    with open(arq, "at") as file:
                        file.write(f"{nome} - {idade} anos\n")
                except:
                    None
            elif escolha == 3:
                from pacote115.arquivo import leararquivo

                leararquivo(arq)
            elif escolha == 4:
                print("encerrando")
                exit()
            else:
                print("Opção não está no menu")
        except ValueError:
            print("ERRO: Opção inválida (digite um número).")

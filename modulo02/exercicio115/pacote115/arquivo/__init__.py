def arqExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, "wt+")
        a.close
    except:
        print("error")
    else:
        print("Arquivo {nome} criado com sucesso")


def leararquivo(nome):
    try:
        with open(nome, "rt") as file:
            print("PESSOAS CADASTRADAS NO ARQUIVO GERAL")
            for line in file.readlines():
                print(line.strip())
    except FileNotFoundError:
        print(f"Arquivo '{nome}' não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

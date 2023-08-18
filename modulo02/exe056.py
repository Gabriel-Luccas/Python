# Receba nome,idade e sexo de 4 pessoas ;
idades = []
m_20 = 0
for c in range(4):
    nome = str(input("Qual seu nome ? "))
    idade = int(input("Qual sua idade ? "))
    idades.append(idade)
    sexo = str(input("Qual seu sexo coloque f ou m : "))
    if sexo == "f" and idade <= 20:
        m_20 += 1
media_idade = sum(idades) / 4
if max(idades):
    print(f" {max(idades)} Vocé é o mais velho")
print(
    f"A media das idade das pessoas é {media_idade:.0f} e tem {m_20} mulheres com menos de 20 anos "
)

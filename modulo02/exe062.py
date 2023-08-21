#Pa em while 
razão=int(input("Digite a razão da PA: "))
inicio=int(input("Digite o Inicio da PA: "))
termo_especifico=int(input("Até qual termo vai a PA: "))
termo = inicio + (termo_especifico - 1 ) * razão 
while inicio <= termo:
    print(inicio)
    inicio += razão

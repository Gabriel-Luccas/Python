palavra01 = str(input("Digite uma palavra: "))
palavra02 = str(input("Digite uma palavra: "))
palavra03 = str(input("Digite uma palavra: "))
palavra04 = str(input("Digite uma palavra: "))
palavra05 = str(input("Digite uma palavra: "))
palavras = (palavra01, palavra02, palavra03, palavra04, palavra05)
for p in palavras:
    print(f"\n Na palavra {p.upper()} temos ", end="")
    for letra in p:
      if letra in "aeiou":
        print(f"{letra}", end="")

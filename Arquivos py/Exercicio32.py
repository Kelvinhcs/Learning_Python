from datetime import date
ano = int(input("Digite um Ano(0 para o ano atual): "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} É bissexto")
else:
    print(f"O ano {ano} Não é bissexto")
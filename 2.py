contador = 0
pergunta1 = str(input('Telefonou para a vítima? S/N'))
pergunta2 = str(input('Estave no local do crime? S/N'))
pergunta3 = str(input('Devia para a vitima? S/N'))
pergunta4 = str(input('Já trabalhou com a vitima? S/N'))
pergunta6 = str(input('MOra perto da vítima? S/N'))
contador += 1
for contador in range [1, 6]:
    print(f'A quantidade de respostas positivas é {contador}')
    if contador == 2:
        print('SUSPEITA')
    elif contador == 3 and contador == 4:
        print('CÚMPLICE')
    elif contador == 5:
        print('ASSASSINO')
    else:
        print('INOCENTE')
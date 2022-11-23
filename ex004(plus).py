q1 = input('Digite algo, meu nobre guerreiro: ')
if q1.isalpha():
    print('Isso é uma musica?')
elif q1.isnumeric():
    print('Não gosto de matemática')
elif q1.islower():
    print('Fale mais alto, porfavor')
elif q1.isupper():
    print('Fale baixo, porfavor')
elif q1.title():
    print('Vejo que você fala bem')
else:
    print('Isso é um', type)

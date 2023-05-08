# Programa para calcular o peso ideal de homem e mulher 

nome = input('Qual o seu nome? ')
altura = input('Qual a sua altura? ')
float_altura = float(altura)
sexo = input('Digite "H" se você for homem e "M" se você for mulher: ').upper()

if sexo == 'H':
    peso_ideal_H = (72.7 * float_altura) - 58
    print(nome, 'o seu peso ideal é: ', peso_ideal_H, 'Kg')
elif sexo == 'M':
    peso_ideal_M = (62.1 * float_altura) - 44.7
    print(nome, 'o seu peso ideal é: ', peso_ideal_M, 'Kg')
else:
    print('Você não escolheu nenhuma das alternativas.')

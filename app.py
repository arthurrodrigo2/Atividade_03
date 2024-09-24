'''
Crie um programa que controle a entrada de usuários no brinquedo "Trem fastasma" de um Parque de 
diversões. O programa só deve autorizar a entrada de usuários que possuam mais de 10 anos de idade
e menos de 150 kg de peso.
Ao terminar, envie para o GitHub.
'''

# Criando as variáveis
idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso em Kg: "))

# Entrada de dados
if idade >= 10 and peso < 150:
    print("Bem-vindo ao Trem Fantasma, você cumpriu com todos os requisitos necessários!")
else:
    print("Infelizmente você não cumpriu com todos os requisitos, pois sua idade é {} e seu peso é {}kg.\n Lamentamos, mas é para a sua segurança.".format(idade,peso))

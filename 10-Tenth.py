print('{:#^50}'.format(' Lista de Exercícios 5 - Final '))
def error():
    print('{:-^50}'.format(' Error no sistema, comando não reconhecido '))
    exit()

def question(q):
    ini = '{:-^50}'.format(f'Questão {q}')
    print('\n\n',ini,'\n\n')
question(1)
# Faça um Programa em Python que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo.
# b) a soma do tripo do primeiro com o terceiro
# c) o terceiro elevado ao cubo
try:
    q1num1 = float(input('> Digite um valor inteiro para o número A\n> '))
    while (q1num1*2)%2 > 0:
        print('\n- Número inválido.')
        q1num1 = float(input('> Digite um valor inteiro para o número A\n> '))
    q1num2 = float(input('> Digite um valor inteiro para o número B\n> '))
    while (q1num2*2)%2 > 0:
        print('\n- Número inválido.')
        q1num2 = float(input('> Digite um valor inteiro para o número B\n> '))
    q1num3 = float(input('> Digite um valor inteiro para o número C\n> '))
except:
    error()
q1calc1 = (2*q1num1)*(q1num2/2)
q1calc2 = 3*q1calc1+q1num3
q1calc3 = q1num3**3
print(f'\n- O produto do dobro do primeiro com metade do segundo é: {q1calc1}.\n- A soma do tripo do primeiro com o terceiro é: {q1calc2}.\n- O terceiro elvado ao cubo é: {q1calc3}.')
question(2)
q2exc = 50
q2preco = 4
try:
    q2peixe = float(input('\n- Qual o peso do peixe em KG? '))
except:
    error()
if q2peixe <= q2exc:
    print('\n- Seu peixe não excedeu o limite!')
elif q2peixe > q2exc:
    print('\n- Seu peixe excedeu o peso permitido! (50 KG)')
    q2excesso = q2peixe - q2exc
    q2multa = q2excesso * q2preco
    print(f'- Peso excedido: {q2excesso} KG\n- Valor a pagar: {q2multa} R$')
question(3)
try:
    q3arquivo = float(input('- Digite o tamanho do arquivo (MB): '))
    q3link = float(input('- Digite a velocidade de download (Mb) de sua internet: '))
except:
    error()
q3velocidades = q3arquivo / (q3link / 8)
q3velocidadem = q3velocidades / 60
print(f'\n- Este arquivo de {q3arquivo} MB será baixado em {q3velocidades} segundos ou {q3velocidadem} minutos em uma internet de {q3link} Mb.')
question(4)
try:
    q4tempf = float(input('- Digite a temperatura em Fahrenheit: '))
except:
    error()
q4tempc = 5 * ((q4tempf-32)/9)
print(f'- A temperatura de {q4tempf} F em Celcius é {q4tempc} °C.')
question(5)
try:
    q5altura = float(input('- Digite a sua altura (M): '))
except:
    error()
q5ideal = (72.7*q5altura)-58
print(f'-O peso ideal para a altura de {q5altura} M é de {q5ideal} KG')
print('\n\n\nFim...')
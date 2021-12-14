# 13.12.21 - Correção de Lista 3 e 4
from ctypes import string_at


try:
    distancia = int(input('Digite a distância percorrida: '))
    tempo = float(input('Digita o tempo gasto:'))
    velocidade = distancia / tempo
except:
    exit(print('Error'))
if velocidade <= 100:
    print("Carro devagar!")
elif velocidade > 100 and velocidade <= 140:
    print("Carro com velocidade mediana")
elif velocidade > 140:
    print("Carro com alta velocidade")
else:
    print("Error XD")
    # and = as duas(ou mais) verdadeiras
    # or = só uma verdadeiras

L1 = int(input('Digite a L1(Lembre-se que L1 vale 5 pontos): \n'))
L2 = int(input('Digite a L2(Lembre-se que L2 vale 5 pontos): \n'))
N1 = L1 + L2

P1 = int(input('Digite a P1(Lembre-se que P1 vale 4 pontos): \n'))
L3 = int(input('Digite a L3(Lembre-se que L3 vale 3 pontos): \n'))
L4 = int(input('Digite a L4(Lembre-se que L4 vale 3 pontos): \n'))
N2 = P1 + L3 + L4

P2 = int(input('Digite a L3(Lembre-se que P2 vale 5 pontos): \n'))
L5 = int(input('Digite a L4(Lembre-se que L5 vale 5 pontos): \n'))
N3 = P2 + L5

P3 = int(input('Digite a L3(Lembre-se que P2 vale 4 pontos): \n'))
L6 = int(input('Digite a L6(Lembre-se que L6 vale 3 pontos): \n'))
L7 = int(input('Digite a L7(Lembre-se que L7 vale 3 pontos): \n'))
N4 = P3 + L6 + L7

media_final = ((N1 + N2 + N3 + N4)/4)

if media_final <= 4:
    print("Reporovado! Cumbo na asa!")
elif media_final > 4 and media_final < 7:
    print("Recuperação!")
elif media_final >= 7:
    print("Aprovado! Férias!")
else:
    print("Erro no sistema")


i=(float(input('diga i')))
a=(float(input('diaga a')))
b=(float(input('diaga b')))
c=(float(input('diaga c')))

if i >= 0:
    if i % 2 == 0:
        media_aritmetica = (a + b + c)/3
        print(media_aritmetica)
    elif i%2 != 0 :
        print('o número nao e par :(')
    else:
        print('erro no sistema')
    if i> 10:
        media_ponderada=(2*a+3*b+4*c)/9
        print(media_ponderada)
    else:
        print('erro no sistrma')
else:
    print('erro')
print('Lista de exercícios 02 - 16/11/2021')
# 1. Faça um programa que o usuário entre com o valor da distância percorrida por um carro em
# quilômetros e o tempo que ele levou para percorrer essa distância em horas. Encontre a
# velocidade média e a aceleração média. Lembrem-se V = d/t e A = V/t.
print('\n\t### Questão 01 ###')
dist=float(input('\n\n> Digite o valor da distância percorrida(KM): '))
tempo=float(input('\n> Digite o tempo que levou para percorrer(Hora): '))
vmedia=dist/tempo
print('\n- Velocidade média do veículo: {0} K/h'.format(vmedia))
amedia=vmedia/tempo
print(f'\n- Aceleração média do veículo: {amedia} K/h²')
# 2. Faça um programa que o usuário entre com os valores de notas de um aluno de acordo com a
# tabela a seguir e no final possa apresentar a média final do aluno.
print('\n\t### Questão 02 ###')
L1=float(input('\n\n> Nota da Lista 01:'))
L2=float(input('\n> Nota da Lista 02:'))
L3=float(input('\n> Nota da Lista 03:'))
L4=float(input('\n> Nota da Lista 04:'))
L5=float(input('\n> Nota da Lista 05:'))
L6=float(input('\n> Nota da Lista 06:'))
L7=float(input('\n> Nota da Lista 07:'))
P1=float(input('\n> Nota da Prova 01:'))
P2=float(input('\n> Nota da Prova 02:'))
P3=float(input('\n> Nota da Prova 03:'))
N1=((L1+L2)/2)
N2=((P1+L3+L4)/3)
N3=((P2+L5)/2)
N4=((P3+L6+L7)/3)
Nff=((N1+N2+N3+N4)/4)
if N1>10:
    N1=10
if N2>10:
    N2=10
if N3>10:
    N3=10
if N4>10:
    N4=10
if Nff>10:
    Nff=10
print(f'\n- Nota 01: {N1}\n- Nota 02: {N2}\n- Nota 03: {N3}\n- Nota 04: {N4}\n- Nota final: {Nff}')
# 3. Faça um programa que usuário entre com o valor de um salário de um colaborador e
# que o programa apresente o salário desse colaborador depois de descontado 15% de
# imposto e 10% de INSS (aposentadoria).
print('\n\t### Questão 03 ###')
salario=int(input('\n\n> Insira o salário do colaborador (R$): '))
print('\n- Salário Bruto: {0} R$'.format(salario))
imposto=salario*0.15
print(f'- Sálario depois de aplicado o imposto: {salario-imposto} R$\n- Retirado(imposto)(15%): {imposto}')
inss=salario*0.1
print(f'- Sálario depois de aplicado o INSS: {salario-inss} R$\n- Retirado(INSS)(10%): {inss}')
print('- Salário final: {0}'.format(salario-(imposto+inss)))
# 4. Faça um programa que receba do usuário um valor em metros e forneça o mesmo valor
# em quilômetros, centímetros e milímetros.
print('\n\t### Questão 04 ###')
metros=float(input('\n\nQuantos metros você deseja converter?\n> '))
km=metros/1000
print('\nQuilômetros: {0}'.format(float(km)))
print('Metros: {0}'.format(float(metros)))
cm=metros*100
print('Centímetros: {0}'.format(float(cm)))
ml=metros*1000
print('Milímetros: {0}'.format(float(ml)))
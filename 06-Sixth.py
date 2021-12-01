# lista de exercicios 03 - 29.11.2021
# 1. Faça um programa que o usuário entre com o valor da distância percorrida por um carro em quilômetros
# e o tempo que ele levou para percorrer essa distância em horas. Encontre a velocidade média. Lembrem-se
# V = d/t. Se o valor da velocidade for menor que 100 km/h, print na tela "Carro devagar", se for entre
# 100 e 140 km/h, print "Carro com velocidade mediana", se for maior que 140 km/h, "Carro com alta velocidade".
q='1'
ini='{:-^90}'.format(f' Questão {q} ')
print(ini,'\n\n')
dist=float(input('> Insira a distância percorrida pelo veículo (KM): '))
tempo=float(input('> Insira o tempo que levou para percorrer essa distância (hora): '))
vm=(dist/tempo)
if vm<100:
    veic='Veículo devagar'
elif vm>=100 and vm<140:
    veic='Veículo com velocidade mediana'
elif vm>=140:
    veic='Veículo com alta velocidade'
else:
    veic='Indefinido'
print(f'\n- Distância percorrida: {dist} KM\n- Tempo decorrido: {tempo} h\n- Velocidade média: {vm} km/h\n- Status: {veic}')
# 2. Faça um programa que o usuário entre com os valores de notas de um aluno de acordo com a tabela a seguir 
# e no final possa paresentar a média final do aluno. (N1 - N2 - N3 - N4)
# Se a média final do aluno for menor que 4, print na tela "Reprovado", se for entre 4 e 7, "Recuperação"
# e se for maior que 7 "Aprovado".
q='2'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
L1=float(input('> Insira a nota da L1 (Nota 1): '))
L2=float(input('> Insira a nota da L2 (Nota 1): '))
N1=((L1+L2)/2)
if N1<0:
    N1=0
elif N1>10:
    N1=10
P1=float(input('> Insira a nota da P1 (Nota 2): '))
L3=float(input('> Insira a nota da L3 (Nota 2): '))
L4=float(input('> Insira a nota da L4 (Nota 2): '))
N2=((P1+L3+L4)/3)
if N2<0:
    N2=0
elif N2>10:
    N2=10
P2=float(input('> Insira a nota da P2 (Nota 3): '))
L5=float(input('> Insira a nota da L5 (Nota 3): '))
N3=((P2+L5)/2)
if N3<0:
    N3=0
elif N3>10:
    N3=10
P3=float(input('> Insira a nota da P3 (Nota 4): '))
L6=float(input('> Insira a nota da L6 (Nota 4): '))
L7=float(input('> Insira a nota da L7 (Nota 4): '))
N4=((P3+L6+L7)/3)
if N4<0:
    N4=0
elif N4>10:
    N4=10
Mf=((N1+N2+N3+N4)/4)
if Mf<4:
    aluno='reprovado'
elif Mf>=4 and Mf<7:
    aluno='recuperação'
elif Mf>= 7:
    aluno="aprovado"
else:
    aluno='Erro no sistema pa pa pa'
print(f'\n- Nota 1: {N1}\n- Nota 2: {N2}\n- Nota 3: {N3}\n- Nota 4: {N4}\n- Média final: {Mf}\n- Status do aluno: {aluno}')
# 3. Faça um programa que o usuário entre com o valor de um salário de um colaborador e que o prgrama apresente o saláriod esse colaborador
# depois de descontado 15% de imposto e 10% de INSS (aposentadoria). Se o salário ficar com um valor abaixo de 1000 reais,
# print na tela "Colaborador receberá cesta básica e gratificação", se ficar entre 1000 e 2000, "Colaborador receberá apenas gratificação",
# se ficar maior que 2000, "Colaborador receberá apenas a metade da gratificação"
q='3'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
salario=float(input('> Informe o salário do colaborador: '))
print('\n- Salário bruto: {0} R$'.format(salario))
imposto=(salario*0.15)
print('- Salário depois de atribuido o imposto (15%): {0} R$'.format(salario-imposto))
inss=(salario*0.1)
print('- Salário depois de atribuida a aposentadoria (10%): {0} R$'.format(salario-inss))
sf=(salario-(imposto+inss))
print('- Salário final (25%): {0} R$'.format(sf))
if sf<1000:
    contri='Colaborador receberá cesta básica e gratificação'
elif sf>=1000 and sf<2000:
    contri='Colaborador receberá apenas gratificação'
elif sf>=2000:
    contri='Colaborador receberá apenas a metade da gratificação'
print('-',contri)
# 4. Faça um programa que receba do usuário um valor em metros e forneça o mesmo valor em quilômetros, caso digite 1, em centímetros, caso digite 2
# em milímetros, caso digite 3. Se o usuário digitar outro valor, print na tela, "Erro no sistema"
q='4'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
metros=(float(input('> Quantos metros você deseja converter? ')))
op=(int(input('> Converter para...?\n1.quilômetros\n2.centímetros\n3.milímetros\n> ')))
if op==1:
    calc=(metros/1000)
    rat='quilômetros'
    sig='km'
elif op==2:
    calc=(metros*100)
    rat='centímetros'
    sig='cm'
elif op==3:
    calc=(metros*1000)
    rat='milímetros'
    sig='mm'
else:
    calc='Erro no sistema'
    rat='Indefinido'
    sig='NaN'
print(f'\n- Converter: {metros} m\n- Para: {rat}\n- Resultado: {calc} {sig}')
# 5. Vamos pensar e agir! Pense em um problema que seja viável fazer um código em Pyhton para resolve-lo.
# Regra: Deve utilizara condicional if.
q='5'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
print('{:#^60}'.format(' Calculador de distância entre dois pontos '))
error='\nInput inválido...'
a1='\n> Informe a latitude do primeiro ponto em graus.\n(Obs: máx = 90)\n> '
lat1=float(input(a1))
while lat1<0 or lat1>90:
    print(error)
    lat1=float(input(a1))
c1='\n> Informe:\n1.Norte\n2.Sul\n> '
dlat1=int(input(c1))
while dlat1!=1 and dlat1!=2:
    print(error)
    dlat1=int(input(c1))
a2='\n> Informe a longitude do primeiro ponto em graus.\n(Obs: máx = 180)\n> '
long1=float(input(a2))
while long1<0 or long1>180:
    print(error)
    long1=float(input(a2))
c2='\n> Informe:\n1.Leste\n2.Oeste\n> '
dlong1=int(input(c2))
while dlong1!=1 and dlong1!=2:
    print(error)
    dlong1=int(input(c2))
##########################################################################################
b1='\n> Informe a latitude do segundo ponto em graus.\n(Obs: máx = 90)\n> '
lat2=float(input(b1))
while lat2<0 or lat2>90:
    print(error)
    lat2=float(input(b1))
dlat2=int(input(c1))
while dlat2!=1 and dlat2!=2:
    print(error)
    dlat2=int(input(c1))
b2='\n> Informe a longitude do segundo ponto em graus.\n(Obs: máx = 180)\n> '
long2=float(input(b2))
while long2<0 or long2>180:
    print(error)
    long2=float(input(b2))
dlong2=int(input(c2))
while dlong2!=1 and dlong2!=2:
    print(error)
    dlong2=int(input(c2))
############################################################################################
if dlat1!=dlat2:
    calcl=lat1+lat2
    if lat2>lat1:
        locl=dlat2
    if lat1>lat2:
        locl=dlat1
else:
    if lat2>lat1:
        calcl=lat2-lat1
        locl=dlat2
    else:
        calcl=lat1-lat2
        locl=dlat1

if dlong1!=dlong2:
    calcll=long1+long2
    if long2>long1:
        locll=dlong2
    if long1>long2:
        locll=dlong1
else:
    if long2>long1:
        calcll=long2-long1
        locll=dlong2
    else:
        calcll=long1-long2
        locll=dlong1
if locl==1:
    uno='N'
elif locl==2:
    uno='S'
else:
    uno=''
if locll==1:
    dos='E'
elif locll==2:
    dos='W'
else:
    dos=''
print(f'\n- Resultado:\n{calcl}° {uno}\n{calcll}° {dos}')
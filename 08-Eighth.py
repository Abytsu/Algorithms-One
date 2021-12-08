# Lista 04
# Questão 01
q='1'
ini='{:-^90}'.format(f' Questão {q} ')
print(ini,'\n\n')
error='\n> Comando Inválido: erro de input <\n'
print('{:^50}'.format(' -Calculadora aritmética- '))
num1 = (float(input('\n> Digite o seu primeiro operador: ')))
num2 = (float(input('> Digite o seu segundo operador: ')))
op = (int(input('\n> Escolha a operação:\n1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n5.Exponenciação\n>')))
if op==1:
    calc=(num1+num2)
elif op==2:
    calc=(num1-num2)
elif op==3:
    calc=(num1*num2)
elif op==4:
    calc=(num1/num2)
elif op==5:
    calc=(num1**num2)
else:
    calc='Indefinido'
    print(error)
print('\n- O resultado é: {0}'.format(calc))
# Questão 2
q='2'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
letra=str(input('> Digite a letra (se houver espaço, o programa não reconhecerá!): '))
if letra =='a' or letra=='e' or letra=='i'or letra=='o'or letra=='u' or letra =='A' or letra=='E' or letra=='I'or letra=='O'or letra=='U':
    le=f'\n"{letra}" é vogal'
    print(le)
elif letra == 'b' or letra =='B' or letra =='c' or letra =='C' or letra =='d' or letra =='D' or letra =='f' or letra =='F' or letra =='g' or letra =='G' or letra =='h' or letra =='H' or letra =='j' or letra =='J' or letra =='k' or letra =='K' or letra =='l' or letra =='L' or letra =='m' or letra =='M' or letra =='n' or letra =='N' or letra =='p' or letra =='P' or letra =='q' or letra =='Q' or letra =='r' or letra =='R' or letra =='s' or letra =='S' or letra =='t' or letra =='T' or letra =='v' or letra =='V' or letra =='x' or letra =='X' or letra =='y' or letra =='Y' or letra =='w' or letra =='W' or letra =='z' or letra =='Z':
    le=f'\n"{letra}" é consoante'  
    print(le)
else:
    print(f'\n- "{letra}" não é uma letra, ou o programa não reconheceu a entrada\nObs: verifique os espaços ou acentuações. O programa só reconhece uma letra por operação.')
# Questão 3
q='3'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
q3_1=float(input('> Informe o primeiro número para comparar: '))
q3_2=float(input('> Informe o segundo número para comparar: '))
q3_3=float(input('> Informe o terceiro número para comparar: '))
if q3_1>=q3_2 and q3_1>=q3_3:
    q3_maior=q3_1
elif q3_2>=q3_1 and q3_2>=q3_3:
    q3_maior=q3_2
elif q3_3>=q3_1 and q3_3>=q3_2:
    q3_maior=q3_3
print('- O maior valor é {0}'.format(q3_maior))
# Questão 4
q='4'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
q4_1=float(input('> Informe o valor à ser analisado: '))
if q4_1<0:
    q4_res='negativo'
elif q4_1==0:
    q4_res='neutro'
elif q4_1>0:
    q4_res='positivo'
print(f'\n- O número {q4_1} é {q4_res}.')
# Questão 5
q='5'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
turno=(str(input('> Olá, em qual turno você estuda?\nM - matutino\nV - vespertino\nN - noturno\n> ')))
if turno=='M':
    saludo='\n- Bom dia! :).'
elif turno=='V':
    saludo='\n- Boa tarde! :).'
elif turno=='N':
    saludo='\n- Boa noite! :).'
else:
    print('\n- Valor inválido')
    saludo='\nErro de entrada.\nObs: \n- somente utilize letras maiúsculas\n- quaisquer espaços prejudica no seu funcionamento.'
print(saludo)
# Questão 6
q='6'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
salario = (float(input('> Informe o salário do mês: ')))
gasto = (float(input('> Informe as despesas do mês em reais: ')))
if salario<gasto:
    print('\n- Orçamento estourado')
    exit()
elif salario>=gasto:
    situacao='orçamento ainda disponível'
orcamento=salario-gasto
if orcamento<0:
    orcamento=0
if orcamento==0:
    situacao='orçamento estourado'
print(f'\n\t\t- Gastos dentro do orçamento -\n\n- Salário da pessoa física: {salario} R$\n- Despesas: -{gasto} R$\n- Restante: {orcamento} R$\n- Situação monetária: {situacao}')
# Questão 7 (extra)
q='7'
ini='{:-^90}'.format(f' Questão {q} ')
print('\n\n',ini,'\n\n')
i=float(input('> Insira o valor de i (inteiro e positivo): '))
q7_test=((i*2)%2)
while i<0 or q7_test>0:
    q7_test=((i*2)%2)
    if i<0:
        i=float(input('\n> O valor de "i" não pode ser menor que 0. Por favor, insira outro valor.\n> '))
        q7_test=((i*2)%2)
    if q7_test>0:
        i=float(input('\n> A variável "i" não pode ser float, apenas int. Por favor, insira outro valor.\n> '))
        q7_test=((i*2)%2)
a=float(input('> Insira o valor de a (peso 2): '))
b=float(input('> Insira o valor de b (peso 3): '))
c=float(input('> Insira o valor de c (peso 4): '))
if i<=10:
    if i== 2 or i==4 or i==6 or i==8 or i== 10:
        media=(((a)+(b)+(c))/3)
    mediatipo='aritmética simples.'
    if i!= 2 and i!=4 and i!=6 and i!=8 and i!= 10:
        media='calculo não definido'
        mediatipo='indefinido - valor de "i" é impar.'
elif i>10:
    media=(((a*2)+(b*3)+(c*4))/(2+3+4))
    mediatipo='aritmética ponderada.'
print(f'\n- O resultado da média é: {media}\n- O tipo de média calculado foi: {mediatipo}\n- Valor da varíavel "i" inserido: {int(i)}')

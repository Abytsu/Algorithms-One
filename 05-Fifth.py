#salario=int(input('> Salário? '))
#imposto=float(input('\n> Imposto em %? '))
#print('\n- Valor real: {0}'.format(salario-(salario*(imposto*0.01))))
A=10
B=5
E=int(input('Escolha: \n1.Soma\n2.Sub\n3.Mult\n4.Div\n> '))
if E==1:
    R=A+B
elif E==2:
    R=A-B
elif E==3:
    R=A*B
else:
    R=A/B
print('Resultado é {0}'.format(R))

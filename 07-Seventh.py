# Lista 1
# Questão 1
print("Nome: Mordred\n\tIdade: 18\n\t\tSigno: Leão\n\t\t\tAniversário: 12/10/1653\n\t\tTime: Flamengo\n\tCidade: Fuyuki\nSonho: Graal")

# Questão 2
nome = ("Mash")
salario_mes = 1000
total_vendas = 2000
salario_final_mes = salario_mes + (total_vendas*0.15)

print(nome)
print(salario_mes)
print(salario_final_mes)

# Questão 3

nome_aluno = ("Tohsaka")
n1 = 7.0
n2 = 10.0
n3 = 0.0

media = (n1+n2+n3)/3

print(nome_aluno)
print(media)

# Questão 4

valor_real = 1000
dolar = 5.62
valor_dolar = valor_real/dolar
print(valor_dolar)

# Questão 5

poupanca = 1000
juros = 0.007
rendimento = poupanca + (poupanca*juros)
print(rendimento) 

# Questão 6
# import. importa uma blibioteca
# só copiar o código

# Questão 7

# Raio é do meio do círculo até fore, diâmetro é duas vezes o raio (de um lado ao outro)

raio = 3
area = 3.14*raio**2
comprimento = 2*3.14*raio

print(area)
print(comprimento)

# Questão 8 

xi="artoria pendragon"
print("\nNome:",xi)
print(xi[8]+xi[9]+xi[10]+xi[2]+xi[0]+xi[14]+xi[15]+xi[16]+xi[3])
print(xi[2]+xi[1]+xi[5]+xi[11]+xi[9]+xi[16]+xi[2]+xi[9])
print(xi[2]+xi[5]+xi[6]+xi[14]+xi[3])

# Lista 2

# Questão 1

tempo = int(input("Qual o tempo : \n"))
distancia = int(input("Qual a distância: \n"))

velocidade = distancia/tempo
aceleracao= velocidade/tempo

print(velocidade)
print(aceleracao)

# Questão 2

L1 = int(input("L1:"))
L2 = int(input("L2:"))
L3 = int(input("L3:"))
L4 = int(input("L4:"))
L5 = int(input("L5:"))
L6 = int(input("L6:"))
L7 = int(input("L7:"))
P1 = int(input("P1:"))
P2 = int(input("P2:"))
P3 = int(input("P3:"))

N1 = (L1 + L2)/2
N2 = (P1 + L3 + L4)/3
N3 = (P2 + L5)/2
N4 = (P3+L6+L7)/3

media_final = (N1 + N2 + N3 + N4)/4

print(media_final)

# Questão 3

salario_l2 = float(input("Salário? "))
salario_final_l2 = salario_l2 - (salario_l2*0.15) - (salario_l2*0.1)

print(salario_final_l2)

# Questão 4

metros = float(input('Metros? '))
km = metros/1000
cm = metros*100
mm = metros*1000

print(km)
print(cm)
print(mm)

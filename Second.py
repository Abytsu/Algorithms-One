# (redacted) - Informática EMI 1 

# 1. Imprima na tela as seguintes informações de acordo com os respectivos posicionamentos utilizando apenas um comando de print. Utilize \n para quebra de linha e \t para espaçamento
print(">Nome: Illyasviel von Einzbern\n\t>Idade: 18 anos\n\t\t>Signo: Sagitário\n\t\t\t>Aniversário: 20 de novembro\n\t\t>Time: Flamengo\n\t>Cidade: Fuyuki - Japão\n>Sonho: Obter o Santo Graal.\n")

# 2. Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês(em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e o salário no final do mês.
nome="Homem de Ferro"
salario=4000
vendas=2000
final=salario+vendas*0.15
print("Nome do vendedor:",nome,"\nSalário fixo:",salario,"R$", "\nTotal de vendas no mês:",vendas,"\nSalário final:",final,"R$")

# 3. Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e sua média (aritmética)
alunonome="Yoshikage Kira"
nota1=8.5
nota2=6.0 
nota3=9.0 
media=(nota1+nota2+nota3)//3
print("\nNome do aluno:",alunonome,"\nPrimeira nota:",nota1,"\nSegunda nota:",nota2,"\nTerceira nota:",nota3,"\nMédia:",media)

# 4. Questão
cotacao=5.66
quantity=6742 #dólares
print("\nBem-vindo à sua conta!","\nQuantidade de dólares disponível na conta:",quantity,"US$","\nCotação:",cotacao,"R$","\nQuantidade convertida para Reais:",quantity*cotacao,"R$")

# 5. Questão
conta1=2200
deposito=3240
rend=(deposito+conta1)*0.007
print("\nSaldo anterior:",conta1,"R$","\nTransferência entre contas","\nTotal depositado:",deposito,"R$","\nValor atual:",(conta1+deposito),"R$","\nRendimento após um mês:",rend,"R$","\nValor após um mês com rendimento:",rend+deposito+conta1,"R$")

# 6. Questão 

import sys
print("\nVersão do Python:")
print(sys.version)
print("Informação da versão:")
print(sys.version_info)

# 7. Questão
raio=3
pi=3.14
area= pi*(raio**2)
comp= 2*pi*raio
print("\nCircunfêrencia com raio de 3 metros","\nÁrea:",area,"M","\nComprimento:",comp,"M")

# 8 . Questão
xi="artoria pendragon"
print("\nNome:",xi)
print(xi[8]+xi[9]+xi[10]+xi[2]+xi[0]+xi[14]+xi[15]+xi[16]+xi[3])
print(xi[2]+xi[1]+xi[5]+xi[11]+xi[9]+xi[16]+xi[2]+xi[9])
print(xi[2]+xi[5]+xi[6]+xi[14]+xi[3])

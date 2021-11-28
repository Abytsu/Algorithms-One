n1=float(input("Nota 1: "))
n2=float(input("Nota 2: "))
n3=float(input("Nota 3: "))
media=((n1+n2+n3)/3)
print(f'Média final: {media}')
#a= 10
#b= 5 
#c= '10'
#d= '5'
#print(a+b)
#print(c+d)

#p='Pikachu '
#s= 10
#print(p*s)

#name=input('Qual é o seu nome?\n')
#print(f"Nome: {name}")

prompt='Qual a velocidae rasante de uma andorinha livre?    '
velocidade=input(prompt)
print(int(velocidade))
print(int(velocidade)**5)
print(int(velocidade*5))
print(int(velocidade)/5)
print(int(velocidade)+432*2)

print(type(True))
print(type(False))

a = 5
b = 10
c = b*2

print(a==b) # Dois iguais é comparação, um igual é valor da variável
print(a!=b)
print(b>a)
print(b<a)
print(c>=a)
print(c<=a)
print(a is a)
print(b is not c)

a = 5
b = 10
c = 20
print(a > b and a < c) # as duas precisam ser verdadeira
print(a > b or a < c) # ou uma coisa ou outra (pelo menos uma verdadeira)

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print(a > b and c > b) # as duas precisam ser verdadeira
print(a > b or a < c) # ou uma coisa ou outra (pelo menos uma verdadeira)

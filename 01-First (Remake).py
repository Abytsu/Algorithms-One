# Etapa 1
# Introdução: Conhecendo as variáves e o comando print
# > Comando "print('objeto')"
# Comando usado para apresentar algo na saída do usuário (mostrar).
# Um dos únicos comandos especialmente do Python
# Deve ser feito de forma minúscula e respeitando a regra das variáveis.
# Nota: o jogo da velha(#) é usado para adicionar comentários que não aparecerão no código final.
# > Variável 1 - string(str): caractéres, frases, palavras e letras.
# Essa variável deve ser escrita dentro do comando print com aspas(") ou aspas simples(').
print("Exemplo 01 - string:")
print('Hello, World!')
print("Flamengo não é time")
print("Fui na casa do João roubar pão!\n")
# Nota: "\n" é o termo usado para se pular uma linha em Python.

# > Variável 2 - inteiro(int): números inteiros
# Essa variável pode ser escrita sem aspas, se for escrita com aspas se tornará string
# e não operará em funções aritméticas.
print("Exemplo 02 - int:")
print(700)
print(-10)
print('25')
print('\n')

# > Variável 3 - float: números decimais
# Essa varíavel compartilha a mesma regra da variável int.
# Diferentemente do uso cotidiano, números decimais devem ser escritos usando 
# "." ao em vez de uma ",".
print("Exemplo 03 - float:")
print(0.25)
print(-2.5)
print('20.5')
print("\n")

# > Variável 4 - complex: números complexos
# Pouco se sabe, porém o que se sabe é que é resultante de raiz quadrada de números negativos
# Representados por: 2i, i... ou j tbm

# > Extra:
# É possível identificar a classe de uma variável com o comando:
# "print(type('varíavel'))"
print("Exemplo Extra - type")
print(type(-2))
print(type(10.5))
print(type("Carlos Eduardo"))
print("\n")

# Etapa 2
# Operações Aritméticas: soma, subtração, divisão, multiplicação, potência e resto
# Essas operações devem ser feitas sem as aspas para serem consideras int ou float.

# > Soma: "+"
# Soma duas ou mais quantidades especificadas
print("Exemplo 04 - soma:")
print(210+10)
print(-40+90)
print(2.5+25)
print("\n")

# > Subtração: "-"
# Subtrai duas ou mais quantidades especificadas
print("Exemplo 05 - subtração:")
print(210-10)
print(-40-90)
print(2.5-25)
print("\n")

# > Multiplicação: "*"
# Multiplica duas ou mais quantidades especificadas
print("Exemplo 06 - multiplicação:")
print(210*10)
print(-40*90)
print(2.5*25)
print("\n")

# > Divisão: "/" ou "//"
# Divide duas ou mais quantidades especificadas
print("Exemplo 07 - divisão:")
print(210/10)
print(-40/90)
print(2.5/25)
print("\n")
# Extra 01: Também pode se utilizar duas barras(//) para resultados somente inteiros
print(210//10)
print(-40//90)
print(2.5//25)
print(800//300,800/300)
print("\n")
#Extra 02: Também pode se utilizar porcento(%) para mostrar somente o resto da divisão
print(210%10)
print(-40%90)
print(2.5%25)
print("\n")

# > Potenciação: "**"
# Potencia duas ou mais quantidades especificadas
print(210**10)
print(-40**90)
print(2.5**25)
print("\n")

# Etapa 3 
# Manipulação de String e Concatenação
# Para quebrar uma linha dentro de um print, utilizase três aspas ou apenas \n (\t para espaço)
print("""Roberto
Carlos
Fernando
asss""")
print('''\nNão ligo
pra
voce
\tcala a boca''')

# Atribuir valor a variável
x=("Kal'Tsit")
y='Yaggr'
print(x)
print(x,y)
# "," dá espaço entre as variáveis/"+" junta as variáveis sem espaço
a=5
b=24
c=b-a
print(f'c:{c}')

# Concatenação de string
# Consegue formar outra palavra através de uma palavra (sempre começa do 0)
r='roberto de nobrega'
print(r[0])
print(r[1])
print(r[2])
print(r[3])
print(r[4])
print(r[5])
print(r[6])
print(r[2]+r[3]+r[0]+r[3]+r[5]+r[5]+r[17])






#exercicio - 03, soma de valores.
n1 = int(input("Informe um valor: "))
n2 = int(input("Informe um segundo valor: "))
s = n1 + n2
#print('O resultado da soma é: ', s)

"""Para facilitar a apresentação dos resultados pelo terminal podemos utilizar a função
.format que temos no print."""

print('O resultado da soma entre {} e {} é igual a {}'.format(n1, n2, s))
'''Elaborar um programa que calcule e mostre o fatorial de um número
(N!),sendo que N é fornecido pelo usuário'''


from math import factorial

n = int(input('digite um número para calcular seu fatorial:'))

f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))

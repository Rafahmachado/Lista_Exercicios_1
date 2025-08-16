
'''Faça um programa que calcule o valor total da venda de uma mercadoria, qualquer
que seja o número de unidades vendidas e o valor da mercadoria. '''

vendas = int(input("Digite o número de unidades vendidas: "))
valor_unidade = float(input("Digite o valor unitário da mercadoria: "))
valor_total = vendas * valor_unidade
print(f"O valor total da venda é: R$ {valor_total:.2f}")

'''Uma empresa deseja fazer o reajuste salarial dos seus funcionários da seguinte
forma: se o empregado for da categoria “Técnico”, receberá 30% de aumento, se for
da categoria “Gerente”, receberá 20% de aumento e os demais funcionários
receberão 15% de aumento. Faça um programa utilizando o comando if-else que leia
do teclado o salário e a categoria do funcionário, calcule e imprima o seu novo
salário'''



salario = float(input("Digite o salário do funcionário: "))
categoria = input("Digite a categoria do funcionário (Tester/Desenvolvedor/Design): ").strip().lower()

if categoria == "técnico":
    novo_salario = salario * 1.300
elif categoria == "gerente":
    novo_salario = salario * 1.200
else:
    novo_salario = salario * 1.150

print(f"O novo salário é: R$ {novo_salario:.2f}")
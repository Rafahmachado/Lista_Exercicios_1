''' Outro aluno fez apenas duas provas, tirando 5.5 e 7.9. Faça um programa que
armazene esses valores em variável, calcule e imprima a nota que ele precisa tirar
para ficar com média 7. '''

nota1 = 5.5
nota2 = 7.9
media = 7
nota_necessaria = (media * 3) - (nota1 + nota2)
print(f"A nota necessária para alcançar a média de {media} é: {nota_necessaria:.2f}")



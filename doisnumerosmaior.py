# Exercício Python 18: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

numero_a = int(input("Digite um númrero inteiro: "))
numero_b = int(input("Digite outro número inteiro: "))
maior = numero_a

print(f"Seus números digitados foram {numero_a} e {numero_b}.")

if numero_a < numero_b :
    maior = numero_b
    print(f"O numero {numero_b} é o maior número e o {numero_a} é o menor número.")
elif numero_a == numero_b :
    print("Nenhum dos números é maior. Eles são iguais.")
else :
    print(f"O numero {numero_a} é o maior número e o {numero_b} é o menor número.")
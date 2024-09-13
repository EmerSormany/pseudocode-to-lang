
print("Digite as notas do aluno: ")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 50:
    print(f"Média: {media:.2f} - Situação: Reprovado")
elif media >= 70:
    print(f"Média: {media:.2f} - Situação: Aprovado")
else:
    print(f"Média: {media:.2f} - Situação: Recuperação")

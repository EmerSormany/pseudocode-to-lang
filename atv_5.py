
valor_saque = int(input("Digite o valor que deseja sacar: "))

notas_50 = valor_saque // 50
resto = valor_saque % 50

notas_10 = resto // 10
resto = resto % 10


notas_1 = resto // 1


print(f"Valor do saque: R$ {valor_saque}")
print(f"Quantidade de notas de R$ 50: {notas_50}")
print(f"Quantidade de notas de R$ 10: {notas_10}")
print(f"Quantidade de notas de R$ 1: {notas_1}")

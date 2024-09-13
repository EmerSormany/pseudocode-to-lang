import math

print("Insira os valores a, b e c da equação: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - 4*a*c
print(delta)

if delta < 0:
    print("A equação não possui raízes reais")
else:
    raiz_a = (-b + math.sqrt(delta))/2*a
    raiz_b = (-b - math.sqrt(delta))/2*a
    print(f"As raízes da equação são {raiz_a:.3f} e {raiz_b:.3f}")
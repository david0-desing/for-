numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

print(f"\nTabla del {numero}\n")

for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
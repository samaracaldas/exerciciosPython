N = int(input("Quantos numeros voce vai digitar? "))
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite um numero: "))

print()
print(f"Valores: ", end="")
for i in range(0, N):
    print(f"{vet[i]:.1f} ", end="")

print()

soma = 0
for i in range(0, N):
    soma = soma + vet[i]

media = soma / N

print(f"SOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")

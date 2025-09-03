import time

def sumatoria_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + sumatoria_recursiva(n - 1)

for valor in [100, 500, 900]:
    inicio = time.time()
    resultado = sumatoria_recursiva(valor)
    fin = time.time()
    print(f"Sumatoria hasta {valor}: {resultado} (Tiempo: {fin - inicio:.6f} segundos)")


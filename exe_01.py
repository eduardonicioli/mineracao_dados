def amplitude(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    return max(lista) - min(lista)

# Testando a função
testes = [
    [3, 7, 2, 9, 4],     # Amplitude: 7 (9 - 2)
    [10, 15, 20, 25],    # Amplitude: 15 (25 - 10)
    [-5, -1, -10, 0],    # Amplitude: 10 (0 - (-10))
    [42],                # Amplitude: 0 (42 - 42)
    []                   # Lista vazia, retorna None
]

for lista in testes:
    print(f"Lista: {lista} -> Amplitude: {amplitude(lista)}")

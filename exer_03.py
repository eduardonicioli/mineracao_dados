def calcular_valor_transporte(peso):
    if peso <= 10:
        return "Valor do transporte: R$ 50,00"
    elif 11 <= peso <= 20:
        return "Valor do transporte: R$ 80,00"
    else:
        return "Transporte não aceito"

# Entrada do usuário
peso_carga = int(input("Digite o peso da carga (kg): "))

# Exibir o resultado
print(calcular_valor_transporte(peso_carga))

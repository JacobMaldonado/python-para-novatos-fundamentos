# Conocer el indice en una iteracion de lista
variable_lista = [12, "Texto", True, 3.2]
for indice, valor in enumerate(variable_lista):
    print(f'El indice {indice} tiene el valor {valor}')
    if indice == 3:
        variable_lista[indice] += 1

print(variable_lista)
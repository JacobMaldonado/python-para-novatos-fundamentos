# comparacion IN
# variable_lista = [1, "texto", True]
# if 'texto' in variable_lista:
#     print('Existe en la lista')
#     print(variable_lista.index('texto'))
# else:
#     print('No Existe en la lista')

# Funcion isinstance
variable_lista = [1, 2, 3]
variable_tupla = (1, 2, 3)
if isinstance(variable_tupla, list):
    print('Si es lista')
else:
    print('No es lista')
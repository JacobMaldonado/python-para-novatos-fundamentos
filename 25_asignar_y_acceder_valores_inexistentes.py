# Agregar valores inexistentes
# variable_diccionario = {}
# variable_diccionario['llave_inexistente'] = 10
# print(variable_diccionario)

# Buscar valores inexistentes
variable_diccionario = {
    'llave_inexistente': 20
}
#print(variable_diccionario.get('llave_inexistente', 10))
# verificar una llave dentro del diccionario
if 'llave_inexistente' in variable_diccionario:
    print(variable_diccionario['llave_inexistente'])
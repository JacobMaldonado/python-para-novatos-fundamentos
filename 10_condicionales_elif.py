numero = int(input('Escribe un Número'))

if numero > 10:
    print('Numero es > 10')
elif numero > 5:
    print('Numero es > 5 pero <= 10')
elif numero > 0:
    print('Numero es > 0 pero <= 5')
else:
    print('Numero es <= 0')
print('Final del programa')
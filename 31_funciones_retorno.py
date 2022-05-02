def suma(a, b):
    return a + b, b + a
    
resultado_suma_1, resultado_suma_2 = suma(1, 2)
print(resultado_suma_1)
print(resultado_suma_2)
resultado_suma_3 = suma(resultado_suma_2, resultado_suma_1)[0]
print(resultado_suma_3)

# Anidar funciones
resultado_anidado = suma(1, suma(1,2)[0])
print(resultado_anidado)
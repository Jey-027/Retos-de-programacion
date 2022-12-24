'''
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
'''

def decimal_to_binario(number:int):
    byte = [1016, 508, 254, 128, 64, 32, 16, 8, 4, 2, 1]
    binary = []
    decimal = []
    temp = 0
    for n in byte:
        if n > number:
            decimal.append('0')
        elif n <= number:
            temp = number - n
            number = temp
            decimal.append('1')   

    var = decimal.index('1')

    binario = ''.join(decimal[var:])
    return binario

print(decimal_to_binario(111))

''''
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
'''

def counting_words(phrase):
    signos = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''    
    mydict = {}
    count = 0
    palabra = []

    for letter in phrase:
        if letter not in signos:
            palabra.append(letter)
    
    var = ''.join(palabra).lower().split(' ')
    
    for i in var:
        word = i
        for find in var:
            if find == word:
                count += 1
        mydict[i] = count
        count = 0

    return mydict

print(counting_words("Hola Mundo. hello world1, esto traduce hola mundo en español!!.."))



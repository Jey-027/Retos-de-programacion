''''
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''

def reverse_string(word):
    new_string = ''
    list = []
    for i in word:
        list.insert(0,i)
    new_string = ''.join(list)
    
    return new_string


print(reverse_string('Hola mundo'))


 
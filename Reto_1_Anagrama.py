
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.

def anagrama(word1, word2):
    
    list1 = []
    list2 = []
    for i in word1:
        list1.append(i.lower())
    
    for j in word2:
        list2.append(j.lower())
    
    if list1 == list2:
        return False
    elif list1.sort() == list2.sort():
        return True
    
print(anagrama("Amor", "amor"))
print(anagrama("Roma", "amor"))
print(anagrama("GATO", "toga"))




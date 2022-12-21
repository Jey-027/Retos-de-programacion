
def anagrama(word1, word2):
    dict1 = {}
    cont1 = 0
    for palabra in word1:
        var = palabra
        for buscar in word1:
            if var == buscar:
                cont1 += 1

        dict1[palabra.lower()] = cont1
        cont1 = 0

    dict2 = {}
    cont2 = 0
    for palabra2 in word2:
        var2 = palabra2
        for find in word2:
            if var2 == find:
                cont2 += 1
        
        dict2[palabra2.lower()] = cont2
        cont2 = 0
    
    if dict1 == dict2:
        return True
    else:
        return False

print(anagrama("Amor", "Roma"))




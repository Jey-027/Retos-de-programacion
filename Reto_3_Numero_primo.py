def is_numero_primo(number):
    for i in range(1,number + 1):
        if i != 1:
            if i == 2 or i == 3 or i == 5 or i == 7:
                print(i)
            else:
                if i % i == 0 and i % 2 !=0 and i % 3 != 0 and i % 5 !=0 and i % 7 != 0:
                    print(i)

is_numero_primo(100)  
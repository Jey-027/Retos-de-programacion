

def fibonacci(num):
    x = 0
    y = 1

    for numero in range(num):
        print(x)
        z = x + y
        x = y
        y = z

        

fibonacci(8)

# Area triangulo ->  A = b * h / 2
# Area cuadrado -> A = lˆ2
# Area rectangulo ->  A = b * h

def area_poligono(poligono:str):

    if poligono.lower() == 'triangulo':
        base = float(input('Ingrese la base del triangulo: '))
        altura = float(input('Ingrese la altura del triangulo: '))
        area = base * altura / 2

        return area
    
    elif poligono.lower() == 'cuadrado':
        lado = float(input('Ingrese el lado del cuadrado: '))
        area = lado * lado

        return area
    
    elif poligono.lower() == 'rectangulo':
        base = float(input('Ingrese la base del Rectangulo: '))
        altura = float(input('Ingrese la altura del Rectangulo: '))
        area = base * altura

        return area


print(area_poligono("Triangulo"))
print(area_poligono("Cuadrado"))
print(area_poligono("Rectangulo"))
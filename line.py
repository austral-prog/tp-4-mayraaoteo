def line():
    import math
    
    my_variable_a = float(input("Ingrese el coeficiente A: "))
    my_variable_b = float(input("Ingrese el coeficiente B: "))
    my_variable_x1 = float(input("Ingrese el coeficiente X1: "))
    my_variable_d1 = float( (my_variable_a * my_variable_x1) + my_variable_b )
    my_variable_x2 = float(input("Ingrese el coeficiente X2: "))
    my_variable_d2 = float( (my_variable_a * my_variable_x2) + my_variable_b )
    p1 = my_variable_x1, my_variable_d1
    p2 = my_variable_x2, my_variable_d2
    distance = math.dist(p1, p2)

    print(f"El coeficiente A de su ecuación de la recta es: {my_variable_a}")
    print(f"El coeficiente B de su ecuación de la recta es: {my_variable_b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {my_variable_x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {my_variable_x2}")
    print()
    print("Para la siguiente ecuación:")
    print(f"\tY = {my_variable_a}X + {my_variable_b}")
    print()
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({my_variable_x1}, {my_variable_d1})")
    print(f"\tP2 ({my_variable_x2}, {my_variable_d2})")
    print()
    print(f"La distancia entre ellos es: {distance}")

def leap_year():

    my_variable_year = int(input("Ingrese un año: "))
    
    if ((my_variable_year % 100 == 0) and (my_variable_year % 400 == 0)) or ( (my_variable_year % 100 != 0) and (my_variable_year % 4) == 0 ):
        print(f"El año {my_variable_year} es bisiesto")
    else: print(f"El año {my_variable_year} no es bisiesto")

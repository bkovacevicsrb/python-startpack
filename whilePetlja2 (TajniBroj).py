tajniBroj = 54
broj = 0

while tajniBroj != broj:
    broj = int(input(" Pogodite tajni broj: "))

    if tajniBroj == broj:
        print("Pogodak!")
    elif tajniBroj < broj:
        print("Tajni broj je manji")
    else :
        print ("Tajni broj je veci")
print ("Kraj programa")        

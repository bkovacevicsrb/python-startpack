def min2Broja(a, b):
    if a < b:
        return a
    else:
        return b
    
        

prviBroj = float(input(" Unesite 1. broj : "))
drugiBroj = float(input(" Unesite 2. broj : "))

manjiOdDva = min2Broja (prviBroj, drugiBroj)

print(" Manji od ta 2 je : " + str(manjiOdDva))

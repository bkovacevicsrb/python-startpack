def faktorijel (n):
    if n == 0:
        return 1
    else:
        return n * faktorijel (n-1)

rezultat = faktorijel(250)

print ("Rezultat faktorijela 250 je : " + str (rezultat))

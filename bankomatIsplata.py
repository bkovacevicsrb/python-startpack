iznos = int(input(" Jovana, dobrodosli na bankomat. Unesite iznos za isplatu : "))

zaIsplatuOd5000 = 0
zaIsplatuOd2000 = 0
zaIsplatuOd1000 = 0
zaIsplatuOd500 = 0
zaIsplatuOd200 = 0
zaIsplatuOd100 = 0
zaIsplatuOd50 = 0
zaIsplatuOd20 = 0
zaIsplatuOd10 = 0
zaIsplatuOd5 = 0
zaIsplatuOd2 = 0
zaIsplatuOd1 = 0

while iznos >= 5000:
        iznos -= 5000
        zaIsplatuOd5000 += 1

while iznos >= 2000:
        iznos -= 2000
        zaIsplatuOd2000 += 1

while iznos >= 1000:
        iznos -=1000
        zaIsplatuOd1000 +=1

while iznos >= 500:
        iznos -=500
        zaIsplatuOd500 +=1

while iznos >= 200:
        iznos -=200
        zaIsplatuOd200 +=1

while iznos >= 100:
        iznos -=100
        zaIsplatuOd100 +=1

while iznos >= 50:
        iznos -=50
        zaIsplatuOd50 +=1

while iznos >= 20:
        iznos -=20
        zaIsplatuOd20 +=1

while iznos >= 10:
        iznos -=10
        zaIsplatuOd10 +=1

while iznos >= 5:
        iznos -=5
        zaIsplatuOd5 +=1

while iznos >= 2:
        iznos -=2
        zaIsplatuOd2 +=1

while iznos >= 1:
        iznos -=1
        zaIsplatuOd1 +=1

if zaIsplatuOd5000 > 0:
        print ("Treba isplatiti od 5000din : " +str(zaIsplatuOd5000))
        
if zaIsplatuOd2000 > 0:
        print ("Treba isplatiti od 2000din : " +str(zaIsplatuOd2000))

if zaIsplatuOd1000 > 0:
        print ("Treba isplatiti od 1000din : " +str(zaIsplatuOd1000))

if zaIsplatuOd500 > 0:
        print ("Treba isplatiti od 500din : " +str(zaIsplatuOd500))

if zaIsplatuOd200 > 0:
        print ("Treba isplatiti od 200din : " +str(zaIsplatuOd200))

if zaIsplatuOd100 > 0:
        print ("Treba isplatiti od 100din : " +str(zaIsplatuOd100))

if zaIsplatuOd50 > 0:
        print ("Treba isplatiti od 50din : " +str(zaIsplatuOd50))

if zaIsplatuOd20 > 0:
        print ("Treba isplatiti od 20din : " +str(zaIsplatuOd20))

if zaIsplatuOd10 > 0:
        print ("Treba isplatiti od 10din : " +str(zaIsplatuOd10))

if zaIsplatuOd5 > 0:
        print ("Treba isplatiti od 5din : " +str(zaIsplatuOd5))

if zaIsplatuOd2 > 0:
        print ("Treba isplatiti od 2din : " +str(zaIsplatuOd2))

if zaIsplatuOd1 > 0:
        print ("Treba isplatiti od 1din : " +str(zaIsplatuOd1))     

print ("Izvadite karticu, dovidjenja Jovana")

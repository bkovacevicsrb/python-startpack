korisnici = [
    {
    'ime' : 'Bane',
    'prezime' : 'Kovacevic'
    },       

    {
    'ime' : 'Marko',
    'prezime' : 'Markovic'
    },

    {
    'ime':'Milos',
    'prezime' : 'Markovic'
    },

    {
    'ime' : 'Nemanja',
    'prezime' : 'Matic',
    },

            ]

redniBroj = 1
for korisnik in korisnici:
    print ('{0:5d}. {1:<20s} {2:<20s}'.format(redniBroj, korisnik['ime'], korisnik['prezime']))
    redniBroj +=1

    
    


    

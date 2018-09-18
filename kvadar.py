def Kvadar (visina, siria, duzina):
    return {
        'visina' : visina,
        'sirina' : sirina,
        'duzina' : duzina
            }

def proveraKvadra(kvadar):
    




def zapremina (kvadar):
    if proveraKvadra(kvadar)==0:
        return 0
    return kvadar ['visina'] * kvadar['sirina'] * kvadar['duzina']

def povrsina (kvadar):
    potrebnaPolja = ['visina', 'sirina', 'duzina']
    for polje in potrebnaPolja:
        if polje not in kvadar.keys():
            print (' Kvadar mora da ima kljuc ' + polje)
            return 0
    return 2* (kvadar['sirina'] * kvadar['visina'] +
               kvadar['sirina'] * kvadar['duzina']
               kvadar['duzina'] * kvadar['visina'])


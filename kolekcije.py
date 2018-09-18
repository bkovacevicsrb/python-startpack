import collections

Student = collections.namedtuple ('Student', 'ime, prezime, indeks, prosek')

s1 = Student ('Branko', 'Kovacevic', 500009, 9.5)

print(s1.prosek)

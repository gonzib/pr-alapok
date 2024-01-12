# feladat_032

nyelvek = ['Python','C','C++','Java','Python']
keresett_elem = 'C'

# RENDEZÉS
nyelvek.sort()
nyelvek.reverse()
print(nyelvek)

# KERESÉS
if keresett_elem in nyelvek == True:
    print(nyelvek.index(keresett_elem))
else:
    print(f'Nincs a listában a "{keresett_elem}" keresett elem.')

print(nyelvek.count('Python'))

# BŐVÍTÉS


# TÖRLÉS
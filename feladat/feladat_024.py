# feladat_024

szo = "almafa"
print(szo[:3])

# üres listát hoz létre
gyumolcsok = []

# kezdőérték nélküli változót hoz létre
gyumolcs = None
while gyumolcs != '':
    gyumolcs = input('Adj meg egy gyümölcsöt! ')
    if gyumolcs != '':
        # hozzáfűzi a listahoz
        gyumolcsok.append(gyumolcs)

print(gyumolcsok)
print(f'A gyümölcsök lista elemeinek száma: {len(gyumolcsok)}')
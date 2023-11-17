# feladat_021
# Egymásba ágyazott ciklusok II.

szam = int(input('Kérek egy páros számot: '))
szam_fele = szam / 2
darab_karakter = 1
sor = 1
while sor <= szam_fele:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1
darab_karakter = szam_fele
sor = 1
while sor <= szam_fele:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter - 1
    sor = sor + 1

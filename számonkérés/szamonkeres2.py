# Gönczi Balázs 1.mat csoport  2023. 10. 13.
jegy = int(input('kérek egy értékelést!'))
if jegy == 1:
    print(f'Az érdemjegye {jegy}-es, elégtelen!')
elif jegy == 2:
    print(f'Az érdemjegye {jegy}-es, elégséges!')
elif jegy == 3:
    print(f'Az érdemjegye {jegy}-as, közepes!')
elif jegy == 4:
    print(f'Az érdemjegye {jegy}-es, jó!')
elif jegy == 5:
    print(f'Az érdemjegye {jegy}-ös, kitűnő!')
else:
    print(f'A "{jegy}" szám nem érdemjegy!')
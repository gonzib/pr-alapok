#feladat_015
"""
Kérjök be a vezeték és keresztnevünket.
Irassuk ki föggvény segítségével nevünket.
pl:
Be: "Kérem a vezetékneved: Takács"
Be: "Kérem a keresztneved: István"
Ki: "A nevem: Takács István"
"""

vezeteknev = input('Kérem a vezetékneved!')
keresztnev = input('Kérem a keresztneved!')

def nevf(vnev,knev):
    nevem = vnev + ' ' + knev
    return nevem

print(f'A nevem: {nevf(vezeteknev,keresztnev)}')
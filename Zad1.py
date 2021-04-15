def oblicz_zarobki_w_netto(kwota_brutto):
    ub_emerytalne = 0.0976 * kwota_brutto
    ub_rentowe = 0.015 * kwota_brutto
    ub_chorobowe = 0.0245 * kwota_brutto
    ubezpieczenia = kwota_brutto - (ub_emerytalne + ub_rentowe + ub_chorobowe)
    ub_zdrowotne = ubezpieczenia * 0.09
    skladki = ub_emerytalne + ub_rentowe + ub_chorobowe + ub_zdrowotne
    zus_odliczenie = ubezpieczenia * 0.0775
    zaliczka_na_PIT = (kwota_brutto - skladki) * 0.17 - 43.76 - zus_odliczenie
    if zaliczka_na_PIT < 0:
        zaliczka_na_PIT = 0
    return round(
        kwota_brutto - (skladki + zaliczka_na_PIT),
        2,
    )


def Wyswietl_Wykonaj():
    kwota = float(input("Podaj kwote brutto: "))
    print(f"Kwota netto wynosi: {oblicz_zarobki_w_netto(kwota)} zł")
    zabiera = kwota - oblicz_zarobki_w_netto(kwota)
    print(f"Kwota Do oddania {round(zabiera,2)} zł")


if __name__ == "__main__":
    Wyswietl_Wykonaj()
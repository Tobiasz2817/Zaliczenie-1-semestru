def koszty_pracodawcy(kwota_brutto):
    ub_emerytalne = kwota_brutto * 0.0976
    ub_rentowe = kwota_brutto * 0.065
    ub_wypadkowe = kwota_brutto * 0.0167
    FP = kwota_brutto * 0.0245
    FGSP = kwota_brutto * 0.01
    return kwota_brutto + ub_emerytalne + ub_rentowe + ub_wypadkowe + FP + FGSP


def Wyswietl_Wykonaj():
    kwota_brutto = float(input("Podaj kwotę brutto zarobkow: "))
    print(
        f"Miesięczny koszt całkowity dla pracodawcy {round(koszty_pracodawcy(kwota_brutto),2)}zl"
    )


if __name__ == "__main__":
    Wyswietl_Wykonaj()
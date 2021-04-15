def prawdziwa_pojemnosc_gb(pojemnosc_podana_przez_producenta):

    bajty = pojemnosc_podana_przez_producenta * 1000000000

    return round(bajty / 1024 / 1024 / 1024, 2)


def Wykonaj():
    gb = float(input("Podaj rozmiar w GB :"))
    print(f"Prawdziwy Rozmiar : {prawdziwa_pojemnosc_gb(gb)} GB")
    print(f"Producenci kradną : {round(gb-prawdziwa_pojemnosc_gb(gb),2)} GB")


if __name__ == "__main__":
    Wykonaj()
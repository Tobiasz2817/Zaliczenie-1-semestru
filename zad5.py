def Przelicz(kwota, typ_waluty, odp):
    Kursy_walut = {
        "THB" : 30.73,
        "BTC" : 0.000018,
        "BTN" : 72.56,
        "MRO" : 35.96,
        "ETH" : 0.00056,
        "PLN" : 3.85,
        "RON" : 4.09,
        "PAB" : 1.00
    }
    if typ_waluty in Kursy_walut:
        if odp == "TAK":
            return round(kwota * Kursy_walut[typ_waluty],2)
        else:
            return round(kwota / Kursy_walut[typ_waluty],2)
    else:
        return "Nie ma takiej Waluty"


def Kantor():
    while True: 
        odp = input("Posiadasz Dolary ? Tak/Nie :").upper()
        if odp == "TAK":
            print("""Na co chciałbyś wymienić :
            THB - Baht Tajski , 1 USD - 30,73 THB 
            BTC - Bitcoin , 1 USD - 0,000018 BTC
            BTN - Ngultrum bhutański , 1 USD - 72,56 BTN
            MRO - Ugija mauretańska , 1 USD - 35,96 MRO
            ETH - Ethereum , 1 USD - 0,00056 ETH
            PLN - Polski złoty , 1 USD - 3,85 PLN
            RON - Lej rumuński , 1 USD - 4,09 RON
            PAB - Balboa , 1 USD - 1 PAB
            """)
            
            waluta = input("Podaj Skrót waluty : ").upper()
            kwota = float(input("Podaj Kwote :"))
            print(f"{kwota}$ to {Przelicz(kwota, waluta, odp)}{waluta}")
            break
        elif odp == "NIE":
            print("""Podaj jaką walute chcesz rozmienic na dolary amerykańskie :
            THB - Baht Tajski , 1 THB - 0,033 USD
            BTC - Bitcoin , 1 BTC - 55 697,20 USD
            BTN - Ngultrum bhutański , 1 BTN - 0,014 USD
            MRO - Ugija mauretańska , 1 MRO - 0,028 USD
            ETH - Ethereum , 1 ETH - 1783,83 USD
            PLN - Polski złoty , 1 PLN - 0,26 USD
            RON - Lej rumuński , 1 RON  - 0,24 USD
            PAB - Balboa , 1 PAB - 1 USD
            """)
            waluta = input("Podaj Skrót waluty : ").upper()
            kwota = float(input("Podaj Kwote :"))
            print(f"{kwota}{waluta} to {Przelicz(kwota, waluta, odp)}$")
            break
        else: 
            print("Odpowiedz powinna brzmieć Tak lub nie ")


if __name__ == "__main__": 
    Kantor()
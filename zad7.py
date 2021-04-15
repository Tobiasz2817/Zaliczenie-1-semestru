import datetime

def rok_przystepny(R):
    if (R % 4 == 0 and R % 100 != 0) or R % 400 == 0:
        return 29
    else:
        return 28

def miesiace(R, index):
    miesiace = [31, rok_przystepny(R), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return miesiace[index]

def Data_Jutro(D, M, R):
    
    if D + 1 > miesiace(R, M - 1):
        D = 1
        M += 1
        if M > 12:
            M = 1
            R += 1
    else:
        D += 1
    return D, M, R

def Data_Wczoraj(D, M, R):
    if D == 1 and M == 1:
        D = miesiace(R, M - 2)
        M -= 1
        if M < 1:
            M = 12
            R -= 1
    elif D == 1 and M > 1:
        D = miesiace(R, M - 2)
        M -= 1
    else:
        D -= 1
    return D, M, R

def Dzien_Tygodnia_Urodziny(d, m, y, s,tydzien):  
    M = (1 + (9 + m)) % 12
    Y = y - (M > 10)
    C = Y / 100
    D = Y % 100
    if s != 0:
        N = ((13 * M - 1) / 5 + D + D / 4 + C / 4 + 5 * C + d) % 7
    else:
        N = ((13 * M - 1) / 5 + D + D / 4 + 6 * C + d + 5) % 7
    return tydzien[int((7 + N) % 7)]

def Wyznaczanie_wielkanocy(R):
    a = R % 19
    b = int(R / 100)
    c = R % 100
    d = int(b / 4)
    e = b % 4
    f = int((b + 8) / 25)
    g = int((b - f + 1) / 3)
    h = (19 * a + b - d - g + 15) % 30
    i = int(c / 4)
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = int((a + 11 * h + 22 * l) / 451)
    p = (h + l - 7 * m + 114) % 31
    day = p + 1
    month = int(h + l - 7 * m + 114) / 31
    return day, int(month)

def Wczytaj_Wartości():
    dzien = int(input("Podaj dzien:"))
    miesiac = int(input("Podaj miesiac:"))
    rok = int(input("Podaj rok:"))

    return dzien,miesiac,rok

def Aktualny_Dzien_Tygodnia(tydzien):
    return tydzien[datetime.datetime.today().weekday()]


def Wykonaj_I_Wypisz():
    tydzien = ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela",]  
    while(True):
        tab = Wczytaj_Wartości()
        if tab[0] >= 31 or tab[0] <= 0 or tab[1] <=0 or tab[1]>12 or (rok_przystepny(tab[2])<tab[0] and tab[1]==2):
            print("\nPodano Niepoprawne wartości")
            print("\tSpróboj ponownie :")
                        
        else:
            print(f"\nJest to {Dzien_Tygodnia_Urodziny(tab[0],tab[1],tab[2],1,tydzien)}")
            print(f"Jutro będzie :{Data_Jutro(tab[0],tab[1],tab[2])}")
            print(f"Wczoraj był :{Data_Wczoraj(tab[0],tab[1],tab[2])}")
            print(f"Wielkanoc wypada {Wyznaczanie_wielkanocy(tab[2])}")
            print(f"Urodziłem się w dniu {Dzien_Tygodnia_Urodziny(3,9,2000,1,tydzien)} A dziś jest {Aktualny_Dzien_Tygodnia(tydzien)} , Życzę miłego dnia ;)")

            exit(0)

if __name__ == "__main__":

    Wykonaj_I_Wypisz()

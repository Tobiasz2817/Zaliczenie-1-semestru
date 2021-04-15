def Z_Celsjusza_Na(Nazwa, temperatura):

    if Nazwa == "F":
        Z_C_N_F = (temperatura * 1.8) + 32
        if Z_C_N_F <= 32:
            return f"Woda Zamarza aktualnie w {round(Z_C_N_F,2)} stopniach Farenheita"
        elif Z_C_N_F >= 212:
            return f"Woda Wrze aktualnie w {round(Z_C_N_F,2)} stopniach Farenheita"
        else:
            return "Chyba nic nie robi"
    elif Nazwa == "K":
        Z_C_N_K = temperatura + 273.15
        if Z_C_N_K <= 273.15:
            return f"Woda Zamarza aktualnie w {round(Z_C_N_K,2)} stopniach Kelvina"
        elif Z_C_N_K >= 373.15:
            return f"Woda Wrze aktualnie w {round(Z_C_N_K,2)} stopniach Kelvina"
        else:
            return "Chyba nic nie robi"
    elif Nazwa == "R":
        Z_C_N_R = (temperatura + 273.15) * 1.8
        if Z_C_N_R <= 491.67:
            return f"Woda Zamarza aktualnie w {round(Z_C_N_R,2)} stopniach Rankine'a"
        elif Z_C_N_R >= 671.67:
            return f"Woda Wrze aktualnie w {round(Z_C_N_R,2)} stopniach Rankine'a"
        else:
            return "Chyba nic nie robi"
    else:
        return "Jakiś Error ?"


def Z_Kelvina_Na(Nazwa, temperatura):
    if Nazwa == "F":
        Z_K_N_F = (temperatura * 1.8) - 459.67
        if Z_K_N_F <= 32:
            return f"Woda Zamarza aktualnie w {round(Z_K_N_F,2)} stopniach Farenheita"
        elif Z_K_N_F >= 212:
            return f"Woda Wrze aktualnie w {round(Z_K_N_F,2)} stopniach Farenheita"
        else:
            return "Chyba nic nie robi"
    elif Nazwa == "C":
        Z_K_N_C = temperatura - 273.15
        if Z_K_N_C <= 0:
            return f"Woda Zamarza aktualnie w {round(Z_K_N_F,2)} stopniach Celsjusza"
        elif Z_K_N_C >= 100:
            return f"Woda Wrze aktualnie w {round(Z_K_N_F,2)} stopniach Celsjusza"
        else:
            return "Chyba nic nie robi"
    elif Nazwa == "R":
        Z_K_N_R = ((temperatura - 273.15) * 1.8000) + 491.67
        if Z_K_N_R <= 491.67:
            return f"Woda Zamarza aktualnie w {round(Z_K_N_R,2)} stopniach Rankine'a"
        elif Z_K_N_R >= 671.67:
            return f"Woda Wrze aktualnie w {round(Z_K_N_R,2)} stopniach Rankine'a"
        else:
            return "Chyba nic nie robi"
    else:
        return "Jakiś Error ?"


def Z_Fahrenheita_Na(Nazwa, temperatura):
    if Nazwa == "C":
        Z_F_N_C = (temperatura - 32) / 1.8
        if Z_F_N_C <= 0:
            return f"Woda Zamarza aktualnie w {round(Z_F_N_C,2)} stopniach Celsjusza"
        elif Z_F_N_C >= 100:
            return f"Woda Wrze aktualnie w {roundZ_F_N_C} stopniach Celsjusza"
        else:
            return "Chyba nic nie robi"
    elif Nazwa == "K":
        Z_F_N_K = (temperatura + 459.67) * 5 / 9
        if Z_F_N_K <= 273.15:
            return f"Woda Zamarza aktualnie w {round(Z_F_N_K,2)} stopniach Kelvina"
        elif Z_F_N_K >= 373.15:
            return f"Woda Wrze aktualnie w {round(Z_F_N_K,2)} stopniach Kelvina"
        else:
            return "Chyba nic nie robi"
    elif Nazwa == "R":
        Z_F_N_R = (temperatura - 32)+ 491.67
        if Z_F_N_R <= 491.67:
            return f"Woda Zamarza aktualnie w {round(Z_F_N_R,2)} stopniach Rankine'a"
        elif Z_F_N_R >= 671.67:
            return f"Woda Wrze aktualnie w {round(Z_F_N_R,2)} stopniach Rankine'a"
        else:
            return "Chyba nic nie robi"
    else:
        return "Jakiś Error ?"


def Z_Rankine_Na(Nazwa, temperatura):
    if Nazwa == "C":
        Z_R_N_C = (temperatura / 1.8) - 273.15
        if Z_R_N_C <= 0:
            return f"Woda Zamarza aktualnie w {round(Z_R_N_C,2)} stopniach Celsjusza"
        elif Z_R_N_C >= 100:
            return f"Woda Wrze aktualnie w {round(Z_R_N_C,2)} stopniach Celsjusza"
        else:
            return "Chyba nic nie robi"
    elif Nazwa == "K":
        Z_R_N_K = ((temperatura - 491.67) / 1.8000) + 273.15
        if Z_R_N_K <= 273.15:
            return f"Woda Zamarza aktualnie w {round(Z_R_N_K,2)} stopniach Kelvina"
        elif Z_R_N_K >= 373.15:
            return f"Woda Wrze aktualnie w {round(Z_R_N_K,2)} stopniach Kelvina"
        else:
            return "Chyba nic nie robi"
    elif Nazwa == "F":
        Z_R_N_F = temperatura - 459.67
        if Z_R_N_F <= 32:
            return f"Woda Zamarza aktualnie w {round(Z_R_N_F,2)} stopniach Fahrenheita"
        elif Z_R_N_F >= 212:
            return f"Woda Wrze aktualnie w {round(Z_R_N_F,2)} stopniach Fahrenheita"
        else:
            return "Chyba nic nie robi"
    else:
        return "Jakiś Error ?"


def Wypisz_Wykonaj():

    while True:
        Nazwa1 = input(
            "Przelicznik temperatur | Podaj z jakiej  (Kelvina - K ,Celsjusza - C ,Farenheita - F, Rankine - R ) :"
        ).upper()
        Nazwa = input(
            "Na jaką temperature chcesz przeliczyć (Kelvina - K ,Celsjusza - C ,Farenheita - F, Rankine - R ) :"
        ).upper()

        if Nazwa1 == "C" and ( Nazwa == "R" or Nazwa == "K" or Nazwa == "F" ):
            temperatura = float(
                input(
                    f"Podaj wartosc w stopniach {Nazwa1} a przeliczymy je na stopnie {Nazwa} :"
                )
            )
            print(Z_Celsjusza_Na(Nazwa, temperatura))
            break
        elif Nazwa1 == "K" and ( Nazwa == "C" or Nazwa == "R" or Nazwa == "F" ):
            temperatura = float(
                input(
                    f"Podaj wartosc w stopniach {Nazwa1} a przeliczymy je na stopnie {Nazwa} :"
                )
            )
            print(Z_Kelvina_Na(Nazwa, temperatura))
            break
        elif Nazwa1 == "F" and ( Nazwa == "C" or Nazwa == "K" or Nazwa == "R" ):
            temperatura = float(
                input(
                    f"Podaj wartosc w stopniach {Nazwa1} a przeliczymy je na stopnie {Nazwa} :"
                )
            )
            print(Z_Fahrenheita_Na(Nazwa, temperatura))
            break
        elif Nazwa1 == "R" and ( Nazwa == "C" or Nazwa == "K" or Nazwa == "F" ):
            temperatura = float(
                input(
                    f"Podaj wartosc w stopniach {Nazwa1} a przeliczymy je na stopnie {Nazwa} :"
                )
            )
            print(Z_Rankine_Na(Nazwa, temperatura))
            break
        else:
            print("Niepoprawna litera : Prosze podać prawidłową litere (K,C,F,R)")


if __name__ == "__main__":
    Wypisz_Wykonaj()

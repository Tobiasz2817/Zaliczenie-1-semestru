import json


def Pokaz(Quiz,punkty):
    print(Quiz["pytanie"])
    print("A." + Quiz["A."])
    print("B." + Quiz["B."])
    print("C." + Quiz["C."])
    print("D." + Quiz["D."])
    odpowiedz= input("Odpowiedz Brzmi :").upper()
    if (odpowiedz==Quiz["poprawna_odpowiedz"]):
        print("Poprawna Odpowiedz , Brawo !!!")
        punkty+=1
    else:
        print("Niestety się nie udało :(")
    print("\n")
    return punkty

def WyznaczOcene(punkty):
    if punkty < 2:
        return "niedostateczny"
    elif punkty < 4:
        return "dopuszczajacy"
    elif punkty < 6:
        return "dostateczny"
    elif punkty < 8:
        return "dobry"
    elif punkty < 9:
        return "bardzo dobry"
    else:
        return "celujacy"

def QuizInformatyczny():
    punkty=0
    podlicz_punkty=0
    with open("zad3.json") as f:
        pytanie = json.load(f)
    for state in pytanie:
         podlicz_punkty+=Pokaz(state,punkty) 
    ocena=WyznaczOcene(podlicz_punkty)
    print("Ocena wynosi : " + ocena)

if __name__ == "__main__": 
    QuizInformatyczny()
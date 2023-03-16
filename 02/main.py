if __name__ == '__main__':
    # zadanie 1
    zmienna1 = 'Python 2023'
    zmienna2 = 'Python 2023'
    zmienna3 = 'Python 2023'

    print(zmienna1 == zmienna2)
    print(zmienna2 == zmienna3)
    print(type(zmienna1))
    print(type(zmienna2))
    print(type(zmienna3))
    print(hex(id(zmienna1)))
    print(hex(id(zmienna2)))
    print(hex(id(zmienna3)))

    zmienna3 = 'Java 11'
    print(zmienna1 == zmienna2)
    print(zmienna2 == zmienna3)
    print(type(zmienna1))
    print(type(zmienna2))
    print(type(zmienna3))
    print(hex(id(zmienna1)))
    print(hex(id(zmienna2)))
    print(hex(id(zmienna3)))
    print()

    # zadanie 2
    number1 = int(input("liczba 1: "))
    number2 = int(input("liczba 2: "))
    operator = input("operator: ")

    if operator == '-':
        print(number1 - number2)
    elif operator == '+':
        print(number1 + number2)
    elif operator == '/':
        print(number1 / number2)
    elif operator == '*':
        print(number1 * number2)

    # zadanie 3
    questions = {"Podaj imie i nazwisko ": [],
                 "Jaki jest najczęstszy sposób spędzania wolnego czasu dla Ciebie: ": [
                     "1. oglądanie telewizji/filmów/seriali", "2. czytanie książek/czasopism", "3. uprawianie sportu"],
                 "W jakich okolicznościach czytasz książki najczęściej? ": ["1. podczas podróży",
                                                                            "2. w czasie wolnym (po pracy, na urlopie)",
                                                                            "3. w ogóle nie czytam"],
                 "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? ": [
                     "1. chęć poszerzenia wiedzy", "2. czytanie to moje hobby",
                     "3. konieczność nauki w związku z wykonywaną pracą/studiami"],
                 "Po książki w jakiej formie sięgasz najczęściej? ": ["1. papierowej (tradycyjnej)",
                                                                      "2. e-booki na tablecie/telefonie",
                                                                      "3. e-booki na specjalnym czytniku (np. Kindle)"],
                 "Ile książek czytasz średnio w ciągu roku? ": ["1. żadnej w całości - jedynie fragmenty", "2. 2 lub 3",
                                                                "3. 4-10"],
                 "Jak często średnio czytasz książki? ": ["1. codziennie", "2. raz w miesiącu", "3. raz na rok"],
                 "Po jakie gatunki książek sięgasz najczęściej? ": ["1. kryminały/thrillery", "2. naukowe", "3. fantastykę"]}
    for k, v in questions.items():
        print(f"pytanie: {k}")
        for a in v:
            print(a)
        print(f"odpowiedz:", end=" ")
        input()

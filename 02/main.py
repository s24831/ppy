if __name__ == '__main__':
    #zadanie 1
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

    #zadanie 2
    number1 = int(input("liczba 1"))
    number2 = int(input("liczba 2"))
    operator = input("operator")

    if operator == '-':
        print(number1 - number2)
    elif operator == '+':
        print(number1 + number2)
    elif operator == '/':
        print(number1 / number2)
    elif operator == '*':
        print(number1 * number2)

    #zadanie 3
    questions = [
        'Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:',
        'W jakich okolicznościach czytasz książki najczęściej?',
        'Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?',
        'Po książki w jakiej formie sięgasz najczęściej?',
        'Ile książek czytasz średnio w ciągu roku?',
        'Jak często średnio czytasz książki?',
        'Po jakie gatunki książek sięgasz najczęściej?'
    ]
    for i in range(7):
        response = input(f"pytanie: {questions[i]}")
        print(f"odpowiedz: {response}")

# Lista1

'''
UWAGA! Nie należy zmieniać nazw funkcji, oraz wartości zmiennych podanych w pliku
poza wartościami ze stringiem "PODAJ WYNIK" - w tych zmiennych należy przechowywać wynik
dotyczący poszczególnych zadań w_1, w_2 ... w_6.

Ciało funkcji wpisujemy w kodzie zamiast "pass".

Wyniki z każdego zadania powinny wyświetlać się w jednej linijce.
Nie należy wyświetlań nic poza wynikiem działania kodu z poszczególnych zadań
w kolejności tak jak w pliku.
Plik należy zapisać w postaci: imie_nazwisko_lista1.py
'''

# 1. Ile unikatowych elementów znajduje się w liście:
# 1 pkt
import random

lista_1 = [0, 7, 8, 3, 3, 0, 7, 0, 3]

w_1 = len(set(lista_1))
print(w_1)

# 2. Napisz kod, który podmieni losowy znak ze stringa
s_2 = "ala ma kota"
# na '0':
# 2 pkt

w_2 = s_2.replace(random.choice(s_2), '0', 1)
print(w_2)

# 3. Napisz kod który podmieni z lista_3 język programowania R na JS, następnie wyświetl podmieniony JS.
# Przed JS nadal musi znajdować się python w strukturze takiego samego typu jak w przykladowej lista_3.
# 2pkt
lista_3 = [[{1: 'java', 0: ('python', 'R')}, 'c++'], ['word', 'excel']]
lista_3[0][0][0] = ('python', 'JS')
w_3 = lista_3[0][0][0][1]
print(w_3)

# 4. Jakiego typu dane z poniższych nie mogą być kluczami słownika?
# boolean,float,int,string,tuple,list,set. Odpowiedź umieśc w stringu w_4
# 1 pkt

w_4 = "list, set"
print(w_4)

# 5. Dla stringa wypisz
# ile razy pojawił się dany znak, w kolejności alfabetycznej.
# Użyj słownika - wynik również ma być słownikiem
# 2 pkt

s_5 = "ala ma kota imie ma macko"

w_5 = dict(sorted({v: s_5.count(v) for v in set(s_5)}.items()))
print(w_5)

# 6. Napisz kod który sprawdzi, czy w poprzednim stringu s_5,
# jakikolwiek znak wystąpił dokładnie 3 razy. Wyświetl Tak jeżeli wystąpił,
# Nie jeżeli nie wystąpił.
# 1 pkt

w_6 = "Tak" if 3 in {v: s_5.count(v) for v in set(s_5)}.values() else "Nie"
print(w_6)


# 7. Napisz funkcję sprawdzającą czy podane słowa/zdania są palindromem
# i zwróci True lub False ( jest/ nie jest)
# pomiń znaki nie będące literami.
# 3pkt

def palindrom(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return s == s[::-1]


s_7_1 = "Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindrom(s_7_1))


# 8. Napisz funkcję, która wyświetli
# wszystkie liczby od 1 do n, jednak jeżeli liczba jest podzielna przez:
# trzy – wypisze „Fizz”,
# pięć – wypisze „Buzz”,
# trzy i pięć wypisz „FizzBuzz”.
# wszystkie liczby/słowa mają zostać wyświetlone w jednej linii, oraz być rozdzielone przecinkiem
# BEZ spacji
# 2 pkt

def fizzbuzz(n):
    to_return = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            to_return.append("FizzBuzz")
        elif i % 5 == 0:
            to_return.append("Buzz")
        elif i % 3 == 0:
            to_return.append("Fizz")
        else:
            to_return.append(f"{i}")
    return ','.join(to_return)


n_8 = 16
print(fizzbuzz(n_8))

# 9. Napisz funkcję zwracającą n-ty element ciągu Fibonacciego
# bez rekurencji:
# 3 pkt

n_9 = 6


def fibonacci(n):
    if n < 1:
        return 0
    prev, current = 0, 1
    for i in range(n - 1):
        prev, current = current, prev + current
    return current


print(fibonacci(n_9))


# 10. Napisz funkcję, która dla podanej posortowanej listy
# zwróci index wyszukiwanego elementu za pomocą wyszkukiwania binarnego,
# lub zwróci None gdy nie ma elementu w liscie:
# 3 pkt


def binary_search(lista, e):
    left = 0
    right = len(lista) - 1
    while left <= right:
        mid = (left + right) // 2
        if lista[mid] == e:
            return mid
        elif lista[mid] < e:
            left = (left + right) // 2 + 1
        else:
            right = (left + right) // 2 - 1
    return None


l_10 = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
print(binary_search(l_10, 2))

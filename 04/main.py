import math
from lib2to3.pgen2.tokenize import String


def panel_calc(room_length: float, room_height: float, plate_length: float, plate_height: float,
               plate_count: int) -> int:
    room_surface = room_length * room_height * 1.1
    plate_surface = plate_length * plate_height
    number_of_plates = room_surface / plate_surface
    return math.ceil(number_of_plates / plate_count)


def is_prime(*args) -> None:
    for number in args:
        is_it_prime = True
        if number > 1:
            for num in range(2, number):
                if number % num == 0:
                    is_it_prime = False
                    print(f"{number} is not prime")
                    break
            if is_it_prime:
                print(f"{number} is prime")
        else:
            print(f"{number} is not prime")


def do_cezar(message: str, count: int, optional_coding=[]) -> str:
    message_temp = list(message.lower())
    if not optional_coding:
        for i in range(len(message_temp)):
            if message_temp[i].isalpha():
                message_temp[i] = chr(((ord(message_temp[i]) - ord("a") + count) % 26) + ord("a"))
        return "".join(message_temp)
    else:
        for i in range(len(message_temp)):
            if message_temp[i] == optional_coding[0]:
                message_temp[i] = optional_coding[1]
        return "".join(message_temp)


if __name__ == '__main__':
    print(panel_calc(10, 10, 1, 1, 10))
    is_prime(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(do_cezar("message z!", 1))

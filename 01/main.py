import webbrowser
import requests
from pygame import mixer

#zadanie 3
mixer.init()
mixer.music.load(".\song.mp3")
mixer.music.play()

#zadanie 4
for i in range(3):
    pageUrl = input("Podaj adres strony: ")
    date = input("Podaj date: ")

    url = "http://archive.org/wayback/available?url=" + pageUrl + "&timestamp=" + str(date)

    page = requests.get(url).json()["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)
    print()

#zadanie 5
# W Pythonie kod zrodłowy jest przetwarzany przez interpreter, ktory przetwarza kod linia po linii w czasie rzeczywistym,a następnie wykonuje go bezposrednio
# Interpreter jest programem, ktory tlumaczy kod zrodlowy na kod maszynowy

# W Java kod źródłowy jest kompilowany do kodu bajtowego, który jest następnie wykonywany przez maszynę wirtualną Javy
# JVM jest programem, ktory dziala multiplatformowo i zapewnia warstwe miedzy kodem bajtowym a komputerem
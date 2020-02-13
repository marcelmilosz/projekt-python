# Data Science, niestacjonarne
# Marcel Miłosz

# Biblioteki
import math
import matplotlib.pyplot as plt
import numpy

# Wylosowane zadania (bez zadań projektówych)
# [2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 22, 27]

## 2. Korzystając z pojęcia funkcji utwórz skrypt, który będzie miał możliwość zamiany temperatury pomiędzy skalami Celsjusza i Fahrenheita (w obie strony).
# C = (F-32)x(5/9), F = (C*9/5)+32
def zad2_Celsjusze(F):  # F - Użytkownik podaje temperature w Fahrenheita'h i otrzymuje w Celsjuszach
    return (F - 32) * (5/9)

def zad2_Fahrenheit(C): # C - Użytkownik podaje temperature w Celsjuszach i otrzymuje w Fahrenheita'h
    return (C * 9/5) + 32

# print(zad2_Celsjusze(2))
# print(zad2_Fahrenheit(2))

## 4. Utwórz skrypt do znajdowania miejsc zerowych trójmianu kwadratowego x1 = (-b+sqrt(b*b-4*a*c))/(2*a) x2 = (-b-sqrt(b*b-4*a*c))/(2*a)
def zad4_MiejscaZerowe(a, b, c):    # ax^2 + bx + c
    delta = b ** 2 - (4 * a * c)

    if delta < 0: return "Delta < 0! Brak rozwiązań"    # a = 1, b = 2, c = 2
    elif delta == 0: return "Delta = 0, istnieje jedno miejsce zerowe: \n| x0: " + str(round((-b) / (2 * a)))   # a = 1, b = 2, c = 1
    elif delta > 0: return "Delta > 0!, istnieją dwa miejsca zerowe: \n| x1: " + str(round(-b - math.sqrt(delta), 2) / (2 * a)) + " \n| x2: " + str(round(-b + math.sqrt(delta), 2) / (2 * a))  # a = 1, b = 3, c = 1

# print(zad4_MiejscaZerowe(1, 2, 1))

## 5. Utwórz skrypt, który będzie komunikować, czy wprowadzona liczba jest dodatnia czy nie
def zad5_czyDodatnia(a):
    if a > 0: return f"Podana liczba: {a} jest dodatnia!"
    elif a < 0: return f"Podana liczba: {a} jest ujemna!"
    else: return "Zero nie jest ani dodatnie ani ujemne!"

# print(zad5_czyDodatnia(5))

## 7. Utwórz skrypt z interfejsem tekstowym, który pobierze od użytkownika zdanie i wyświetli w kolejnych wierszach litery tego zdania w odwróconej kolejności
def zad7_OdwrocKolejnosc():
    s = input("Podaj tekst: ")
    for i in range(0, len(s)):
        print(s[len(s) - i - 1])

# zad7_OdwrocKolejnosc()

## 9. Utwórz skrypt z interfejsem tekstowym, który wyliczy sumę n kolejnych liczb (użytkownik podaje pierwszą i ostatnią liczbę sumy).
# Uwaga - w zadaniu należy zbudować funkcję własną realizującą dane zadanie
def zad9_WyliczSume():
    a = int(input("Podaj początkową liczbę: ")) # a -> od
    b = int(input("Podaj końcową liczbę: "))    # b -> do
    suma = 0

    if a < b:
        for i in range(a, b + 1): suma += i
    elif a > b:
        for i in range(a, b - 1, -1): suma += i
    else: suma = a

    return f"\nSuma liczb od {a} do {b} wynosi: {suma}"

# print(zad9_WyliczSume())

## 11. Utwórz skrypt z interfejsem tekstowym który obliczy silnię od danego argumentu. Wykonać zadanie na dwa sposoby - iteracyjnie i rekurencyjnie
def zad11_silnia_Iter():
    n = int(input("Podaj liczbę: "))
    silnia = 1
    for i in range(1, n + 1):
        silnia *= i

    return f"Silnia z {n}! to: {silnia}"

def zad11_silnia_Reku(n):
    if n > 1: return n * zad11_silnia_Reku(n - 1)
    else: return 1

# print(zad11_silnia_Iter())                                                                # Silnia Iteracyjnie
# print("Silnia wynosi: " + str(zad11_silnia_Reku(n = int(input("Podaj liczbę: ")))))       # Silnia Rekurencyjnie

## 12. Utworzyć skrypt z interfejsem tekstowym obliczający n-ty element ciągu Fibonacciego - wykonać zadanie iteracyjnie i rekurencyjnie
def zad12_Fibb_Iter():
    n = int(input("Podaj n: "))
    Fibb = [1, 1]

    if n < 2:
        return f"Dla 'n' = {n}, Liczba wynosi: 1"
    else:
        for i in range(1, n - 1):
            Fibb.append(Fibb[i] + Fibb[i - 1])

        return f"Dla 'n' = {n}, Liczba wynosi: {Fibb[len(Fibb) - 1]}"

def zad12_Fibb_Reku(n):
    if n < 2:
        return 1

    return zad12_Fibb_Reku(n - 1) + zad12_Fibb_Reku(n - 2)

# print(zad12_Fibb_Iter())                                        # Fibbonaci Iteracyjnie
# print(zad12_Fibb_Reku(n = int(input("Podaj n: ")) - 1))         # Fibbonaci Rekurencyjnie

## 14. Utworzyć skrypt z interfejsem tekstowym, który będzie zwracać wiersz n-tego rzędu z trójkąta Pascala
# (użytkownik podaje n, program zwraca odpowiadający wiersz trójkąta)
def zad14_Pascal(): # Do tego zadania użyję wcześniejszej funkcji z silnią 'zad11_silnia_Reku(n)' oraz wzoru na Dwumian Newtona
    a = int(input("Podaj jaki wiersz z trójkąta Pascala chcesz otrzymac: "))
    wiersz = []

    for n in range(0, a): # n = wiersz, k = kolumna (od 0)
        print(str(' ' * (a - n)), end = '')                                                             # (Dodanie spacji)

        for k in range(0, n + 1):
            newton = int((zad11_silnia_Reku(n)) / (zad11_silnia_Reku(k) * zad11_silnia_Reku(n - k)))    # Obliczenie konkretnej liczby ze wzoru
            print(newton, end = ' ')

            if n == a - 1: wiersz.append(newton)                                                        # Zapisanie konkretnego wiersza

        print()

    return f'\nTwoj wiersz ({a}) to: {wiersz}'

# print(zad14_Pascal())

## 16. Utwórz funkcję własną, która jako argument przyjmować będzie listę argumentów i wartości, a jako wynik będzie wyświetlać sformatowany wykres
# (stosowny zakres, opis, kolory, legenda)
def zad16_Wykres(arrX, arrY):
    if len(arrX) != len(arrY): return print("Ilość argumentów jest różna od ilości wartości!")

    plt.plot(arrX, arrY, label = 'Legenda XY', color = '#bd271c')
    plt.plot([i * 2 for i in arrX], [i * 2 for i in arrY], label = 'Legenda XY * 2', color = '#1cbd7d')
    plt.xlabel("Lista X")
    plt.ylabel("Lista Y")
    plt.legend()
    plt.show()

# zad16_Wykres([1, 2, 3, 4, 10, 12, 14, 15], [2, 4, 2, 4, 4, 8, 1, 9])

## 17. Utwórz funkcję, która będzie generować listy danych do wykreślenia w oparciu o:
# a) fukcję liniową ax+b
# b) funkcję kwadratową ax^2+bx+c
# c) funkcję odwrotnie-potęgową a/x^n
# Każda z fukcji powinna przyjmować parametry równania, natomiast zwracać powinna dwie listy - x i y, które następnie będzie można wykreślić na wykresie

def zad17_Funkcja_Liniowa(a, b):    # y = ax + b
    X = []
    Y = []

    for i in range(-5, 5 + 1):
        X.append(i)
        Y.append((a * i + b))

    print("Funkcja Liniowa: ")
    print(f"Wygenerowany X: {X}")
    print(f"Wygenerowany Y: {Y}")

    plt.plot(X, Y, color='#bd271c')
    plt.show()

def zad17_Funkcja_Kwadratowa(a, b, c):    # y = ax^2 + bx + c
    X = []
    Y = []

    for i in range(-5, 5 + 1):
        X.append(i)
        Y.append((a * (i ** 2)) + (b * i) + c)

    print("Funkcja Kwadratowa: ")
    print(f"Wygenerowany X: {X}")
    print(f"Wygenerowany Y: {Y}")

    plt.plot(X, Y, color='#bd271c')
    plt.show()

def zad17_Funkcja_OdwPotegowana(a, n):    # y = a / x^n
    X = []
    Y = []

    for i in range(-5, 5 + 1):
        if i == 0: continue
        X.append(i)
        Y.append((a / (i ** n)))

    print("Funkcja Odwrotnie potęgowana: ")
    print(f"Wygenerowany X: {X}")
    print(f"Wygenerowany Y: {Y}")

    plt.plot(X, Y, color='#bd271c')
    plt.show()

# zad17_Funkcja_Liniowa(2, 3)
# zad17_Funkcja_Kwadratowa(5, 2, -1)
# zad17_Funkcja_OdwPotegowana(2, 3)

## 19. Korzystając ze słownika, utwórz funkcję, która będzie zwracać liczbę dni danego miesiąca w roku
def zad19_Slownik(s):
    dictio = {
        "Styczeń" : 31, "Luty" : 29, "Marzec" : 31,
        "Kwiecień": 30, "Maj": 31, "Czerwiec": 30,
        "Lipiec": 31, "Sierpień": 31, "Wrzesień": 30,
        "Październik": 31, "Listopad": 30, "Grudzień": 31
    }

    return f"Liczba dni w '{s}' wynosi: {dictio[s]}"

# print(zad19_Slownik("Grudzień"))

## 22. Utwórz fukcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, a jej wynikiem
# będzie mediana (skorzystaj z metody sort działającej na standardowych listach)
def zad22_Mediana(arr):
    print(f"Podana lista: {arr}")
    arrSort = sorted(arr)
    print(f"Posortowana lista: {arrSort}")

    if len(arrSort) % 2 == 0:
        Me = (arrSort[int(len(arrSort) / 2)] + arrSort[int((len(arrSort) / 2) - 1)]) / 2
    else:
        Me = arrSort[int(len(arrSort) / 2)]

    return Me

# print("Mediana wynosi: " + str(zad22_Mediana([4, 2.0, 12, 5.7, 3, 3.5, 5, 18])))

## 27. Utwórz funkcję, która jako argument będzie przyjmować listę liczb zmiennoprzecinkowych, a jej wynikiem będzie czwarty moment centralny (kurtoza)
def zad27_Kurtoza(arr):
    X = arr                             # Podane wartości
    Sr_X = numpy.mean(X)                # Średnia
    X_min_SrX_Kwad = []                 # (Xi - ŚrX) ^ 2
    X_min_SrX_Czwa = []                 # (Xi - ŚrX) ^ 4

    for i in range(0, len(X)):
        X_min_SrX_Kwad.append((X[i] - Sr_X) ** 2)
        X_min_SrX_Czwa.append((X[i] - Sr_X) ** 4)

    Kurtoza = (1/len(X) * sum(X_min_SrX_Czwa)) / ((1/len(X) * sum(X_min_SrX_Kwad)) ** 2) - 3

    print(f"Podane X {X}")
    print(f"Średnia: {Sr_X}")
    print(f"(Xi - ŚrX) ^ 2: {X_min_SrX_Kwad}")
    print(f"(Xi - ŚrX) ^ 4: {X_min_SrX_Czwa}")
    print(f"Kurtoza: {Kurtoza}")

# zad27_Kurtoza([1, 2, 3, 3, 4, 4, 4, 5])
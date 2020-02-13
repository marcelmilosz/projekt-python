# Data Science, niestacjonarne
# Marcel Miłosz

# Biblioteki
import math

# Wylosowane projekty
# [2, 4]

# ! Tutaj rozwiązuje projekt nr. 2 !

## 2. Utwórz klasę Vector2D. Wykorzystaj całą wiedzę jaką posiadasz na temat wektorów na płaszczyźnie. Zdefiniuj wszystkie znane Ci operacje.
class Vector2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def zapiszWektor(self):                         # Zapisuje wektor w postaci listy
        return [self.x, self.y]

    def pomnozPrzezLiczbe(self, n):                 # Pomnoż przez liczbę (podajemy n)
        Wynik = [(self.x * n), (self.y * n)]
        print(f"Pomnożenie przez {n} * [{self.x}, {self.y}] = {Wynik}")

    def dodajWektor(self, B):                       # Dodaj wektor (B to jest drugi wektor)
        A = [self.x, self.y]
        Wynik = [A[0] + B[0], A[1] + B[1]]
        print(f"Suma {A} + {B} = {Wynik}")

    def odejmijWektor(self, B):                     # Odejmij wektor (B to jest drugi wektor)
        A = [self.x, self.y]
        Wynik = [A[0] - B[0], A[1] - B[1]]
        print(f"Różnica {A} - {B} = {Wynik}")

    def iloczynSkalarny(self, B):                   # Oblicz iloczyn skalarny
        A = [self.x, self.y]
        Wynik = A[0] * B[0] + A[1] * B[1]
        print(f"Iloczyn skalarny {A} * {B} = {Wynik}")

    def obliczDlugoscWektora(self):                 # Oblicz długość wektora
        Wynik = math.sqrt((self.x ** 2) + (self.y ** 2))
        print(f"Długość [{self.x}, {self.y}] = {round(Wynik, 2)}")


V1 = Vector2D(2, 3)                                 # Stowrzenie wektora 2D (2, 3)
V2 = Vector2D(5, -2)                                # Stworzenie wektora 2D (5, -2)

print("Wektor A: " + str(V1.zapiszWektor()))        # Metoda zapiszWektor() zwraca listę np. (2, 3) --> [2, 3]
print("Wektor B: " + str(V2.zapiszWektor()))        # Metoda zapiszWektor() zwraca listę np. (5, -2) --> [5, -2]

# V1.dodajWektor(V2.zapiszWektor())                   # Metoda dodająca dwa wektory (V1 + (W argumencie podajemy drugi jako lista dwuwymiarowa))
# V1.odejmijWektor(V2.zapiszWektor())                 # Metoda odejmująca dwa wektory (V1 + (W argumencie podajemy drugi jako lista dwuwymiarowa))
# V1.iloczynSkalarny(V2.zapiszWektor())               # Metoda iloczynu skalarnego dwóch wektorów (V1 + (W argumencie podajemy drugi jako lista dwuwymiarowa))
# V1.pomnozPrzezLiczbe(5)                             # Metoda która mnoży wektor przez liczbę (skalar)
# V1.obliczDlugoscWektora()                           # Metoda licząca długość wektora
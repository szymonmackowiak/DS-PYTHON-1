import matplotlib.pyplot as plt

class Prostokat():
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.bokA = b[0] - a[0]
        self.bokB = d[1] - a[1]
        
    def boki(self):
        return [self.bokA, self.bokB]
    
    def pole(self):
        return self.bokA*self.bokB
    
    def obwod(self):
        return 2*self.bokA + 2*self.bokB
    
    def rysuj(self):
        plt.axes()
        line = plt.Line2D((self.a[0], self.a[1]), (self.b[0], self.b[1]), lw=1.5)
        plt.gca().add_line(line)
        line = plt.Line2D((self.b[0], self.b[1]), (self.c[0], self.c[1]), lw=1.5)
        plt.gca().add_line(line)
        line = plt.Line2D((self.c[0], self.c[1]), (self.d[0], self.d[1]), lw=1.5)
        plt.gca().add_line(line)
        line = plt.Line2D((self.d[0], self.d[1]), (self.a[0], self.a[1]), lw=1.5)
        plt.gca().add_line(line)
        plt.axis('scaled')
        plt.show()
        
class ProstyProstokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def obwod(self):
        return 2*self.a+2*self.b

    def pole(self):
        return self.a*self.b

class ProstyKwadrat(ProstyProstokat):
    def __init__(self, a):
        super().__init__(a, a)
        

class Ulamek():
    def __init__(self, licznik=0, mianownik=1):
        self.licznik = licznik
        self.mianownik = mianownik
    
    def dodajUlamek(self, b):
        self.licznik = self.licznik*b.mianownik + b.licznik*self.mianownik
        self.mianownik = self.mianownik*b.mianownik
    
    def odejmijUlamek(self, b):
        self.licznik = self.licznik*b.mianownik - b.licznik*self.mianownik
        self.mianownik = self.mianownik*b.mianownik
    
    def pomnozPrzezLiczbe(self, x):
        self.licznik = self.licznik * x
        
    def pomnozPrzezUlamek(self, b):
        self.licznik = self.licznik*b.licznik
        self.mianownik = self.mianownik*b.mianownik
    
    def odwroc(self):
        kopia_licznik = self.licznik
        kopia_mianownik = self.mianownik
        self.licznik = kopia_mianownik
        self.mianownik = kopia_licznik
        
    def poteguj(self, n):
        self.licznik = int(self.licznik**n)
        self.mianownik =int(self.mianownik**n)
        
    def przeciwnosc(self):
        self.licznik = (-1)*self.licznik
    
    def wyswietl(self):
        return (self.licznik, self.mianownik)



















import numpy as np

class Perceptron():
   
    def __init__(self, n, c):
        self.stala_uczenia = c
        self.liczba_wejsc = n
        self.waga = []
        for i in range(self.liczba_wejsc):
            self.waga.append(2*np.random.rand(1)[0]-1)
    
    def aktywacja(self, suma):
        if suma>0:
            return 1
        else:
            return -1
        
    def iloczynSkalarny(self, x):
        suma = 0
        for i in range(self.liczba_wejsc):
            suma = suma + x[i]*self.waga[i]
        return suma
    
    def odpowiedz(self, x):
        suma = self.iloczynSkalarny(x)
        return self.aktywacja(suma)


    def dopasuj(self, x, poprawna_odp):
        odp = self.odpowiedz(x)
        blad = poprawna_odp - odp
        for i in range(self.liczba_wejsc):
            self.waga[i] = self.waga[i] + self.stala_uczenia*blad*x[i]
            

def cel(xp, yp):
    y_linii = xp
    if (y_linii - yp)>0:
        return -1
    else:
        return 1

p = Perceptron(3, 0.05)    

for i in range(500):
    x = []
    x.append(40*np.random.rand(1)[0]-20)
    x.append(40*np.random.rand(1)[0]-20)
    x.append(1)
    
    poprawna_odp = cel(x[0], x[1])
    
    p.dopasuj(x, poprawna_odp)
    
        
        
        
        

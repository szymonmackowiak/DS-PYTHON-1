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
        
        
        
#    def strojenie(self, x, poprawna_odp):
#        odp = self.odpowiedz(x)
#        blad = poprawna_odp - odp
#        for i in range(self.liczba_wejsc):
#            self.waga[i] = self.waga[i] + self.stala_uczenia*blad*x[i]
        
        
        

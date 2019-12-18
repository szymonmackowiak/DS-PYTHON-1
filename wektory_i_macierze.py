import numpy as np
import math

class Vector2D():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def display(self):
        print("x="+str(self.x)+", y="+str(self.y))
  
    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        
    def substr(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        
    def multByNumber(self, a):
        self.x = a*self.x
        self.y = a*self.y
        
    def dotProd(self, other):
        return self.x*other.x + self.y*other.y 
    
    def rotate(self, alfa):
        alfaDeg = alfa*math.pi/180
        sinus = math.sin(alfaDeg)
        cosinus = math.cos(alfaDeg)
        x = self.x
        y = self.y       
        self.x = x*cosinus - y*sinus
        self.y = x*sinus + y*cosinus
        
    def modulus(self):
        return (self.x**2 + self.y**2)**0.5
    
    def opposite(self):
        self.x = -self.x
        self.y = -self.y
        

#Utworzyć metody:
#1. wyswietlanie wspolrzednych
#2. zwiększ o inny wektor (suma)
#3. zmniejsz o inny wektor (różnica)
#4. wymnoz przez liczbę (iloczyn)
#5. wymnoz przez drugi wektor skalarnie
#6. obroc o dany kąt
#7. oblicz modul
#8. wyznacz wektor przeciwny 
        
class Vector3D():
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def display(self):
        print("x="+str(self.x)+", y="+str(self.y) + ", z=" + str(self.z))
        
    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.z = self.z + other.z
        
    def substr(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        self.z = self.z - other.z
        
    def multByNumber(self, a):
        self.x = a*self.x
        self.y = a*self.y
        self.z = a*self.z
        
    def dotProd(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
        
    def crossProd(self, other):
        new_x = self.y*other.z - self.z*other.y
        new_y = self.z*other.x - self.x*other.z
        new_z = self.x*other.y - self.y*other.x
        
        return Vector3D(new_x, new_y, new_z)
    
    def modulus(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
        
    def opposite(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
        
        
#Utworzyć metody:
#1. wyswietlanie wspolrzednych
#2. zwiększ o inny wektor (suma)
#3. zmniejsz o inny wektor (różnica)
#4. wymnoz przez liczbę (iloczyn)
#5. wymnoz przez drugi wektor skalarnie
#6. wymnoz przez drugi wektor wektorowo
#7. oblicz modul
#8. wyznacz wektor przeciwny 
        
class Matrix():
    
    
    def __init__(self, m, n):
        self.m = m #liczba wierzy
        self.n = n #liczba kolumn
    
    def fill(self):
        self.body = []
        for i in range(self.m):
            init_list = []
            for j in range(self.n):
                element = float(input("aij = "))
                init_list.append(element)
            
            self.body.append(init_list)
            
    def zeros(self):
        self.body = []
        for i in range(self.m):
            init_list = []
            for j in range(self.n):
                element = 0
                init_list.append(element)
            
            self.body.append(init_list)
            
    def ones(self):
        self.body = []
        for i in range(self.m):
            init_list = []
            for j in range(self.n):
                element = 1
                init_list.append(element)
            
            self.body.append(init_list)
            
    def unit(self):
        if(self.m == self.n):
            self.body = []
            for i in range(self.m):
                init_list = []
                for j in range(self.n):
                    if (i==j):
                        element = 1
                    else:
                        element = 0
                    init_list.append(element)
            
                self.body.append(init_list)
        else:
            print("dimensions not equal")
            
    def add(self, other):
        if(self.n == other.n and self.m == other.m and len(self.body) != 0 and len(other.body) != 0):
            for i in range(self.m):
                for j in range(self.n):
                    self.body[i][j] = self.body[i][j] + other.body[i][j]
            
        else:
            print("dimensions not equal")
            
    def substr(self, other):
        if(self.n == other.n and self.m == other.m and len(self.body) != 0 and len(other.body) != 0):
            for i in range(self.m):
                for j in range(self.n):
                    self.body[i][j] = self.body[i][j] - other.body[i][j]
            
        else:
            print("dimensions not equal")
            
    def multByNumber(self, a):
        for i in range(self.m):
            for j in range(self.n):
                self.body[i][j] = a*self.body[i][j]            
        
            
    
        
            
    
                
                
                
        
        
        
#Metody dla klasy matrix:
#1. Wypełnij - przyjmuje z klawiatury od użytkownika kolejne elementy macierzy
#2. Wypełnij zerami
#3. Wypełnik jedynkami
#4. Utwórz macierz jednostkową
#5. Dodaj macierz
#6. Odejmij macierz
#7. Pomnóż przez liczbę
#8. Pomnóż przez inną macierz
#9. Znajdź wyznacznik
#10. Znajdź macierz odwrotną


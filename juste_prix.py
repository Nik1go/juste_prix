# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
compléxité de la fontcion  : compté le nombre d'operation elementaire que l'algorithm réalise 


def listepremier(n):
    L =[2]
    entier = 3
    while len(L) <n:
        booleen = True
        k=2
        while k< entier and booleen == True :
            if entier %k ==0:
                booleen = False
            k+=1
        if booleen == True :
            L. append ( entier )
        entier = entier +1   
    return L 
print(listepremier(int(input('entrer la valeur : '))))


def factoriel(n):
    resultat=1
    for i in range (1,n+1):
        resultat = resultat * i
    return resultat 
print(factoriel (int(input('entrer la valeur:'))))


#recursive 
def factoriel2(n):
    resultat=1
    if n==0:
        return 1
    resultat = n*factoriel2(n-1)
    return resultat 
print(factoriel2(int(input('entrer la valeur:'))))

"""

"""
import numpy as np
import matplotlib.pyplot as plt

def H(w, w0, lamda):
    # Calcul de la fonction de transfert H(jw)
    denominator_real = w0**2 - w**2
    denominator_imag = 2 * lamda * w
    denominator = denominator_real + 1j * denominator_imag
    return 1 / denominator

# Paramètres de la fonction de transfert
w0 = 6  # Valeur de ω0
lamda = 0.8 # Valeur de λ l'ammortissement 

# Plage de fréquences
w = np.linspace(0.1, 10, 1000)

# Calcul de la réponse en fréquence
H_freq = H(w, w0, lamda)

# Tracé du module en dB
plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(np.abs(H_freq)))
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Module (dB)')
plt.title('Diagramme de Bode - Module')


# Affichage du graphique
plt.tight_layout()
plt.show()

t = np.linspace(0, 10, 1000)
acceleration = np.sin(t)  # Exemple de fonction d'accélération (à adapter selon tes besoins)

# Diagramme d'accélération en fonction du temps
plt.subplot(2, 1, 2)
plt.plot(t, acceleration)
plt.xlabel('Temps')
plt.ylabel('Accélération')
plt.title('Accélération en fonction du temps')
"""
import random as rd
def juste_prix(n):
    c = rd.randit(1,100)
    print(c)
    for i in range (n):
        d= rd.randint(1,100) 
        print (d)
        if c==d:
            return "gg"
        else : 
            if c<d : 
                print("high")
            else : 
                print("low")
        if i==n-1:
            return "perd"
            
        



        

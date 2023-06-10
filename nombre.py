import random

nombre_choisi = random.randint(1, 6)
resultat = 0

for i in range(3):
    nombre_propose = int(input('Saisir un nombre: '))
    if nombre_propose == nombre_choisi:
        resultat = 1
        break
    elif nombre_propose > nombre_choisi:
        print("C'est moins !")
    elif nombre_propose < nombre_choisi:
        print("C'est plus !")

if resultat ==1:
    print(f"Bravo, le bon nombre est {nombre_choisi}")

else:
    print(f"Perdu, le bon numéro était {nombre_choisi}")
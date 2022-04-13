# Lesoing Valentin et Romain Busso Web_data_ia P2024
# Mini projet 2 - Scrabble - 07/12/2021


import random

# On prépare les variables pour la suite du code.
liste_sneakers = ["nike","adidas","puma","vans","converse","dior","balenciaga"]
trois_mots_aleatoire = []
liste_melange = []
Score = 0 

# print(liste_sneakers)

#enter_word = str(input("entrez votre mot"))

# On définis une fonction qui vas récupérer trois mots dans la liste de base.

def choose_word(liste_sneakers, trois_mots_aleatoire):
  i = 0
  while i < 3:
   mots_aleatoire = liste_sneakers[random.randint(0, len(liste_sneakers)) -1]
   trois_mots_aleatoire.append(mots_aleatoire)
   liste_sneakers.remove(mots_aleatoire)# Supprime les doublons de la liste pour garder 3 mots
   i += 1
  return trois_mots_aleatoire


# On définis une fonction qui va mélanger les mots et enlever les doublons. 

def melange(trois_mots_aleatoire, liste_melange):
    liste_melange = trois_mots_aleatoire[0]+trois_mots_aleatoire[1]+trois_mots_aleatoire[2]
    liste_melange = list(set(liste_melange)) # Détermine les lettres et supprimes les doublons
    random.shuffle(liste_melange)
    return liste_melange


# On pose les bases fonctionnelles du scrabble.

def Scrabble(trois_mots_aleatoire, Score, a):
    while a < 4:
        choose_word(liste_sneakers, trois_mots_aleatoire)
        liste_test = melange(trois_mots_aleatoire, liste_melange)
        essai = 3 #nombre de tour à chaque manche 
        mot = True
        print("Votre liste de lettre est :", "-".join(liste_test))
        print("Vous êtes à la manche : ",a, ".", "Vous avez 3 tentatives au total") 
        
        for i in range(3):
            proposition = input("Rentrer une proposition d'un mot / Quit : ")
            proposition = proposition.lower() # Toute mot entrée par l'utilisateur est réduit en minuscule
            if proposition == "quit":
                break
            else:
               for i in range(3):
                   if proposition == trois_mots_aleatoire[i]:
                       trois_mots_aleatoire[i] = ""
                       print("Bravo tu as trouvé un mot.")
                       Score = Score + 1
                       mot = False
                       print("Ton score est de", Score, "points !")
                       essai = essai - 1
                       print("Vous avez gagné ce tour !", "Il vous reste", essai, "tentative(s)")
               if mot == True:
                   print("Mauvais mot ou vous avez deja rentré ce mot")
                   essai = essai - 1
                   print("Vous avez perdu ce tour !", "Il vous reste", essai, "tentative(s)")
        a = a + 1
        trois_mots_aleatoire = []
        return Scrabble(trois_mots_aleatoire, Score, a)
    if a == 4:
       print("Vous avez finis le jeu du mini Scrabble avec", Score, "points !")


Scrabble(trois_mots_aleatoire, Score, 1)
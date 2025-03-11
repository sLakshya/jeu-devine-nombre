import random

def jeu_devine_nombre():
    nombre_a_trouver = random.randint(1, 100)
    tentative = 0
    
    print("Bienvenue dans le jeu de devinette !")
    print("J'ai choisi un nombre entre 1 et 100. À toi de deviner !")
    
    while True:
        try:
            choix = int(input("Entrez votre nombre : "))
            tentative += 1
            
            if choix < nombre_a_trouver:
                print("Trop petit !")
            elif choix > nombre_a_trouver:
                print("Trop grand !")
            else:
                print(f"Bravo ! Tu as trouvé en {tentative} tentatives.")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    jeu_devine_nombre()

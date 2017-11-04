#!/usr/bin/python3.5
# La ligne ci-dessus n'est probablement pas nécessaire sous Windows, il faudra peut-être la supprimer.

# Une ligne qui commence par un dièze (on ne dit pas hashtag, hein, non mais!) indique un commentaire.
# Les commentaires servent aux humains qui lisent le code, mais sont ignorés par la machine.

# Ce programme affiche un menu, demande à l'utilisateur qu'elle action effectuer, puis réalise cette action avant d'afficher le menu à nouveau.
# Ce comportement tourne en boucle jusqu'à ce que l'utilisateur décide d'arrêter le programme.
# Certaines parties du programme sont à remplir, et vous êtes encouragés à modifier ce que vous voulez pour observer ce qui se passe.



# Ceci est une fonction, elle sera appellée par le programme principal.
# On utilise des fonctions pour rendre la lecture du programme plus claire (entre autres).
def menu():
    # Le code exécuté par la fonction est "indenté", c'est à dire qu'on rajoute une tabulation.
    # L'indentation est obligatoire, c'est elle qui indique où commence et où termine la fonction.
    # Ce n'est pas le cas pour la plupart des langages de programmation, mais c'est une bonne habitude à garder pour plus de lisibilité.

    # Cette fonction affiche un menu
    print ("Menu")
    print ("1) Conversion d'un nombre décimal")
    print ("2) Conversion d'un nombre binaire")
    print ("3) Conversion d'un nombre hexadécimal")
    print ("4) Conversion d'un caractère ASCII")
    print ("5) Quitter")

    # Puis demande à l'utilisateur de rentrer quelque chose au clavier, ce quelque chose sera stocké dans la variable "ret" (qui est automatiquement créée).
    ret = input("Quelle action effectuer? ")

    # La fonction "retourne" la valeur de la variable "ret". On verra plus loin comment s'en servir.
    return ret


# Une autre fonction, qui reçoit un paramètre nommé "nombre"
# À l'intérieur de la fonction, on peut utiliser le paramètre "nombre" comme une variable. Par contre, on ne peut pas le modifier.
def decimal (nombre):
    print ("Cette fonction est à compléter")
    # Le paramètre "nombre" est une chaîne de caractères, ici on le convertit en entier (integer en anglais, abrégé int)
    n = int(nombre)
    print ("Le nombre " + nombre + "(10) vaut:")
    #Affiche "nombre" en binaire et en hexadécimal


# 3 autres fonctions, à vous de jouer
def binaire (nombre):
    print ("Cette fonction est à compléter")
    #Affiche "nombre" en décimal et en héxadécimal

def hexadecimal (nombre):
    print ("Cette fonction est à compléter")
    #Affiche "nombre" en binaire et en décimal

def caractere (car):
    print ("Cette fonction est à compléter")
    #Affiche le code ASCII de "car" en décimal, binaire et hexadécimal



# Cette ligne est un peu cryptique, on l'expliquera un autre jour.
# En attendant, on va dire que ça indique le début du programme. Elle n'est pas nécessaire, mais c'est une bonne habitude à prendre.
# Quand je lance ce programme, la machine commence à exécuter les lignes ci-dessous.
if __name__ == '__main__':
    # On crée une variable booléenne (vrai ou faux, "True" ou "False"), initialisée à True.
    # On se servira de cette boucle pour savoir quand le programme doit s'arrêter
    continuer = True

    # Ceci est une boucle "while", ce qui se traduit par "tant que". Le programme boucle tant que la condition entre parenthèses est vraie (True)
    # Ici, tant que la variable "continuer" vaut True, le programme reboucle.
    while (continuer):
        # On appelle la fonction "menu" déclarée plus haut.
        # La valeur retournée (ret) est stoquée dans la variable "action".
        action=menu()

        # Ceci est une structure conditionnelle. Si la condition entre parenthèse est vraie (ici action vaut "1"), alors le code qui suit est exécuté.
        if (action == "1"):
            n = input("Entrez un nombre décimal : ")

            # On appelle la fonction "decimal" en lui passant pour paramètre "n".
            # Si je rentre "10", par exemple, le paramètre "nombre" de la fonction vaudra "10". 
            # Je peux rappeler plusieurs fois la même fonction avec un paramètre différent.
            decimal(n)

        # elif signifie "sinon si". Si action ne vaut pas "1" mais "2", alors:
        elif (action == "2"):
            n = input("Entrez un nombre binaire : ")
            binaire(n)

        # Si action ne vaut ni "1", ni "2", ni "3"...
        elif (action == "3"):
            n = input("Entrez un nombre hexadécimal : ")
            hexadecimal(n)

        # Vous avez compris le principe
        elif (action == "4"):
            c = input("Entrez un caractère : ")
            caractere(c)

        # else veut dire "sinon". C'est à dire dans tous les autres cas. Donc action ne vaut ni "1", ni "2", ni "3", ni "4". 
        # Il peut valoir "5", "0", mais aussi "420", "pouet" ou "Monsieur Fiack est trop fort".
        else:
            print ("À bientôt")
            # On modifie la variable continuer qui vaut maintenant False. 
            # La condition du while est maintenant fausse, on sort de la boucle.
            # Comme il n'y a plus rien après ça, le programme s'arrête.
            continuer = False

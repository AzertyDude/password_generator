#-*- coding: utf-8 -*-
import random
import os #importation du module random pour le hasard et os pour la manipulation de fichier
print("+---------------------------+")
print("|       password generator  |")
print("|           by              |")
print("|            Sphynx         |")
print("|                           |")
print("+---------------------------+")
char =["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n","A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N","?","&","é","(","-","è","_","ç","à",")","=","^","%","*","!","/" ] # liste des caractère utilisé pour générer le mot de passe
length = int(input("Entrez la taille désiré pour votre mot de passe : "))#entré de la taille du mot de passe désiré
password = random.choices(char, k=(length))#création d'une nouvelle liste avec 5 caractère au hasard
mdp = "".join(password)#conversion de la liste en caractère
chemin = " "#votre chemin à modifier
if os.path.isfile(chemin) :#vérifier si le fichier ou sera stocké le mdp existe et le supprimer pour éviter les doublon
		os.remove("password.txt")
file =open("password.txt", "w")
file.write(mdp)
file.close()
print("mot de passe = ", mdp)
print("Le mot de passe a été généré et stocké dans password.txt")
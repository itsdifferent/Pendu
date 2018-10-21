#!/usr/bin/python3.6
# -*-coding:utf-8 -*

from random import *
from fonctions import *

print("Bienvenue dans le jeu du pendu !\n".center(75))
name = input("Entre ton prénom/pseudo pour commencer : ")
score = 0
z = 1

while z == 1:

	print("\nBonjour",name,", ton score est de", score, "pour l'instant. Joue pour l'augmenter ! \n")
		
	nb_chance = 0
	star = "*"

	list_of_words = ["Fil", "Mur", "Haut", "Tapis", "Cadre", "Souris", "Portable", "Sublime", "Clavier", "Sac", "Gilet", "Email", "Sourcil", "Mais", "Tulipe", "Limer", "Sceau", "Lait", "Bad", "Copines", "Plot"]
	random_word = choice(list_of_words)
	random_word = random_word.lower()
	nb_caracteres = len(random_word)
	print("Le mot à deviner contient",nb_caracteres,"caratères.\n")
	hidden_word = nb_caracteres * star
	print(hidden_word,"\n")
		
	while nb_chance < 8:
		
		j = hidden_word.find(star)
			
		if j == -1:
			print("\nBravo, tu as trouvé le mot ! \n\nFin de la partie.\n")
			break

		letter = input("Entre une lettre de l'alphabet afin de deviner le mot : ")
		letter = letter.lower()
		print("\n")
			
		i = random_word.find(letter)

		if i == -1:
			print("La lettre entrée ne se trouve pas dans le mot.\n")
			print(hidden_word)
			nb_chance += 1
			print("\nIl te reste",8-nb_chance,"chances.\n")
			continue
		if i >= 0:
			list_hidden_word = list(hidden_word)
			list_hidden_word[i] = letter
			hidden_word1 = "".join(list_hidden_word)
			print("Tu as trouvé une lettre !\n")
			print(hidden_word1)
			hidden_word = hidden_word1
			continue

	score = score + (8 - nb_chance)

	other_player()

	options = input("""\nQue veux-tu faire maintenant ?
	1. rejouer
	2. quitter\n""")

	if options == "1":
		continue	
	if options == "2":
		player = {name : score}
		with open('scores.txt', 'a') as fichier:
			fichier.write(str(player))
		z = 0
	else:
		print("Caractère entré non reconnu.")
		z = 0
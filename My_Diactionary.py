import json 
from difflib import get_close_matches
import os,pyfiglet
from colorama import Fore,Style
import random


data = json.load(open("dictionary.json"))




all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)

def banner():
        os.system("clear")

        print(ran, pyfiglet.figlet_format("\tDictionary"))
        print(ran + "\n\t\tV_1.0\t\n\n")
        print("*" * 63)

        print(Style.BRIGHT+Fore.LIGHTCYAN_EX, "\n" ,"- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Style.BRIGHT+Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Style.BRIGHT+Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        print("\n" , "*" * 63)

banner()


def dictionary(word):

	if word in data:
		print(f'"\n" {data[word]}')

	elif word.title() in data:
		print(f'{data[word.title()]}')

	elif word.upper() in data:
		print("\n" + data[word.upper()])

	elif len(get_close_matches(word , data.keys())) > 0:
		print(f"\nDid you mean {get_close_matches(word , data.keys())[0]} instead of")
		dec = input(ran+("\nType below [y/n]\n~>")).lower()

		if dec == "y":
			print(f"{data[get_close_matches(word , data.keys())[0]]}")

		elif dec == "n":
			print("\nYou like rough play! ")

	else:
		print("\nNothing found! ")

cont = ""
no = ["n","no"]
while cont not in no:

	word = input(ran+"\nEnter word below to find\n~>").lower()

	meaning = dictionary(word)
	try:
		meaning = filter(None , meaning)
	except TypeError:
		pass
	if type(meaning) == list:
		for i in meaning:
			print(f"{i}")
	else:
		print(f"{meaning}")

	cont = input(ran+"\nDo you want to continue [y/n]\n~>").lower()
	if cont == "y":
		os.system("clear")
		banner()
		pass


			
		
		















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
		return f'"\n"{ran} {data[word]}'

	elif word.title() in data:
		return f'{ran}{data[word.title()]}'

	elif word.upper() in data:
		return "\n"+ran + data[word.upper()]

	elif len(get_close_matches(word , data.keys())) > 0:
		print(f"\n{ran}Did you mean {get_close_matches(word , data.keys())[0]} instead of")
	
		dec = input(ran+("\nType below [y/n]\n~>")).lower()

		if dec == "y":
			return f"{ran}{data[get_close_matches(word , data.keys())[0]]}"

		elif dec == "n":
			return "\n{ran}You like rough play! "

	else:
		return "\nNothing found! "

cont = ""
no = ["n","no"]
while cont not in no:

	word = input(ran+"\nEnter word below to find\n~>").lower()

	meaning = dictionary(word)
	if type(meaning) == list:
		for i in meaning:
			print(f"{ran}{i}")
	else:
		print(f"{ran}{meaning}")

	cont = input(ran+"\nDo you want to continue [y/n]\n~>").lower()
	if cont == "y":
		os.system("clear")
		banner()
		pass


			
		
		















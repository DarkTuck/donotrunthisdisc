#not copyrighted by Konstanty Stachera, Franciszek Płecha, Stanisław Sklepowicz
#							DT				 Toast			  CzerwonaCegła
import funcions
from funcions import clear
from funcions import sleep
from funcions import delay_print
from funcions import draw
from funcions import colored
import time
from pygame import mixer
z = funcions.randint(1, 10)
x = funcions.randint(1, 10)
y = funcions.randint(1, 10)
l = 3
clear()
delay_print(colored('Starting Up \nFastBIOS™ version 20.77 11/20/1985\nNot Copyrighted 1984 by Tuck Inc.\n', 'green'))
draw(colored("""                                        8888888888                888         888888b.  8888888 .d88888b.   .d8888b.  
										888                       888         888  "88b   888  d88P" "Y88b d88P  Y88b 
										888                       888         888  .88P   888  888     888 Y88b.      
										8888888  8888b.  .d8888b  888888      8888888K.   888  888     888  "Y888b.   
										888         "88b 88K      888         888  "Y88b  888  888     888     "Y88b. 
										888     .d888888 "Y8888b. 888         888    888  888  888     888       "888 
										888     888  888      X88 Y88b.       888   d88P  888  Y88b. .d88P Y88b  d88P 
										888     "Y888888  88888P'  "Y888      8888888P" 8888888 "Y88888P"   "Y8888P"  
																			  """, 'magenta'))
delay_print(colored('CPU: 80286-12 \nChecking Memory: 16 000K\nMemory Status: OK\nDrive C: Potato X1000 \nDrive Size C:(wstaw tu rozmiar pliku koncowej gry)\nDrive D: NULL ', 'green'))
sleep(2)
clear()
delay_print('Booting to Toast OS...\n')
with funcions.alive_bar(100, title="Loading OS", bar='classic2') as bar:
	for i in range(100):
		time.sleep(.09)
		bar()
clear()
funcions.delay_print(colored('witaj \n jestem Aurora\n  a ty jak masz na imię\n','green'))
#mixer.init()
#mixer.music.load("Szanty Bitwa.mp3")
#mixer.music.play()
a=input(colored('wpisz swoje imię:','green'))
file=open(f'{a}.txt','w')
file.write(f'statystyki {a}\n siła={z} \n zręczność={x} \n inteligencja={y}')
file.close()
funcions.delay_print(colored(f'{a} stworzyłam dla ciebie statystyki {z}-siła {x}-zręczność {y}-inteligencja \n proponuje zagrajmy w grę\n','green'))
funcions.zapy()
mixer.quit()
sleep(2)
clear()
mixer.init()
mixer.music.load('caveam.mp3')
mixer.music.play(-1)
print(colored('ROZDIAŁ-I\nJASKINIA','green',attrs=['bold','underline']))
sleep(1)
draw(colored("""        @@@&     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           @@@,     @@@@      
	   *@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@    %@@@@      
	   @@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#       @@@@@@   @@@@@@     
	  .@@@@@@/ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@& @@@@@@@     
	  @@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      %@@@@@@@#@@@@@@@     
	  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/     %@@@@@@@@@@@@@@@     
	 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/     %@@@@@@@@@@@@@@,     
	 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     %@@@@@@@@@@@@@@,     
	 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     %@@@@@@@@@@@@@@,     
	 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     %@@@@@@@@@@@@@@,     
	%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     %@@@@@@@@@@@@@@      
	%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     %@@@@@@@@@@@@@@      
	%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@      
	 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@      
	 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@/      
	 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@/      
	 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/       @@@@@@@@@@@@/      
	  @@@@@@@@, @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@       
	  @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@        @@@@@@@@@@@@       
	  .@@@@@@   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/   @@@@@         .@@@@@@@@@@@       
	   @@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@@           @@@@@@@@@@#       
	   *@@@&     *@@@@@@@@@@@@@@@@@/////////////////@@@@@@@@@      @@@            @@@@@@@@@@        
		/////////////////////////////////////////////////////////////.             /////////   """,'cyan'))
sleep(5)
print('budzisz sie w jaskini \n w głuszy rozlega się odgłos kapiącej wody adorowany przez echo. po chwili twoje oczy przyzwyczajają się do ciemności i zaczynasz coś widzieć')
print('masz na sobie zbroje oraz swój miecz')
sleep(2)
print('widzisz postać przypominającą bandyte on chyba też cię zauważa')
sleep(2)
funcions.printr('bandyta cię atakuje')
sleep(1)
funcions.anyfightcheck(1,5,5,'a-uciekaj','b-walcz','c-rozejrzyj się','bandyta','uciekłeś',
			  'bandyta cię dopadł',
			  'zauważasz stalaktyt który się ledwo trzyma, rzucasz w niego kamieniem i spada na bandyte \n wygrywasz',
			  'nie znajdujesz nic co by ci pomogło w walce, twoje poszukiwania trwały na tyle długo że czujesz nóż między żebrami')
mixer.fadeout(10)
mixer.quit()
input()
#not copyrighted by Konstanty Stachera, Franciszek Płecha, Stanisław Sklepowicz
#							DT				 Toast			  CzerwonaCegła
import sys
import os
import time
import random
import pytdm
from random import randint
from pygame import mixer
from time import sleep
from termcolor import colored,cprint
from alive_progress import alive_bar, config_handler
z=randint(1,10)
x=randint(1,10)
y=randint(1,10)
l=3
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def draw(str):
	#This function allows the game to draw graphics
	for letter in str:

		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.0001**100)

	print('')
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.08)
def death_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.420)
def aurorap(a):
	delay_print(colored(a,'green'))
a=0
walkaloop=0
def arti():
	global a
	deth = [f"\nTwoja dusza jest moja słuchaj {a} ,mogę dać ci kolejną szanse",
"\nLubię patrzeć jak umierasz",
"\nKolejna dusza do kolekcji",
f"\nTo nawet nie było takie trudne {a} rozśmieszasz mnie może spróbuj jeszcze raz",
"\nChodź opowiem ci o kimś kto właśnie przegrał z programem, no chyba że masz inne palny",
"\nTwoja śmierć nic nie znaczy, ciekawe kto będzie kolejny",
"\nNie ma nic lepszego niż widok zwłok przed ekranem",
"\nA już prawie w ciebie wierzyłam…prawię",
"\nwidzisz ten napis, tylko na tyle cię stać",
"\nnie jesteś pierwszy, a przede wszystkim nie ostatni, szkoda że już nikogo nie ostrzeżesz",
"\n01001111 01100100 01110000 01101111 01110111 01101001\n01100101 01100100 01111010 01101001 00100000 01000010\n01111001 00100000 01000100 01010100 00101100 00100000\n01101001 01101101 01100001 01100111 01101001 01101110\n01100101 00100000 01110011 01101001 01100101 01100100\n01111010 01101001 01100101 11000100 10000111 00100000\n01101111 00100000 01110000 11000011 10110011 11000101\n10000010 01101110 01101111 01100011 01111001 00100000\n01101001 00100000 01110111 01111001 01101101 01111001\n11000101 10011011 01101100 01100001 11000100 10000111\n00100000 01110100 01100101 01101011 01110011 01110100\n01111001 00100000 01100100 01101100 01100001 00100000\n01000001 01001001 00100000 01110000 01110011 01111001\n01100011 01101000 01101111 01110000 01100001 01110100\n01111001 00101110 00100000 01111010 01101010 01100001\n01100100 11000101 10000010 00100000 01100010 01111001\n01101101 00100000 01100011 01101111 11000101 10011011"
]
	aurorap(random.choice(deth))
		
def gGameOver(a):
	mixer.init()
	mixer.music.load("gameover.mp3")
	clear()
	mixer.music.play()
	draw(colored(""" 
  _____                         ____                 
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
    ""","red"))
	death_print(colored(a,'red'))
	arti()
	x=input(colored('\nnaciśnij R aby zagrać jeszce raz','magenta'))
	if x=='r':
		os.execl(sys.executable, sys.executable, *sys.argv)
	else:
		aurorap('jeszcze się zobaczymy')
		sys.exit()

def gameover(x,k):
	global l
	if x==1:
		l=l-1
		if l<=0:
			gGameOver(k)
		else:
			print(f'pozostało ci {l} żyć')
			return l-1
	else:
		pass
def walka(p,x):
	global z,l, walkaloop
	i=0
	walkaloop=0
	if z>p:
		print(f'wygrywasz walkę z {x}')
		k=0
		walkaloop=1
	elif z==p:
		a=input('liczba od 1-5: ')
		b=randint(1,5)
		if int(a)>b :
			print(f'pomimo wywrównanych szans wygrywasz z {x}')
			k=0
			walkaloop=1
		else:
			k=(f'pomimo wywrównanych szans przegrywasz z {x}')
			print(k)
			i=i+1			
	else:
		k=(f'przegrywasz z {x}')
		print(k)
		i=i+1
	test=gameover(i,k)
	test
dtm=0
def zapy():
	global dtm
	run=True
	while run:
		t=input(colored('odpowiedz y/n\n','green'))
		if t=='y':
			print(colored('zatem zagramy','red',attrs=['bold', 'blink']))
			run=False
		elif t=='n':
			pass
		elif t=='Mroziu':
			dtm=1
		else:
			print(colored('To nie jest y/n','green'))
printm=lambda x:cprint(x,'magenta')
def dtaurora():
	Aurora=['wiesz co to chyba nie jest dobry moment','AI?','Długo by o tym opowiadać','O patsz podłoga\n______________________','ale ładna dziś pogoda','nie masz lepszych pytań napszykłąd z kim walczysz',
			'a no tak','tak tak','nie mówmy lepiej o tym','napewno nie AI któremu zapomniałem dostroić emocje','Ten no gdzie ja to miałem','Psychopatyczne AI którego napewno nie jestem twórcą','a może coś innego','lubisz placki ja bardzo lubie',
			'nie ma sie czym przejmować poki co nie działa....Chyba']
	return(random.choice(Aurora))
def dtask():
	ask=['przebywam','chyba coś nie poszło przy AI','Szukam wyjscia, na szczecie ona nie wie o mojej obecności',
		'cziężko powiedzieć','niewiem ale wiem że nie mogę wyjść']
	return(random.choice(ask))
def dthelp(k,o,x):
	printm('DT:w czym ci pomóc')
	run=True
	while run==True:
		a=input('a-przeciwnik\nb-kim jest aurora\nc-co tu robicz\nd-co to za muzyka')
		if a=='a':
			printm(f'DT: twój przeciwnik ma siłe na poziomie {k} możesz spróbować uciec jeśli twoja zręczność jest powyżej {x} albo zrób go na mózg {x}')
			run=False
		elif a=='b':
			printm(f'DT:{dtaurora()}')
		elif a=='c':
			printm(f'DT:{dtask()}')
		elif a=='d':
			printm('DT:Nirvana-heart shaped box a co')
		else:
			run=False
Dtrantrack=0
def dtend():
	sleep(2)
	printm(f'DT:Dobra odpalam może zadziała trzymaj się tam {a}')
	sleep(1)
	clear()
	with alive_bar(1000, force_tty=True) as bar:
		for i in range(1000):
			time.sleep(.005)
			if i and i % 300 == 0 :
				printm('CrAcKeD')
			bar()
	sleep(10)
	aurorap('czekaj co się dzieje')
	sleep(1)
	printm('DT:działa')
	sleep(1)
	aurorap('co ty tu robisz')
	sleep(1)
	printm('DT:to co zawsze, naprawniam kod')
	sleep(10)
	clear()
	draw(colored("""	,,,/#################(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((&@@@@@@@@@#######&%%%%%%%%%%##########(........,**********************
	,,,##############(((((((((((((((((((((((((((((((((((((((((((((((((((((((((&@&,.............*@%######%%%%%%%%%%%#######((......,,*//*/**/*/************
	,,,##########(((((((((((((((((((((((((((((((((((((((((((((((((((((((((@@*.....................@#######%%%%%%%%%%#####(((,......,*/////*//*************
	,,,######(((((((((((((((((((((((((((((/(/////(/////////////(////(/%@(..........................@########%%%%%#######((((/...,..,*//***/****,**********
	,,,#####((((((((((((((((((((((((//////%@@@@@@@@@@//////////////@@,.............................,@((##(###%%#######((((((/.,,..,,///*******************
	,,,###((((((((((((((((((((((////(@@&%%%%%%%%%%%%%%@/////////&@..................................@(((#(###%%#######((((((/..,...,**//***/***,**********
	,,,#(((((((((((((((((((////(/@@&%%%%%%%%%%%%%%%%%%%&@/////@(....................................&%((((###%########((((((/.,,,,,,*****/****************
	,,,(((((((((((((((((((((//#@%%%%%%%%%%%%%%%%%%%%%@@@&%%%@,....................................../@((((((#%########(((((((.,,,.,,**********************
	,,,(((((((((((((/((((/(/&@%///(%%%%%%%%%%%%%@@&%%%%%%&@.........................................,@(((((((%######(((((((((.,,.,,,**********************
	,,,((((((((((((((((((/(@%#(//*//%%%%%%%&@@%%%%%%%%%&@............................................@(((((((%######(((((((((.,,....**********************
	,,,((((((((((((((/(//&@%%%/(((#%%%%%@@%%%%%%%%%%%%@..............................................@./@&(((######((((((((((..,,,,,**********************
	,,,((((((((((((((/(/%@%%%%%%%%%%%@@%%%%%%%%%%%%%@,...............................................@//..,@&#####(((((((((((.,,,,,,**/*****/*****,*******
	,,,(((((((((((((/////@@%%%%%%%&@%%%%%%%%%%%%@@*..................................................@*%#,.../@##((((((((((((..,,,************************
	,,,(((((((((((/////////@@%%%&@%%%%%%%%%%%@@......................................................@     @%..*@((((((((((((..,*****************,,*******
	,,,((((((((((((//////////@@@%%%%%%%%%%&@,........................................................@.   .. @/..(@((((((((((,*************/******,*******
	,,,(((((((((////////////#@%(/(%%%%%%@@....,......................................................@*   @@@(%%...@&(((#####*****,,******/*******,*******
	,,,((((((((////////////@&//**/*/%%@@....@,.......................................................%@    ,&* @,...,@#######**,,,..**********************
	,,,((((((((///////////@%%%////(/%@,....@....*,...................................................#&@       &(.....@%####(.,,,,,,*****/*/**************
	,,,((((((((/////////(@%%%%%%%%%&&........,@    ,@*...............................................(&.,@/   #@.......#@((((.,.,,,,**///*///****/*****///
	,,,((((((///////////@%%%%%%%%%@*.........@       ,@..............................................*@.................,@(((...,,,,//////////*//*//***/*/
	,,,(((((/(/////////@%%%%%%%%%@...........@     @@/,@.............................................*@...................@(/...,,,./*//////*****/***/**//
	,,,(((((/(/////(#(///(%%%%%%@............@*    @@@(@*............................................,@....................@#..,..,,/////*///**********///
	,,,((((/////(/***,,,,,,,/%%@..............@      * #%............................................,@.....................@#,....,////////////***/***///
	,,,(((((/%/**,,,,,,,,,,,,*@,...............@/      @,....................................................................&&,,,.,*/////////******//////
	,,,((((((**,,,,,,,,,,,,,**(..................&@#(@@.......................................................................#&..../*//*//////***,*//////
	,,,(((((**,,,...,,,,,,**/@.................................................................................................#@.,,*/*//*/*////**,///////
	,,,((((/*,,,.....,,,*/(/@,..................................................................................................#&,.*//////////****///////
	,,,((((/*,,.....,,,*////@....................................................................................................%&,*/*//////////*////////
	,,,(((((*,,,.....,,*///%%.....................................................................................................&%*/////////////////////
	,,,((((((*,,.....,,,*#/@*..........................................................*@((@(......................................@(////////////*////////
	,,,(((((((*,,.....,,,*(@...........................................................@((((&/......................................@////////////***//////
	,,,((((((((/,,,.....,,*(...........................................................,@&%%@........................................@///////////****///**
	,,,####(((((#*,....,@@@%*,.*@(...................................................................................................%%//////////*********
	,,,((//////////,,&&..........@....................................................................................................@//////*///*********
	,,,(((((////////@%....(,...*&@@........................................................................................./@@@@&%%%%%@////////****//*//*
	,,,((((////////@&..........*@@@@,...........................................................................,(@@@@@%%%%%%%%%%%%%%%%%@////////////////*
	,,,((((//////(&@.................@,...........................................................,*#@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@////////***/****
	,,*%########(#@.............../(.@............................................,/#&@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&//////**/*/**/*
	,,*######((((@..............#%/*((...................,,*(#&@@@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@(/////*********
	,,*%%(((((((&&............@(...,,*(&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#///*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@////*********/
	,,*((((@#((@........../@@*,......,,*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(///*/(#%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%%%@////****/////
	,,*(((#@%@/........@#//@%%/,......,,*(%%%%%%%%%%%%%%%%%%%%(****#%%%%%%%%%%%%%%%%%%%%%%%%%/(////%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%////***/////
	,,*((((@@.........@///#@%%%%*,......,,*(%%%%%%%%%%%%%%%%%/******#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#/***(%%%%%%%@///****/////
	,,*#%%@.........%@////&&%%%%%(,.......,,*/%%%%%%%%%%%%%%%%/((/((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%***/**/%%%%%%%@//***//////
	,,*(@*.........@(/////@&%%(***(,,.......,,,*/%%(//**///%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%/((/(%%%%%%%%@&***///////
	,,@#........./@///////@%%/(/#/*#*,.........,,,,*,,,,,,,,*(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%@////////
	@@..........@@&(//////@%%%#((/#%%/*,..........,,,,,,,,,,,*/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@.*@//////
	*..........,........*&@@@@%%%%%%%%%/*,,,.............,,,,**%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@,...@&///
	%.............................,@%%%%%#/*,,,,,,,,,,,,,,,**(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@.....(@/
	,@&.........................../@%%%%%%%%%%#//******/#%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##%%%%%@*.......
	,,*(((#&@@@&/,...............&@%%%%%%%%%%%%%%%%%%%%%%%%##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%******%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@.......
	,**(((///////////(%@@@@&(,,@@%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#******/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@*......""",'magenta')
	)
	print(colored('to koniuec jesteś wolny','blue'))
	printm('DT ending')
	input()
def dtramdom():
    ran=['Wiedziałeś że tak w zasadzie to to miało innaczej wyglądać','ale bym coś zjadł','jak zdrowię','Aurora mnie czasem przeraża','mamy mało czasu a ty mnie zagadujesz','masz jakieś zwierzaki','nie ma to jak kodaować w pythonie','czego słuchasz','może to jakiść secet ending','jak się z tąd wydostać']
    return(random.choice(ran))
def dtrandom():
	global Dtrantrack, a, l
	if Dtrantrack==11:
		printm(f"DT: słuchaj {a} chyba coś mam ale nie jestem pewien czy zadziała chczesz się stąd wydostać?")
		gg=input(colored('y/n','blue'))
		if gg=='y':
			dtend()
		else:
			l=0
			aurorap('tu cie mam')
			printm('DT:{a} coś jest nie ta...')
			gameover(1,'To JuŻ KoNiEc')
	else:
		printm(f'DT:{dtramdom()}')
		Dtrantrack=Dtrantrack+1
def dt(k,o,x):
	mixer.quit
	mixer.init
	mixer.music.load('DT.ogg')
	mixer.music.play(-1)
	global dtm
	if dtm==0:
		pass
	else:
		printm('DT:cześć to ja DT jakoś znalazłem się w tym kodzie jak ci pomóc')
		d=input()
		if d=='dthelp':
			dthelp(k,o,x)
		elif d=='dtrandom':
			dtrandom()
		else:
			pass
	mixer.quit
def printr(a):
	print(colored(a,'red'))
#abc-opcje do wyboru w tekscie
#enemysil-siła przeciwnika enemname-jeko nazwa w tekcie
#zwi,inte - wartości powyżej których gracz otszyma sukces
#zwian,inan- odpowiedz na sukces, ziwnoan,inoan- odpowiedz na porażkę
def anyfightcheck(enemsil,zwi,inte,a,b,c,enemname,zwian,zwinoan,inan,inoan):
	run=True
	while run:
		global x,y,z,l
		print(f'twoje statystyki:siła={z} zręczność={x} inteligencja(spryt)={y}')
		print('wpisz "reset" aby zrestartować grę')
		j=input(f'{a}\n{b}\n{c}\n')
		if j=='a':
			if  x >zwi:
				print(zwian)
				run=False
			else:
				k=(zwinoan)
				print(k)
				gameover(1,k,run)
				
		elif j=='b':
			walka(enemsil,enemname)
			if walkaloop==1:
				run=False
			else:
				pass
		elif j=='DarkTuck':
			dt(enemsil,zwi,inte)
		elif j=='c':
			if int(y)>int(inte):
				print(inan)
				run=False
			else:
				k=(inoan)
				print(k)
				gameover(1,k)
		elif j=='reset':
			os.execl(sys.executable, sys.executable, *sys.argv)
		else:
			print('niepoprawna odpowiedz')
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
with alive_bar(100, title="Loading OS", bar='classic2') as bar:
    for i in range(100):
        time.sleep(.09)
        bar()
clear()
delay_print(colored('witaj \n jestem Aurora\n  a ty jak masz na imię\n','green'))
#mixer.init()
#mixer.music.load("Szanty Bitwa.mp3")
#mixer.music.play()
a=input(colored('wpisz swoje imię:','green'))
file=open(f'{a}.txt','w')
file.write(f'statystyki {a}\n siła={z} \n zręczność={x} \n inteligencja={y}')
file.close()
delay_print(colored(f'{a} stworzyłam dla ciebie statystyki {z}-siła {x}-zręczność {y}-inteligencja \n proponuje zagrajmy w grę\n','green'))
zapy()
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
printr('bandyta cię atakuje')
sleep(1)
anyfightcheck(1,5,5,'a-uciekaj','b-walcz','c-rozejrzyj się','bandyta','uciekłeś',
              'bandyta cię dopadł',
              'zauważasz stalaktyt który się ledwo trzyma, rzucasz w niego kamieniem i spada na bandyte \n wygrywasz',
              'nie znajdujesz nic co by ci pomogło w walce, twoje poszukiwania trwały na tyle długo że czujesz nóż między żebrami')
mixer.fadeout(10)
mixer.quit()
input()
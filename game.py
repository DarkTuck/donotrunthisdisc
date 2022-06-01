#not copyrighted by Konstanty Stachera, Franciszek Płecha, Stanisław Sklepowicz
#							DT				 Toast			  CzerwonaCegła
import funcions
import stats
from funcions import clear
from funcions import sleep
from funcions import draw
from termcolor import colored
from pygame import mixer
z, x, y, l=stats.stats_list


clear()
#funcions.boot()
#funcions.delay_print(colored('witaj \n jestem Aurora\n  a ty jak masz na imię\n','green'))
#mixer.init()
#mixer.music.load("Szanty Bitwa.mp3")
#mixer.music.play()
a=input(colored('wpisz swoje imię:','green'))
#file=open(f'{a}.txt','w')
#file.write(f'statystyki {a}\n siła={z} \n zręczność={x} \n inteligencja={y}')
# file.close()
funcions.delay_print(colored(f'{a} stworzyłam dla ciebie statystyki {z}-siła {x}-zręczność {y}-inteligencja \n proponuje zagrajmy w grę\n','green'))
funcions.zapy()
#mixer.quit()
#sleep(2)
#clear()
#mixer.init()
#mixer.music.load('caveam.mp3')
#mixer.music.play(-1)
print(colored('ROZDIAŁ-I\nJASKINIA','green',attrs=['bold','underline']))
#sleep(1)
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
sleep(2)
print('świat ci znika przed oczami i po chwili znadujesz się w nowej lokacji')
funcions.aurorap('całkiem nieźle ale to dopiero początek')
sleep(5)
print(colored('ROZDIAŁ-II\nGÓRY','white',attrs=['bold','underline']))
sleep(1)
draw(colored("""          /\
         /**\
        /****\   /\
       /      \ /**\
      /  /\    /    \        /\    /\  /\      /\            /\/\/\  /\
     /  /  \  /      \      /  \/\/  \/  \  /\/  \/\  /\  /\/ / /  \/  \
    /  /    \/ /\     \    /    \ \  /    \/ /   /  \/  \/  \  /    \   \
   /  /      \/  \/\   \  /      \    /   /    \
__/__/_______/___/__\___\__________________________________________________   """,'grey'))
print('po wyjściu z jaskini znajdujesz się w górach, zauważasz wioskę do której się udajesz')
sleep(1)
draw(colored("""                       X_x
                      / \\\
                      |n| |
                    )(|_|-'X
                   /  \\Y// \
                   |A | | |A|
                   |  | | |_|
            )(__X,,|__|MEB;;;-,)(,
           /  \\\;;;;;;;;;;;;/    \
           |A | |            | U  |
         )_|  | |____)-----( |    |
        ///|__|-'////       \|___)=(__X
       /////////////         \///   \/ \
       |           |  U    U |//     \u|
       |   )_,-,___|_)=(     | |  U  |_|_X
       |  ///   \\|//   \    | |  __ |/// \
     )_')(//     \Y/     >---)=( /  \|  | |-----------------..,
    //// ,\ u   u |   u /////   \|  ||__|A|----------------.., \,
   |  | .. |      |    ///// ,-, \__||--------------------.., \, \,
---'--'_::_|______'----| u | | | |-----------------------.., \, \, \,
                       |___|_|_|_|----------------------.., \, \, \, \,
                            `--------------------------.., \, \, \, \, \
                                                       \, \, \, \, \, \ \
                                                         \, \, \, \, \ \
                                                           \, \, \, \ \
                                                             \, \, \ \
                                                               \, \ \
                                                                 \ \
                                                                  """,'brown'))
print('w wiosce witają cie ciepło dają ci jadło, napajają i zapewniają schronienie.\n oferują ci żebyś się tu osiedlił co zdecydujesz')
funcions.QA(input('a-zostaje\nb-nie zostaje'),funcions.wioska_ending(),print("wyruszasz dalej"))
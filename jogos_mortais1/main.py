# Jogos Mortais
# fase 0:
import os
import time 
import random 
import pyttsx3
engine = pyttsx3.init()
os.system("cls")
os.system("color 2")

print('''                                             
\  ( OO ) _(  OO)( '.( OO )_            _(OO  )_             ( OO ) )( (  OO) )              
 ;-----.\(,------.,--.   ,--.)      ,--(_/   ,. \ ,-.-') ,--./ ,--,'  \     .'_  .-'),-----. 
 | .-.  | |  .---'|   `.'   |   .-')\   \   /(__/ |  |OO)|   \ |  |\  ,`'--..._)( OO'  .-.  '
 | '-' /_)|  |    |         | _(  OO)\   \ /   /  |  |  \|    \|  | ) |  |  \  '/   |  | |  |
 | .-. `.(|  '--. |  |'.'|  |(,------.\   '   /,  |  |(_/|  .     |/  |  |   ' |\_) |  |\|  |
 | |  \  ||  .--' |  |   |  | '------' \     /__),|  |_.'|  |\    |   |  |   / :  \ |  | |  |
 | '--'  /|  `---.|  |   |  |           \   /   (_|  |   |  | \   |   |  '--'  /   `'  '-'  '
 `------' `------'`--'   `--'            `-'      `--'   `--'  `--'   `-------'      `-----' ''')
print("Vamos jogar um jogo? Se prepare para enfrentar o desafio mais mortal da sua vida.")

time.sleep(3)
os.system("cls")
os.system("color 4")

print('''
__   __                    ___                           _ _ _ 
\ \ / /_ _ _ __  ___ ___  / __|___ _ __  ___ __ __ _ _ _| | | |
 \ V / _` | '  \/ _ (_-< | (__/ _ \ '  \/ -_) _/ _` | '_|_|_|_|
  \_/\__,_|_|_|_\___/__/  \___\___/_|_|_\___\__\__,_|_| (_|_|_)
                                             )_)               ''')
print ('''
         @@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@/      \@@@/   @
@@@@@@@@@@@@@@@@\      @@  @___@
@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@
@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@
 @@@@@@@@@@@@@@@/,/,/./'/_|.\'\,\
   @@@@@@@@@@@@@|  | | | | | | | |
                 \_|_|_|_|_|_|_|_| ''')
engine.say ("hahahahahahaha")
engine.runAndWait ()
os.system("cls")

# fase 1:
print("ACERTE OU MORRA!!!")
numeroSorteado =  random.randint (1,3)
#print (numeroSorteado)
numeroAposta = int(input ("numero sorteado (ENTRE 1 e 3): "))
respostaFase1 = numeroAposta

if numeroSorteado == numeroAposta:
    print("Fez o mínimo de um ser humano...você passou dessa vez...")
else:
    print("Nem pra isso presta, VOCÊ MORREU HAHAHAHA!!!")
    quit ()

# fase 2:
os.system("cls")
print("Prontos para A POTÊNCIA MORTAL???")
numero1 = random.randint(1,9)
print(numero1)
numero2 = random.randint(1,3)
print(numero2)
resultado1 = numero1 ** numero2 
print("E aí, qual é a resposta dessa potência meu mero mortal??")
print("Dica porque estou de bom humor: primeiro número elevado ao segundo....")
resultado2 = int( input("O resultado da potência é...: "))
respostaFase2 = resultado1

if resultado1 == resultado2 :
    print("Hm... até que você sabe matemática básica, agora vai piorar...")
else:
    print("Você já era.")
    engine.say ("Você já era.")
    engine.runAndWait ()
    print('''
               ___-----------___
           __--~~                 ~~--__
       _-~~                             ~~-_
    _-~                                     ~-_
   /                                           \
  |                                             |
 |                                               |
 |                                               |
|                                                 |
|                                                 |
|                                                 |
 |                                               |
 |  |    _-------_               _-------_    |  |
 |  |  /~         ~\           /~         ~\  |  |
  ||  |             |         |             |  ||
  || |               |       |               | ||
  || |              |         |              | ||
  |   \_           /           \           _/   |
 |      ~~--_____-~    /~V~\    ~-_____--~~      |
 |                    |     |                    |
|                    |       |                    |
|                    |  /^\  |                    |
 |                    ~~   ~~                    |
  \_         _                       _         _/
    ~--____-~ ~\                   /~ ~-____--~
         \     /\                 /\     /
          \    | ( ,           , ) |    /
           |   | (~(__(  |  )__)~) |   |
            |   \/ (  (~~|~~)  ) \/   |
             |   |  [ [  |  ] ]  /   |
              |                     |
               \                   /
                ~-_             _-~
                   ~--___-___--~ ''')
    quit()

# fase 3:
os.system("cls")
print('''
                                 _            
  __ _  __ _ _   _  __ _ _ __ __| | ___       
 / _` |/ _` | | | |/ _` | '__/ _` |/ _ \      
| (_| | (_| | |_| | (_| | | | (_| |  __/_ _ _ 
 \__,_|\__, |\__,_|\__,_|_|  \__,_|\___(_|_|_)
       |___/                                  ''')
engine.say ("Aguarde criaturinha")
engine.runAndWait ()
time.sleep(5)

print("Vamos ver se você tem boa memória! Resolva a seguinte fórmula:")
print("(respostaFase1 + respostaFase2) ** respostaFase1 - respostaFase2")
resultado = (respostaFase1 + respostaFase2) ** respostaFase1 - respostaFase2
print("Coloque o número inteiro, sem pontos.")
resultadoFinal = int(input("A resposta é: "))

if resultado == resultadoFinal :
    print ("Muito beemmm, parabéns por fazer o mínimo...passou por pouco")
    engine.say ("Vamos continuar")
    engine.runAndWait ()
else:
    print ("Preste mais atenção, você está prestes a morrer por ser BURRO! HAHAHA")
    print('''
                       ______
                    .-"      "-..
                   /             |
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)''')
    engine.say ("Hahahahahaha")
    engine.runAndWait ()
    quit ()

# fase 4
os.system("cls") 
print("Vamos ver se você é bomzão meeesmo.")
numeros = random.sample(range(0,15),5)                  
print(numeros)
time.sleep(2)
os.system("cls")

print("Quais foram os cinco números que você viu???")
engine.say ("Quais foram os cinco números que você viu?")
engine.runAndWait ()
primeiroNumero = int(input ("primeiro número: "))
segundoNumero = int(input ("segundo número: "))
terceiroNumero = int(input ("terceiro número: "))
quartoNumero = int(input ("quarto número: "))
quintoNumero =int(input ("quinto número: "))

tentativa = [primeiroNumero, segundoNumero, terceiroNumero, quartoNumero, quintoNumero]

if sorted(numeros) == sorted(tentativa):                  
    print ("Até que na memória você é bom...vamos para o DESAFIO FINAL!!!")
    engine.say ("Boa sorte na última fase, você vai precisar.")
    engine.runAndWait ()
else: 
    print("Sua memória é pior que a de um peixinho dourado, ENFRENTE AS CONSEQUÊNCIASS")
    print('''
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"''')
    quit ()

# fase 5
os.system("cls")
print("Não sei como conseguiu chegar até aqui... mas já que esta aqui, vamos ver se você é tão inteligente assim...")
print('''
   __  _  _____ ___ __  __  ___    ___ _  _ ___ ___ __  __   _   
 _/_/_| ||_   _|_ _|  \/  |/ _ \  | __| \| |_ _/ __|  \/  | /_\  
| |_| | |__| |  | || |\/| | (_) | | _|| .` || | (_ | |\/| |/ _ \ 
 \___/|____|_| |___|_|  |_|\___/  |___|_|\_|___\___|_|  |_/_/ \_\ ''')
print("Um programador encontra um nano computador que trabalha apenas com bits. O computador tem exatamente 41.943.040 bits de memória. Quantos Megabytes isso representa?")
print("Dica porque eu sei que você NÃO VAI conseguir: 1 byte = 8 bits, 1024 bytes = 1 KB, 1024 KB = 1 MB. HAHAHAHA")
engine.say("hahahahaha")
engine.runAndWait ()

respostFinal = 5
tentativaFinal = int( input("A resposta final é: "))

if respostFinal == tentativaFinal:
    print("PARABÉNS! VOCÊ VIVEU...dessa vez....")
    print('''
__     _____   ____ _____  __     _______     _______ _   _ _ _ _ 
\ \   / / _ \ / ___| ____| \ \   / /_ _\ \   / / ____| | | | | | |
 \ \ / / | | | |   |  _|    \ \ / / | | \ \ / /|  _| | | | | | | |
  \ V /| |_| | |___| |___    \ V /  | |  \ V / | |___| |_| |_|_|_|
   \_/  \___/ \____|_____|    \_/  |___|  \_/  |_____|\___/(_|_|_)''')
    time.sleep(3)
    print('''       
        ##########################          
   #####################################    
 #########################################  
####      ######################       #### 
###       ######################        ### 
##        ######################        ### 
###     ##########################      ### 
###    ############################    #### 
 ###   ### #################### ###    ###  
 ####   ### ################## ####  ####   
   ####  ######################### #####    
    ######## ################ #########     
      ######  ##############   ######       
               ############                 
                 ########                   
                   ####                     
                   ####                     
                   ####                     
                   ####                     
               ############                 
            ##################              
            ##################              
            ###            ###              
            ###            ###              
            ###            ###              
            ##################              
            ##################              
          ######################            
         ########################           ''')
    
else: 
    print("Você é um burro mesmo. É obvio que é 5.")
    print("ESTÁ NA CARA que 1 byte = 8 bits, logo, 41.943.040 bits/8= 5.242.880 bytes, 5.242.880/1024= 5.120KB e 5.120/1024 é...")
    time.sleep(2)
    print("5... VOCÊ VAI PAGAR POR TER ERRADO O DESAFIO MAIS FÁCIL HAHAHAHAHA")
    time.sleep(3)
    os.system("cls")
    print("Seu computador vai ser formatado em...")
    print('''
 _____ 
|___ / 
  |_ \ 
 ___) |
|____/ ''')
    time.sleep(2)
    print('''
 ____  
|___ \ 
  __) |
 / __/ 
|_____|''')
    time.sleep(2)
    print('''
 _ 
/ |
| |
| |
|_|''')
    os.system("cls")
    print('''
           _..--""---.                                
          /           ".                              
          `            l                              
          |'._   ,._ l/"\                              
          |_J&lt;__/.v._/                              
           \( ,~._,,,,-)                              
            `-\' \`,,j|                               
               \_,____J                               
          .--.__)--(__.--.                            
         /  `-----..--'. j                            
         '.- '`--` `--' \\                            
        //  '`---'`  `-' \\                           
       //   '`----'`.-.-' \\                          
     _//     `--- -'   \' | \________                 
    |  |         ) (      `.__.---- -'\               
     \7          \`-(               74\\\             
     ||       _  /`-(               l|//7__           
     |l    ('  `-)-/_.--.          f''` -.-"|         
     |\     l\_  `-'    .'         |     |  |         
     llJ   _ _)J--._.-('           |     |  l         
     |||( ( '_)_  .l   ". _    ..__I     |  L         
     ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._    
          \ |           ) /.              ``'`-.._``-.
          l l          / / |                      |''|
           " \        / /   "-..__                |  |
           | |       / /          1       ,- t-...J_.'
           | |      / /           |       |  |        
           J  \  /"  (            l       |  |        
           | ().'`-()/            |       |  |        
          _.-"_.____/             l       l.-l        
      _.-"_.+"|                  /        \.  \       
/"\.-"_.-"  | |                 /          \   \      
\_   "      | |                1            | `'|     
  |ll       | |                |            i   |     
  \\\       |-\               \j ..          L,,'. `/ 
 __\\\     ( .-\           .--'    ``--../..'      '-. ''')
    quit ()
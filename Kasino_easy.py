
"""

Kasino_easy
v1.0
by Pavel Branda
released: 9.5.2021

The purpose of program "Kasino" is to quess ten numbers in range of 0-2.
Those ten numbers are 10 randomly generated integer numbers
in range 0-2.
! You have to guess the numbers in its specific order !
Eg: you guess number 3 as a 1st but it will be draw as 7th number - you don't won!
    ->you have to guess number 3 as your 7th pick (7th in order).
There are specific rules for winning:

• if you guess right all 10 values - you won 5x of the deposit value 
• if you guess right 9 values - you won 4x of the deposit value
• if you guess right 8 values - you won 3x of the deposit value
• if you guess right 7 values - you won 2x of the deposit value
• if you guess right 6 values - you won back your deposit value

• if you guess right 5 values - you lose 1/4 (25%)of the deposit value
• if you guess right 4 values - you lose 1/3 (33%) of the deposit value
• if you guess right 3 values - you lose 1/2 (50%) of the deposit value
• if you guess right 2 values - you lose 2/3 (66%) of the deposit value
• if you guess right less than 2 values - you lose the whole deposit value

(VARIANTA B: obtížnost moc vysoká -> 10 čísel v intervalu 0-2 = zvýšení šance na výhru)


*** přepis zdrojového kódu Pascal > Python...
*** zdrojový kód má: 129 řádků (bez poznámek)

"""

import sys
import time
print ("Dobrý večer")
print()
time.sleep(1)
hotovost = int(input("Kolik peněz chcete vyměnit za žetony? (min.50): "))
    
while True:  

    if hotovost < 50:
        print("Bohužel, minimum je 50. Opusťte prosím kasino.")
        sys.exit()
      
    else:
        print("Jste-li připraven ke hře, vsaďte si.")
        print("Minimální sázka je 50 Kč")
        sazka = int(input("Vaše sázka: "))
    
        while sazka <50 or sazka > hotovost:
            while sazka <50:
                print("Měl byste přihodit alespoň ", 50 - sazka)
                i = int(input("Kolik přihodíte: "))
                sazka = sazka + i


            while sazka > hotovost:
                print("Tolik nemáte, snižte prosím svou sázku.")
                print("Vaše hotovost: ", hotovost)
                sazka = int(input("Vaše sázka (min.50): "))
                break
        

            print("Sázka ", sazka, " je OK.")
            hotovost = hotovost - sazka
            print("Nyní u sebe máte hotovost: ", hotovost)
            break
    
    hotovost = hotovost - sazka
    tips = []
    
    for i in range (1,11):
        print("Tipněte ", i , ". Číslo (0-10): ")
        tip = int(input())
        tip = tips.append(tip)

    print("Vaše tipy: ")
    print(*tips, sep = ",")
    print("Pro začátek losování stiskněte klávesu Enter: ")
    input()

    draws = []

    uspesnost = 0
    import random

    for i in range(10):
        draw = draws.append(random.randint(0,2))
    for i in range(1,11):
        print(i, ".Číslo: ", draws[i-1])
    
        if draws[i-1] == tips[i-1]:
            uspesnost = uspesnost + 1
            print(" ANO! -> úspěšnost = ",uspesnost,". Stiskněte Enter.")
            input()
        else:
            print(" Nic. úspěšnost = ",uspesnost,". Stisknžte Enter.")
            input()     

    print("Vaše tipy: ")
    print(*tips, sep = ",")  
    print("Vylosováno: ")
    print(*draws, sep = ",")
    time.sleep(1)
    print('uspesnost: ', uspesnost);
    time.sleep(1)

    if uspesnost == 10:
        hotovost = hotovost + (sazka*5)
        print("Vyhráváte pětinásobek sázky = ", sazka*5)

    elif uspesnost == 9:
        hotovost = hotovost + (sazka*4)
        print("Vyhráváte čtyřnásobek sázky = ", sazka*4)
    
    elif uspesnost == 8:
        hotovost = hotovost + (sazka*3)
        print("Vyhráváte trojnásobek sázky = ", sazka*3)
    
    elif uspesnost == 7:
        hotovost = hotovost + (sazka*2)
        print("Vyhráváte dvojnásobek sázky = ", sazka*2)
    
    elif uspesnost == 6:
        hotovost = hotovost + sazka
        print("Vyhráváte zpět svou sázku = ", sazka)
    
    elif uspesnost == 5:
        vyhra = sazka - (sazka // 4)
        hotovost = hotovost + vyhra
        print("Vyhráváte 3/4 ze své sázky = ", vyhra)
    
    elif uspesnost == 4:
        vyhra = sazka - (sazka // 3)
        hotovost = hotovost + vyhra
        print("Vyhráváte 2/3 ze své sázky = ", vyhra)
    
    elif uspesnost == 3:
        hotovost = hotovost + (sazka // 2)
        print("Vyhráváte polovinu ze své sázky = ", sazka // 2)
    
    
    elif uspesnost == 2:
        hotovost = hotovost + (sazka // 3)
        print("Vyhráváte třetinu ze své sázky = ", sazka // 3)
    
    else:
        print("Ztrácíte celou sázku = ", -sazka)
                     
    print("Vaše hotovost: ", hotovost)
    time.sleep(1)

    if hotovost < 50:
        print("Vaše hotovost bohužel nedosahuje stanoveného minima.")
        print("Prosím, opusťte kasino.")
        sys.exit()

    else:
        print("Chcete-li skončit, napište Konec a stiskněte Enter.")
        print("Pro pokračování ve hře stiskněte samotné Enter.")
        answer =input()
    
    if answer == ("Konec" or "konec"):
        sys.exit()
    if (hotovost < 50):
        sys.exit()
    else:
        continue

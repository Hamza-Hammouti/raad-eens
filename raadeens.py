import random

tries = 10
ronde = 0
score = 0
geraden = True
verder = True

print("Het getal is tussen de 0 en de 1000")

while geraden == True and verder == True:
    geraden = False
    number = random.randint(0,1000)
    print(number)

    while ronde <= 20:
        poging = int(input("Welk getal raad je?: "))
        verschil = number - poging
        print("-----------------------------------")
    
        if verschil >= -50 and verschil <= -20:
            print("Je bent warm")

        elif verschil >= 20 and verschil <= 50:
            print("Je bent warm")

        elif verschil >= -20 and verschil <= 20:
            print("Je bent heel warm")

        if poging > number:
            print("Het antwoord is kleiner")

        elif poging < number:
            print("Het antwoord is hoger")   

        if poging == number:
            geraden = True
            print("Je hebt het antwoord geraden!")
            ronde = ronde + 1
            score = score + 1
            print ("Score: " + str(score))
            number = random.randint(0,1000)
            tries = 10

            verderinput = input("Wil je verder gaan? (Ja of nee): ").lower()
            if verderinput == "ja":
                verder == True
                tries == 10
            if verderinput == "nee":
                verder == False
                print("De game wordt nu gestopt.")
                print("Jouw eindscore is: " + str(score))
                exit()
    
        elif poging != number:
            tries = tries - 1
            print("Je hebt nog " + str(tries) + " poging(en).")

        if tries == 0:
            print("-----------------------------------")
            print("Je hebt te vaak het verkeerde antwoord gegeven.  ")

            verderinput = input("Wil je verder gaan? (Ja of nee): ").lower()
            if verderinput == "ja":
                verder == True
            if verderinput == "nee":
                verder == False
                print("De game wordt nu gestopt.")
                print("Jouw eindscore is: " + str(score))
                tries == 10
                exit()
    
    if ronde >= 21:
        print("Je hebt het einde bereikt")
        print("Je eindscore is: " + str(score))
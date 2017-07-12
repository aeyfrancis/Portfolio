from time import sleep
from os import system
system("cls")

print("Hi! Welcome to my game!")
sleep(1)

'''welcomeString = "Hi! Welcome to my game")
print(welcomeString, end="!")

for H in welcomeString:
    if H != "\n":
        print(H, end ="i". flush = True)
        sleep(0.1)'''

#Thirst question
print("Hmm... I'm kind of thirsty. Aren't you?")
print()
print("1. Yes")
print("2. No")

yesnoSelection = int(input("Choice"))

if yesnoSelection is 1:
    print("Well, we'll have to do something about that huh")
elif yesnoSelection is 2:
    print("Well TOO BAd, you're thirsty. Feel the thirst")
else:
    print("Pick 1 or 2. Do it.")

#Store question
print("Pick your store")
print()
print("1. Starbucks")
print("2. Liquiteria")
print("3. McDonalds")

storeSelection = int(input("Select your store"))

if storeSelection is 1:
    print("Good choice!")
elif storeSelection is 2:
    print("Very good choice!")
elif storeSelection is 3:
    print("Seriously? If you say so, bud")
else:
    print("Um excuse you, how bout no. Try again.")

#Drink question
print("Choose your drink")
print()
print("1. Frappucino")
print("2. Coffee")
print("3. Tea")
print("4. Smoothie")

drinkSelection = int(input("Which one?"))

if drinkSelection is 1:
    print("Nice!")
elif drinkSelection is 2:
    print("How do you do it - how do you drink coffee? Disgusting creature you are. Alright.")
elif drinkSelection is 3:
    print("You're not the only one who loves tea!")
elif drinkSelection is 4:
    print("Delicious choice!")
else:
    print("Pick 1, 2, or 3")

#Cup size
print("How much of it would you like?")
print()
print("1. Kids size")
print("2. Small")
print("3. Regular")
print("4. Medium")
print("5. Large")
print("6. Bucket sized")

sizeSelection = int(input("Select your cup size"))

if sizeSelection is 1:
    print("Okay!")
elif sizeSelection is 2:
    print("Alright!")
elif sizeSelection is 3:
    print("Cool!")
elif sizeSelection is 4:
    print("Delicious choice!")
elif sizeSelection is 5:
    print("Wow")
else:
    print("Wow, you're really going for it aren't you")

#Sugar
print("How many sugar cubes would you like in your drink?")
print()
print("1. 0")
print("2. 1")
print("3. 2")
print("4. 3")
print("5. 18")

sugarSelection = int(input("Choice"))

if sugarSelection is 1:
    print("None? I mean if you insist.")
elif sugarSelection is 2:
    print("Alright!")
elif sugarSelection is 3:
    print("Nice!")
elif sugarSelection is 4:
    print("Okay!")
else:
    print("You rebel")

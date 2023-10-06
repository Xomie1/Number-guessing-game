from random import randint
guess = 5
number = randint(1,10)
while guess > 0: 
    user = eval(input("Please guess a number: "))
    if user != number:
        guess -= 1
        print(f"Oh no!, you have {guess} tries left")
    else:
        print("Yay!!!")
        break
if guess == 0:  
    print(f"Correct number is {number}")
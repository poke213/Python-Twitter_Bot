#uses rand, pee pee poo poo
import random

rand = random.randint(1, 1000)
user = 0
while(user != rand):
    user = int(input("Enter a guess: "))
    
    if(user == rand):
        user = 1
        print("Guess is correct")
        break
    elif(user > rand):
        print("Lower")
    elif(user < rand):
        print("Higher")
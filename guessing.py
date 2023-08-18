import random

jackpot = random.randint(1,50)

Guess = int(input("Please Guess a One Number : "))

Counter = 1

while Guess != jackpot:
    if Guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")
    
    Guess = int(input("Please Guess a One Number : "))
    Counter +=1
    

print("Congrats ! You Guessed Right")
print("You Took",Counter,"attempts")


# while Guess != jackpot:
#     if Guess < jackpot:
#         print("Guess Higher")
#     else:
#         print("Guess Lower")
    
#     Guess = int(input("Please Guess a One Number : "))
#     Counter +=1
    

# print("Congrats ! You Guessed Right")
# print("You Took",Counter,"attempts")
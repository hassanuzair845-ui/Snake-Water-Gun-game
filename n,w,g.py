import random
choices=["snake","water","gun"]
print("Welcome to the best game in the world")
user_score=0
computer_score=0
rounds=int(input("Enter total numbers of rounds: "))

for round_number in range(1,rounds+1):
    print(f"Total numbers of round are {round_number} of {rounds}")

    player=input("Enter your choice (snake, water, gun) :").lower()
    if player not in choices:
        print("Its invalid choice Computer gets a point")
        computer_score+=1
        continue
    computer=random.choice(choices)
    print(f"you choose: {player}")
    print(f"computer  choose: {computer}")

    if player==computer:
        print("its tie")

    elif (player=="snake" and computer=="water") or \
    (player=="water" and computer=="gun") or\
    (player=="gun" and computer=="snake"):
        
        print("Congratulations You win this round! ")
        user_score+=1

    else:

        print("Computer wins this round!")
        computer_score+=1

    print(f"you score{user_score} | computer score {computer_score} ")

print("\n final result: ")

if user_score>computer_score:
                
                print("WOOHOOO Congratulations you are the victorious ")
elif user_score<computer_score:
                print("You looses better luck next time")

else:
        print("Its a tie " )







    



import random
import time

print("----------------------------------------------------------------------------------------------")
print("|                                                                                            |")
print("|                              GUESS THE RIGHT NUMBER  !!!!!!!                               |")
print("|                                                                                            |")
print("----------------------------------------------------------------------------------------------") 

name: str = input("Enter your name: ")
print(f"Hello {name}, welcome to the random number guessing game! You have only 7 guesses to find the random number!!")
guess_number = random.randrange(100)
chances = 7
guess_count = 0

# Start the timer
start_time = time.time()

while guess_count < chances:
    guess_count += 1
    print(guess_count ,"your chance count")
    
    player_guess = int(input("Enter your number: "))

    if player_guess == guess_number:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Yahoo!!! You made it, congratulations {name}!! You found it in {guess_count} attempts and it took you {elapsed_time:.2f} seconds.")
        break

    elif player_guess != guess_number and guess_count >= chances:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Aww!! The answer is {guess_number}. Your attempts are over! Better luck next time {name}!! It took you {elapsed_time:.2f} seconds.")
    
    elif player_guess > guess_number:
        print("Your guess is too high!!")

    elif player_guess < guess_number:
        print("Your guess is too low!!")
   
    elif guess_count >= chances - 3 and abs(player_guess - guess_number) >= 5 and abs(player_guess - guess_number) <= 8:
        print("Your guess is close!!")


print("------------------------------------THANK YOU-----------------------------------------------------------")
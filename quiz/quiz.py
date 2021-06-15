def check_guess(guess,answer):
    global score
    attempts = 0
    still_guessing = True
    while still_guessing and attempts<3:
        if guess.lower() == answer.lower():
            print("Hooray!You have Guessed Right")
            score = score + 1
            still_guessing = False
        else:
            if attempts<2:
                guess = input("Sorry! Wrong anser. Try again!\n")
            attempts = attempts+1
    if attempts == 3:
        print("The corrext answer is ",answer)

score=0
print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the larget animal? ")
check_guess(guess3, "Blue Whale")
print("Your Score is "+ str(score))

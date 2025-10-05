import random
enter = input(("\nWelcome to Guess the pokemon challenge! \n\n-press enter to continue-"))
if enter == "":
    print("\n-----------------------------------------\nRules:\n\t -Use only lower case. \n\t -Do not use any symbols or numbers.\n\t -Only one letter per attempt.\n-----------------------------------------")
while True:
    words = {"magnemite": "It discharges electromagnetic waves and so on from the units at its sides while constantly hovering ", "rapidash": "Evolved from ponyta.", "wattrel": "When its wings catch the wind, the bones within produce electricity.", "eevee": "A cute pokemon that has 8 evolutions. Associated with Chloe from pokemon journeys.", "sprigatito": "A cat-like pokemon which can produce soothing scent from it's paws", "pikachu": "One of the classic pokemon which is known by everyone!", "ditto": "This pokemon can transform itself to any pokemon it encounters with."}
    word, hint = random.choice(list(words.items()))
    guessed_word = ["_"] * len(word)
    attempts = len(word) + 3

    again = input("\n-press enter to continue-")
    if again == "":
        print("\nHint: " + hint) 
        print("\nYour word: ", guessed_word)
    while attempts > 0 and "_" in guessed_word:
        print("\nYou have ",str(attempts)," attempts left. \nGuess a letter:")
        guess = input().lower()

        if len(guess)!= 1:
            print("please enter a single letter")
            continue

        if guess in word: 
            for i in range(len(word)): 
                if word[i] == guess: 
                    guessed_word[i] = guess
            print("Good guess! Your word so far: ", guessed_word)
        else: print("Oops! That letter is not in the word.")

        attempts-=1
    if "_" not in guessed_word:
        print("\nCongratulations! You have guessed the pokemon!",word)
    else: 
        print("\nSorry, you've run out of attempts. The pokemon was:",word)
    
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again != "yes": 
        print("\nThanks for playing come again later !") 
        break
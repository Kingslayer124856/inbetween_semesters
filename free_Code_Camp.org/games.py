# Mad Limbs Game
color = input("Enter a colour: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

# make my own mad limb game as extra work

# Guessing game with while loop
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not (out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You Win!")

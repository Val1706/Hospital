from random import randint





def print_welcome():

    print("""

I am thinking of a 3-digit number. Try to guess what it is.



Here are some clues:



When I say:    That means:



  Cold       No digit is correct.



  Warm       One digit is correct but in the wrong position.



  Hot        One digit is correct and in the right position.""")





def check_for_duplicates(secret_number):

    secret_number = str(secret_number)

    temporary_storage = []



    for digit in secret_number:

        if digit not in temporary_storage:

            temporary_storage.append(digit)



    if len(temporary_storage) == 3:

        without_duplicates = True

    else:

        without_duplicates = False



    return without_duplicates





def right_formated_input(guess):



    while not guess.isdigit() or len(guess) != 3:

        guess = input("Guess number: ")

        if not guess.isdigit() or len(guess) != 3:

            print("It's not a number or length of number is not equal to 3 elements")



    return guess





def main():

    print_welcome()

    equal_elements = False

    game_is_on = True

    count_guesses = 0



    cold = 0



    while not equal_elements:

        secret_number = randint(100, 999)

        equal_elements = check_for_duplicates(secret_number)



    secret_number = str(secret_number)

    print(secret_number)



    while game_is_on:

        cold = 0

        guess = ""

        guess = right_formated_input(guess)

        count_guesses += 1

        guess_copy = guess



        print(count_guesses)



        for i in range(3):

            if guess[i] == secret_number[i]:

                print("hot ", end = "")

                cold += 1

                guess = guess.replace(guess[i], "H")



        for i in range(3):

            if guess[i] != secret_number[i] and guess[i] in secret_number:

                if guess[i] != "H":

                    print("warm", end=" ")

                    cold += 1

        if cold == 0:

            print("cold")

        print()



        if guess_copy == secret_number or count_guesses == 10:

            print("The End!")

            game_is_on = False





if __name__ == "__main__":

    main()










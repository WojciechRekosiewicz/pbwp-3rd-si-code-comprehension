#Program pyta o imię, które musimy wprowadzić, a potem musimy odgadnąć w 6 próbach losową liczbę od 1 do 20.
import random #importuje modul random

guesses_taken = 0 # przypisuje wartość 0 do guesses_taken

print('Hello! What is your name?') # zwraca- Hello! What is your name?
myName = input() #wartość myName przujmuje wartość input

number = random.randint(1, 20) # wartość number przyjmuje losową wartość od 1 do 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # zwraca - Well... razem z wartością myName którą otrzymal na początku

while guesses_taken < 6: # pętla while z warunkiem guesses_taken < 6
    print('Take a guess.') # zwraca- Take a guess.
    guess = input() # wartość guess przyjmuje wartość wprowadzoną przez użytkownika
    guess = int(guess) # wartość guess przyjmuje wartość która musi być integerem

    guesses_taken += 1 #iteracja. do wartości guesses_taken zostaje dodane 1

    if guess < number: # warunek jeśli zmienna guess jest mniejsze od zmiennej number
        print('Your guess is too low.') # jeśli warunek zostanie spelniony zwraca- Your guess is too low.

    if guess > number: # warunek jeśli zmienna guess jest wieksza od zmiennej number
        print('Your guess is too high.') # jeśli warunek zostanie spelniony zwraca- Your guess is too high.

    if guess == number: # warunek jeśli zmienna guess jest równa zmiennej number
        break # jeśli warunek zostaje spelniony przerywa loop i przechodzi dalej

if guess == number:  # warunek jeśli zmienna guess jest równa zmiennej number
    guesses_taken = str(guesses_taken) # zmienna guesses_taken zostaje przesztalcona z int na stringa.
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') # zwraca- Good job.. razem z wartością zmiennej myName oraz wartością zmiennej guesses_taken

if guess != number: # warunek jeśli zmienna guess nie równa się zmiennej number
    number = str(number) # zmienna number zostaje przeksztalcona z int na stringa
    print('Nope. The number I was thinking of was ' + number) # zwraca- Nope. The number I w... razem z wartością zmiennej number

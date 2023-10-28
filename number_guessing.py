import random
#you can pass these message in the variables below right inside the print function
#but i decided to put them in a variable
small = 'is small'
large = 'is large'
number = random.randrange(1, 10)
guess = int(input('Enter any number: '))
while number != guess:
    if guess < number:
        print(guess, small)
        guess = int(input('try again: '))
    elif guess > number:
        print(guess, large)
        guess = int(input('try again: '))
    else:
        break
print('Great,', guess, '=', number)

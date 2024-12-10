# while-practice
# Henry Roeser 
# 12/10/24

# 7-4 Pizza Toppings
prompt = 'Enter a pizza topping: '
active = True 
while active:
    message = input(prompt).lower()
    if message == 'quit':
        active = False
    else:
        print(f'I will add {message} to your pizza.')
# 7-5 Movie Tickets 
active = True
while active:
    age = int(input('Enter your age: '))
    if age != -9999 and age <= 3:
        print('Your ticket is free.')
    elif age > 3 and age <= 12:
        print('Your ticket is $10.')
    elif age > 12:
        print('Your ticket is $15.')
    else:
        active = False

print('Thanks for using my Movie Tickets script.')

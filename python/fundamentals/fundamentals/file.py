# variable declaration
num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
# type check
print(type(fruit))
# log statements
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

# going to print it's greater
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# going to print just right
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# forloops 
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0

# while loop
while(x < 5):
    print(x)
    x += 1

# pop off pizza_toppings
pizza_toppings.pop()
pizza_toppings.pop(1)

# log statement
print(person)
person.pop('eye_color')
print(person)

# conditional forloop print for pizza_toppings
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

# funtion print hello ten times
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

# execute function
print_hello_ten_times()

# function print hello x times
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

# execute function with variable 4
print_hello_x_times(4)

# function print hello x or ten times 
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

# execute the function
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
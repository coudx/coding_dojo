# Write the code to print a literal string saying "Hello World" (#1)
print("Hello World")

# Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a comma in the print function(  # 2a)
name = "Cloud Xu"
print(f"Hello {name}!")

# Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a + in the print function(  # 2b)
print("Hello " + name + "!")

# Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a comma in the print function(  # 3a)
num = 521
print("Hello", num)

# Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a + in the print function(  # 3b)
# NINJA BONUS: Figure out how to resolve the error from above, without changing the + sign to a comma
print("Hello " + str(num))

# Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with the format method(  # 4a)
print("I love to eat {food_one} and {food_two}.".format(food_one="lobster", food_two="pineapple"))

# Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with the format method(  # 4a)
food_one="lobster"
food_two="pineapple"
print(f"I love to eat {food_one} and {food_two}.")


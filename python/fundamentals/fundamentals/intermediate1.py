# Update Values in Dictionaries and Lists

x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

'''
Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30
'''
x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30
print(x)
print(students)
print(sports_directory)
print(z)

# Iterate Through a List of Dictionaries
'''
Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
should output: (it's okay if each key-value pair ends up on 2 separate lines;
bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
'''
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(dict):
    for key in dict:
        print(
            "fist_name - {}, last_name - {}".format(key["first_name"], key["last_name"]))


iterateDictionary(students)

# Get Values From a List of Dictionaries
'''
Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name,
the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
Michael
John
Mark
KB
And iterateDictionary2('last_name', students) should output:
Jordan
Rosales
Guillen
Tonel
'''


def iterateDictionary2(key, dict):
    for keys in dict:
        print(keys[key])


iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

# Iterate Through a Dictionary with List Values
'''
Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
prints the name of each key along with the size of its list, and then prints the associated 
values within each key's list. For example:
# output:

7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank

8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dict):
    keys = dict.keys()
    for key in keys:
        print(len(dict[key]), key.upper())
        for val in dict[key]:
            print(val)


printInfo(dojo)

#ternary operator

# age = int(input("Enter your age: "))
# message = "You are Welcome!" if age >=18 else "You are not allowed!"
# print(message)
                #if-elif-else

# discount = 0
# price = float(input("Enter the price: "))
# if price >= 1000:
#     discount = 0.1
# elif price >= 500:
#     discount = 0.05
# else:
#     discount = 0
# final_price = (1 - discount) * price
# print(f"price after discount is: {final_price}$")

                #chained comparison

# age = int(input("Enter your age: "))
# if age >= 0 and age <= 12: # old way
#     print("You are a child.")
# elif  13 <= age <= 19:     # chained comparison
#     print("You are a teenager.")
# else:
#     print("You are an adult.")  

                #match-case 

# http_status = 404
# match http_status:
#     case 200:
#         print("Success!")
#     case 400:
#         print("Bad Request")
#     case 404:
#         print("Not Found")
#     case 500 | 501:  # The | (pipe) means "OR"
#         print("Server Error")
#     case _:
#         print("Unknown status code")

                #while loop in guessing game

# import random
# secret_number = random.randint(1, 10)
# guess = None
# print("Guess the secret number between 1 and 10!")
# while guess != secret_number:
#     guess = int(input("Enter your guess: "))
#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the secret number.")


                #for loop 

# for i in range(6):
#     print(f"Iteration number: {i} -> {i * '$'}")

# print()  # Print a newline for better readability


# for i in range(1, 4):
#     print("Iteration number:", i, "->", i * '$')

# print()  # Print a newline for better readability

# for i in range(1, 10, 2):
#     print("Iteration number:", i, "->", i * '$')

# print()  # Print a newline for better readability

# frutis = ["apple", "banana", "cherry"]
# for fruit in frutis:
#     print("I like", fruit)

# print()  # Print a newline for better readability

# for item in [10, 20, 30, 40]:
#     print(item * 2)

# print()  # Print a newline for better readability

# for i in "Elsafty": #iterable string
#     print(i)


# print()  # Print a newline for better readability


                    # User Input Validation:

# age = 0

# while age < 18:
#   age = int(input("Enter your age (must be 18 or older): "))

# print("You are old enough to proceed.")

                    #guessing game with while loop
# secret = 7
# guess = None
# cnt = 0
# while guess != secret:
#     cnt +=1
#     guess = int(input("Guess the secret number (between 1 and 10): "))
# print("Pravo!!")


                    # Searching in a List with While Loop:
# shopping_list = ["apples", "bread", "milk", "cheese"]
# item_found = False

# while not item_found:
#   item = input("Search for an item in your list (or 'q' to quit): ").lower()
#   if item == "q":
#     break  # Exit the loop if user enters 'q'
#   if item in shopping_list:
#     item_found = True
#     print(f"{item} is on your shopping list.")
#   else:
#     print(f"{item} is not on your list.")

                #nested while loop
# i = 5
# while i > 0:
#     j = 1
#     while j <= i:
#         print(j, end=' ')
#         j += 1
#     print()
#     i -= 1


# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end=' ')
#     print()

                            #pyramid pattern
# row = 7
# cur = 1
# while row >= cur:
#     star_cnt = (2*cur) -1
#     space_cnt = row - cur
#     while space_cnt:
#         print(" ", end='')
#         space_cnt -= 1
#     while star_cnt:
#         print("*", end='')
#         star_cnt -= 1
#     print()
#     cur += 1
#                             # OR
# row = 7
# for i in range(1,row+1):
#     print(' '*(row-i) + '*'*(2*i-1))
   
#                 multiplication table using nested loops
# for i in range (1,11):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i*j}", end='\t')
#     print()


                    # fnction definition and call
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Abdelrahman")

# def add(a,b):           # regular function
#     return a+b
# print(add(3,5))

# sum = lambda a,b: a+b       # lambda function
# print(sum(4,6))

                            #global variable
# cnt = 0
# def increment():
#     global cnt
#     cnt += 1
    
# increment()
# print(cnt) # 1

#                             #nonlocal variable      
# def outer_function():
#     x = 10 
#     def inner_function():
#         nonlocal x  # Using nonlocal to modify x from the enclosing(outer) function
#         x += 5      # to make it modifiable , not just readable

#     inner_function()  # 
#     print("Modified value of x from inner function:", x)

# outer_function()

# num = 5
# def check(x):
#     return "Even" if x % 2 == 0 else "Odd"
# print(check(num))


                    #Data Structures: Lists, Tuples, sets,and Dictionaries

tub=(1,2,3) #tuples are ordered and immutable 
print(tub)
print(type(tub))
# tub[0]=10   immutable (we cannot change their elements)

li = list(tub) #convert tuple to list
li[0]=10
print(li)
print(type(li))

my_list = [1, 2, 3, 4, 5]  # list is ordered and mutable
print(my_list) 
my_list.pop()  # removes last element
print(my_list)
my_list.append(6)  # adds element at the end
print(my_list)
my_list[0] = 10  # modify element
print(my_list)
print(my_list[::-1])  # reverse list
print(my_list[1:4])  # slicing
print(len(my_list))  # length of list
my_list.sort()  # sort list
print(my_list)
print(my_list[:-2]) # all elements except last two
del my_list[1]  # delete element at index 1
print(my_list)
print(3 in my_list)  # check membership
print(my_list.index(4))  # index of element
print(my_list.count(2))  # count occurrences of element

print("=============================")

#set
set_a = {1, 2, 2, 2, 3, 4, 4, 5}  # set is unordered and mutable
print(set_a)
print(type(set_a))
print(len(set_a))  # length of set (duplicates are removed)
set_a.add(6)  # add element
print(set_a)
set_a.remove(3)  # remove element
#print(set_a[2])  # sets are unordered, cannot access by index
print(set_a)
set_a.discard(10)  # remove element if exists, no error if not
print(set_a)
print(2 in set_a)  # check membership
x={10,20,20,20,30,30}
y={30,10,20}
print(x==y)  # sets are equal if they have same elements, order doesn't matter
lst = [1,2,2,3,4,4,5]
unique_set = set(lst)  # convert list to set to remove duplicates
print("Unique elements:", unique_set)
set_b = {20,40,40,80,100,100,100}
set_c = {10,10,30,30,30,50,40,20}
union_set = set_b.union(set_c)  # union
print("Union OR: ", union_set)
intersection_set = set_b.intersection(set_c)  # intersection
print("Intersection AND: ", intersection_set)
difference_set = set_b.difference(set_c)  # difference
print("Difference b - c: ", difference_set)    


print("=============================")
                    #dictionary
my_dict = {"k1": 1, "k2": 2, "k3": 3}
print(my_dict)

xdict = ([("a", 10), ("b", 20), ("c", 30)])  # list of tuples
print(xdict)
dictx = dict(xdict)  # convert list of tuples to dictionary
print(dictx)

print(dictx["b"])
dictx["d"] = 40  # add new key-value pair
print(dictx)
dictx["a"] = 15  # modify value for key 'a'(key is immutable while value is mutable) ,key must be unique
print(dictx)

dicty = dict()
dicty["first"] = 100
dicty["second"] = 200
dicty["third"] = 300    
print(dicty)
print(len(dicty))  # length of dictionary
print("second" in dicty)  # check if key exists navigation with the key NOT value

print(set(dicty))  # get all keys as a set
print(set(dicty.values()))  # get all values

def searchfun(d,target):
    for key in d:
        if d[key] == target:
            return key
    return dict()
print(searchfun(dicty,200)) # second
print(searchfun(dicty,500)) # {}


                    #scope of variables
count = 10 
def outer_fun():
  count = 5   

  def inner_fun():
    count = 2  
    print(f"Inner function: {count}")  

  inner_fun()
  print(f"Outer function: {count}")  

print(f"Global scope: {count}")  

outer_fun()

print("===================================")

z = 10
def outer():
    z = 20
    def inner():
        nonlocal z # to modify the z in the outer function
        z = 30
        print("Inner:", z)
    inner()
    print("Outer:", z)
outer()
print("Global:", z)

print("===================================")

z2 = 10
def outer2():
    global z2 # to modify the global z
    z2 = 20
    def inner2():
        # global z # if we want to modify the global z from inner function
        z2 = 30
        print("Inner 2:", z2)
    inner2()
    print("Outer 2:", z2)
outer2()
print("Global 2:", z2)

print("===================================")
z3 = "I am global"
def outer3():
    #
    def inner3():
        #
        print("Inner 3:", z3)  # can access global z3

    inner3()
    print("Outer 3:", z3)  # can access global z3

outer3()
print("Global 3:", z3)
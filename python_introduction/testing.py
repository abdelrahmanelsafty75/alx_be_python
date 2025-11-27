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
row = 7
cur = 1
while row >= cur:
    star_cnt = (2*cur) -1
    space_cnt = row - cur
    while space_cnt:
        print(" ", end='')
        space_cnt -= 1
    while star_cnt:
        print("*", end='')
        star_cnt -= 1
    print()
    cur += 1
                            # OR
row = 7
for i in range(1,row+1):
    print(' '*(row-i) + '*'*(2*i-1))
   
#                 multiplication table using nested loops
# for i in range (1,11):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i*j}", end='\t')
#     print()


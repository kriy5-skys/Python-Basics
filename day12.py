# # While loop
# i = 0
# while i<5:
#     print(i)
#     i = i + 1

# i = 1
# sum_even = 0
# print("The even numbers are: ")
# while i <= 20:
#     if i%2== 0:
#         print(i, end=" ")
#         sum_even = sum_even + i
#     i = i+1

# print("\nThe addition of the above even numbers is: ", sum_even)

# Game:
import random

# # print(int(random.random()*100))
# To guess the number and count in how many times it matches.

# random_num = random.randint(1,100)
# print(random_num)
# count = 1

# while True:
#     user_num = int(input("Enter your guess number: "))
#     if user_num == random_num:
#         print(f'The number is matched in {count} times.')
#         break
#     else:
#         print("Try again.")
#     count = +1

# # print(f'You have tried {count} times.')

# To guess within 5 times. I tried
# random_num = random.randint(1,100)
# print(random_num)
# count = 1
# i = 1
# while i<=5:
#     user_num = int(input("Enter your guess number: "))
#     if user_num == random_num:
#         print(f'The number is matched in {count} times.')
#         break
#     else:
#         if i == 5:
#             print(f'You are not able to guess.The random number was: {random_num}.')
#         else:
#             print("Try again.")
#     count = count + 1

# To guess within 5 times. Sir tried
# random_num = random.randint(40,80)
# print(random_num)
# count = 1
# limit = 5

# while True:
#     if count == 5:
#         print("Limit exceeded.",random_num)
#         break
#     user_num = int(input("Enter your guess number: "))
#     if user_num == random_num:
#         print(f'The number is matched in {count} times.')
#         break
#     else:
#         print("Try again.")
#     count = count + 1

# To guess within 5 times, and again let the user try again to guess.
# random_num = random.randint(1,100)
# print(random_num)
# count = 0
# limit = 5

# while True:
#     if count == 5:
#         print(f'limit exceeded. {random_num}')
#         ans = input("Would you try again? Yes/No: ").lower()
#         if ans == "yes":
#             random_num = random.randint(1,100)
#             count = 1
#         else:
#             print("Thank you.")
#             break
#     user_num = int(input("Enter your guess number: "))
#     if user_num == random_num:
#         ans = str(input("Would you try again? Yes/No: "))
#         if ans == "Yes":
#             random_num = random.randint(1,100)
#             count = 0
#         else:
#             print("Thank you.")
#             break
#     else:
#         print("Try again.")
#     count = count + 1
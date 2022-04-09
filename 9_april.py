# find All keyword in python.

# import keyword
# print("The list of keyword in python is")
# print(keyword.kwlist)

#####################################################################################################

# NameSpaces

# num1 = 5                         # global Namespace

# def my_funtion():
# 	num2 = 6                     # local Namespace

# 	def inner_function():
# 		num3 = 7                 # nested local Namespace

#################################################################################################### 
#Declared using Continuation Character (\)
# var1 = 1 + 2 + 3 + \
# 6 + 7 + 8
# print(var1)

#Declared using parentheses ()
# var2 = (1*2+5+4/8*5)

#Declared using square brackets []
# var3= ['Ali', 'Ahmed', 'Habib']

#Declared using braces {}
# var4 = {45 + 8 + 2 + 7 + 52 + 15}
# print(var4)

#Declared using semicolons(;)
# var5 = 5 ; var6 = 45 ; var7 = 15
 
#################################################################################################### 

# Indentation
# if 4 > 2:
#     print(True)

#################################################################################################### 
# Single line comment
'''Multiline Comment'''

#################################################################################################### 
#Structuring Python Programs

# def Python(var1):
#     pass

# def java(var2):
#     pass

# def JS(va3):
#     pass

# Python(4)
# java(5)
# JS(6)

#################################################################################################### 
#How to check if a string is a valid keyword in Python?

# import keyword
# str = "else"
# output = keyword.iskeyword(str)
# print(output)

#################################################################################################### 
#How to assign values to variables in Python

# a = 15
# print("The value of a is : " + str(a))

#################################################################################################### 
# How to print without newline in Python?

# print("hello", end= " ")
# print("hy")

#################################################################################################### 
#Decision making

# num = 10 
# if (num<10):
#     print("Number is less then 10")

# elif (num>10):
#     print("Number is greaer then 10")

# else:
#     print("Number is equal to 10")

# #################################################################################################### 
# #Basic calculator program using Python

# # Python program for simple calculator

# # Function to add two numbers
# def add(num1, num2):
# 	return num1 + num2

# # Function to subtract two numbers
# def subtract(num1, num2):
# 	return num1 - num2

# # Function to multiply two numbers
# def multiply(num1, num2):
# 	return num1 * num2

# # Function to divide two numbers
# def divide(num1, num2):
# 	return num1 / num2

# print("Please select operation -\n" \
# 		"1. Add\n" \
# 		"2. Subtract\n" \
# 		"3. Multiply\n" \
# 		"4. Divide\n")


# # Take input from the user
# select = int(input("Select operations form 1, 2, 3, 4 :"))

# number_1 = int(input("Enter first number: "))
# number_2 = int(input("Enter second number: "))

# if select == 1:
# 	print(number_1, "+", number_2, "=",
# 					add(number_1, number_2))

# elif select == 2:
# 	print(number_1, "-", number_2, "=",
# 					subtract(number_1, number_2))

# elif select == 3:
# 	print(number_1, "*", number_2, "=",
# 					multiply(number_1, number_2))

# elif select == 4:
# 	print(number_1, "/", number_2, "=",
# 					divide(number_1, number_2))
# else:
# 	print("Invalid input")

#################################################################################################### 

#Taking input in Python

# var = input("Enter your input : ")
# print(var)
# print(type(var))

####################################################################################################
#Taking input from console in Python

#var = input()

####################################################################################################
#Taking multiple inputs from user in Python\

# var1, var2, var3 = input("Enter three inputs : ").split()
# print("1st input is : ", var1)
# print("2nd input is : ", var2)
# print("3rd input is : ", var3)
# print()

#2nd method : Talking multipul inputs as a list

# x = [int(x) for x in input("Enter multiple values: ").split()]
# print("Number of list is: ", x)

####################################################################################################

# Python 2.x program to show Vulnerabilities
# in input() function using a variable 
  
# import random
# secret_number = random.randint(1,500)
# print "Pick a number between 1 to 500"
# while True:
#     res = input("Guess the number: ")
#     if res==secret_number:
#         print "You win"
#         break
#     else:
#         print "You lose"
#         continue

####################################################################################################
#Python Input Methods for Competitive Programming

# import sys
# def get_ints(): return map(int, sys.stdin.readline().strip().split())

# arry = get_ints()

####################################################################################################
#Python | Output using print() function

#print("Hello, I'm learning Python today")

####################################################################################################
#How to print without newline in Python?

# print("Hello", end=" ")
# print("How Are You")

####################################################################################################

#Python | end parameter in print()

# print("Hello", end="! ")
# print("How Are You")

####################################################################################################
#Python | sep parameter in print()

# print("Hello", "I'm", "learning", "Python", sep="_")

####################################################################################################
#Python | Output Formatting

# print("gpa : %2.3f, cgpa : %5d" % ( 0.458, 3))
# print('I {} my Contry "{}!"'.format('love', 'Pakistan'))

# str = "I Love PaKisTan"
# print (str.center(40, '#'))

# data = dict(fun ="Python", adj ="Hack")
# print("Hello! I'm {fun} for {adj}".format(**data))


************************************* The End ********************************************************










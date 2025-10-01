# 1. Python program to add two numbers 
# one , two = map(int ,input("enter two values seperated with space : ").split())
# print(f'sum of {one} , {two} is { one + two }')



# 2. Python program to find maximum of two numbers 

# while True:
#     try:
#         one , two = map(int ,input("enter two values seperated with space : ").split())
#         break
#     except:
#         print("Invalid input! Please enter numbers only")
            
# print(f'maximum of {one} , {two} is {one if one > two else two}')




# 3. Python program for factorial of a number 
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# while True:
#     try:
#         num = int(input("enter a number to find the factorial : "))
#         break
#     except:
#         print("Invalid input! Please enter numbers only")
        
# print(f'factorial of {num} is {factorial(num)}')



# 4. Python program to calculate simple interest 
# def check_time( time):
#     # years , months = time.split(".")
#     if type(time) == float:
#         str_time = str(time)
#         print(type(str_time))
#         years , months = str_time.split(".")
#         if int(months) > 12:
#             raise ValueError("Months cannot be greater than 12")
#     if time < 0:
#         raise ValueError("Time cannot be negative")
#     elif time == 0:
#         raise ValueError("Time cannot be zero")
#     else:
#         return

# def check_time(years , months):
#     if years < 0 or months < 0:
#         raise ValueError("Time cannot be negative")
#     if years == 0 or months == 0 :
#         raise ValueError("Time cannot be zero ")
#     if months >= 12:
#         raise ValueError("months cannot be grater than or equal to 12 (convert months to years insted )")
#     return years +(months / 12)


# while True:
#     try:
#         principal = float(input("enter Amount : "))
#         rate = float(input("enter Interest Rate (do not include % symbol) : "))
#         # time = float(input("Enter time in years (months as decimal, e.g. 5.6) : "))
#         years = int(input("Enter Years : "))
#         months = int(input("Enter Months : "))
#         time = check_time(years, months)
#         # principal , rate , time = map(float ,input("enter Amount , Interest Rate (do not include % symbol) and time in years ( Enter nounths as 1/12) seperated with space : ").split())
#         break
#     except ValueError as e:
#         print(e)

# print(f'simple interest for the amount {principal} at intrest rate of {rate}% in {time} years is {(principal * rate * time) / 100}')


# 5. Python program to calculate compound interest 


# 6. Python program to check Armstrong Number 
# def check_amstrong():
#     sum = 0
#     num = input("Enter a number to check wheather it is Amstrong or not : ")
#     number_length = len(num)
#     for i in num:
#         iterated_number = int(i)
#         sum += (iterated_number**number_length)
#         # sum = sum + (int(i)^len(num))
#         # print(sum)

#     if sum == int(num):
#         print(f"{num} is an Amstrong number")
#     else:
#         print(f"{num} is not an Amstrong number")     

# check_amstrong()

# def is_amstrong(number : int)-> bool:
#     digits = str(num)
#     power = len(digits)
#     total = sum(int(digit)**power for digit in digits )
#     return total == number 


# num = int(input("enter a number to check it is amstrong or not : "))

# if is_amstrong(num):
#     print(f'{num} is an amstrong number')
# else:
#     print(f'{num} is not an amstrong number')

# 7. Python program to find area of a circle 

# pi = 3.14

# radius = int(input("enter the radius of a circle to find area : "))
# print(f'Area of a circle with radius {radius} is {pi * radius**2}')

from math import pi 

def area_of_circle(radius : float)-> float:
    return pi*radius**2

radius = float(input("enter the radius of a circle to find area : "))
print(f'are of a circle with radius {radius} is {area_of_circle(radius)}')
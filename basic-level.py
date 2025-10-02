# # 1. Python program to add two numbers 
# one , two = map(int ,input("enter two values seperated with space : ").split())
# print(f'sum of {one} , {two} is { one + two }')



# # 2. Python program to find maximum of two numbers 

# while True:
#     try:
#         one , two = map(int ,input("enter two values seperated with space : ").split())
#         break
#     except:
#         print("Invalid input! Please enter numbers only")
            
# print(f'maximum of {one} , {two} is {one if one > two else two}')




# # 3. Python program for factorial of a number 
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



# # 4. Python program to calculate simple interest 
# # def check_time( time):
# #     # years , months = time.split(".")
# #     if type(time) == float:
# #         str_time = str(time)
# #         print(type(str_time))
# #         years , months = str_time.split(".")
# #         if int(months) > 12:
# #             raise ValueError("Months cannot be greater than 12")
# #     if time < 0:
# #         raise ValueError("Time cannot be negative")
# #     elif time == 0:
# #         raise ValueError("Time cannot be zero")
# #     else:
# #         return

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


# # 5. Python program to calculate compound interest 



# # 6. Python program to check Armstrong Number 
# # def check_amstrong():
# #     sum = 0
# #     num = input("Enter a number to check wheather it is Amstrong or not : ")
# #     number_length = len(num)
# #     for i in num:
# #         iterated_number = int(i)
# #         sum += (iterated_number**number_length)
# #         # sum = sum + (int(i)^len(num))
# #         # print(sum)

# #     if sum == int(num):
# #         print(f"{num} is an Amstrong number")
# #     else:
# #         print(f"{num} is not an Amstrong number")     

# # check_amstrong()

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

# # 7. Python program to find area of a circle 

# # pi = 3.14

# # radius = int(input("enter the radius of a circle to find area : "))
# # print(f'Area of a circle with radius {radius} is {pi * radius**2}')

# from math import pi 

# def area_of_circle(radius : float)-> float:
#     return pi*radius**2

# radius = float(input("enter the radius of a circle to find area : "))
# print(f'are of a circle with radius {radius} is {area_of_circle(radius)}')

# # 8. Python program to find area of a cylinder 

# #  area of cylinder is A + 2* pi * R (r + h)

# from math import pi

# def area_of_cylinder(radius: float, height : float)-> float:
#     return 2*pi*radius* (radius + height)

# radius = float(input("enter radius of cylinder : "))
# height = float(input("enter height of cylinder : "))
# print(f'area of cylinder with radius: { radius }, height : {height} is {area_of_cylinder(radius, height)}')


# # 9. Python program to find volume of a cone 
# #  volume of cone is 1/3 * pi * r^2 * h


# from math import pi

# def volume_of_cone(radius : float, height : float)-> float:
#     return (1/3) * pi * radius**2 * height

# radius = float(input("enter radius of cone : "))
# height = float(input("enter height of cone : "))
# print(f'volume of cone with radius: { radius }, height : {height} is {volume_of_cone(radius, height)}')

# # 10. Python program to check whether a number is prime or not 

# def is_prime(number : int)-> bool:
#     if number < 2:
#         return False
#     for i in range(2 , number):
#         if number % i == 0:
#             return False
#     return True

# number = int(input("enter a number to check it is prime or not : "))
# if is_prime(number):
#     print(f'{number} is a prime number')
# else:
#     print(f'{number} is not a prime number')

# # 11. Python program to print all prime numbers in an interval 

# def is_prime(number : int)-> bool:
#     if number < 2:
#         return False
#     for i in range(2 , number):
#         if number % i == 0:
#             return False
#     return True

# start ,end = map(int, input("enter two numbers to print the prime numbers in between the range : ").split())

# # for i in range(start, end+1):
# #     if is_prime(i):
# #         print(i)

# primes = [i for i in range(start, end+1 ) if is_prime(i)]
# print(f"Prime numbers between {start} and {end}: {primes}")

# # 12. Python program for 𝑛th Fibonacci number 
# fibonacci_series = [0,1]

# num = int(input("enter a number to find the fibonacci series : "))
# # generated_list = [fibonacci_series[i-1] + fibonacci_series[i-2] for i in range(2,num)  ]
# # print(fibonacci_series + generated_list)

# for i in range(2, num+1):
#     fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
# print(fibonacci_series)


# # 13. Python program to find sum of squre of n natural numbers
# #  with formula 
# # def sum_sq_natural_numbers(number : int)-> int:
# #     return int( 1/6 * number * (number+1 ) * (2*number + 1))

# # num = int(input("enter a number to find squre of first n natural numbers : "))
# # print(f'the sum squre of first {num} natural numbers is {sum_sq_natural_numbers(num)} ')

# # without formula 
# def sum_sq_natural_numbers(number : int)->int:
#     # total = 0
#     # for i in range(1, number+1):
#     #     total = total + (i**2)
#     # return total    
#     return sum(i**2 for i in range(1, number + 1))

# num = int(input("enter a number to find squre of first n natural numbers : "))
# print(f'the sum squre of first {num} natural numbers is {sum_sq_natural_numbers(num)} ')


# # 14. Python program for cube sum of first 𝑛 natural numbers 

# def sum_cube_natural_numbers(number : int)->int: 
#     # return int((1/2 * number * (number+1 ))**2)
#     return sum(i**3 for i in range(1, number + 1))

# num = int(input("enter a number to find squre of first n natural numbers : "))
# print(f'the sum cobe of first {num} natural numbers is {sum_cube_natural_numbers(num)} ')

# # 15. Python program to compute the LCM of two numbers 

# from math import lcm
# def lcm_two_numbers(num1: int, num2:int)-> int:
#     return lcm(num1, num2)


# num1 , num2 = map(int, input("enteer two numbers two find there lcm seperated with space : ").split())
# print(f"Lcm of {num1} , {num2} is {lcm_two_numbers(num1, num2 )}")

# # 16. Python program to compute the GCD of two numbers 

# from math import gcd
# def gcd_two_numbers(num1:int, num2:int)->int:
#     return gcd(num1,num2)

# num1 , num2 = map(int, input("enteer two numbers two find there gcd seperated with space : ").split())
# print(f"Gcd of {num1} , {num2} is {gcd_two_numbers(num1, num2 )}")
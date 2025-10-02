# Python Programming Experiments

## Basic Level   
[python code](https://github.com/doer431/MAT4102_ASSIGNMENTS/blob/main/basic-level.py)

### 1. Python program to add two numbers 

``` Python

one , two = map(int ,input("enter two values seperated with space : ").split())
print(f'sum of {one} , {two} is { one + two }')

```

### 2. Python program to find maximum of two numbers  

``` Python 

while True:
    try:
        one , two = map(int ,input("Enter two values seperated with space : ").split())
        break
    except:
        print("Invalid input! Please enter numbers only")
            
print(f'maximum of {one} , {two} is {one if one > two else two}')

```

### 3. Python program for factorial of a number 
``` Python 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

while True:
    try:
        num = int(input("enter a number to find the factorial : "))
        break
    except:
        print("Invalid input! Please enter numbers only")
        
print(f'factorial of {num} is {factorial(num)}')
```

### 4. Python program to calculate simple interest 
Simple intrest (si) =( P (principple) * R (intrest rate) * T (time in years)) /100
```python
def check_time(years , months):
    if years < 0 or months < 0:
        raise ValueError("Time cannot be negative")
    if years == 0 or months == 0 :
        raise ValueError("Time cannot be zero ")
    if months >= 12:
        raise ValueError("months cannot be grater than or equal to 12 (convert months to years insted )")
    return years +(months / 12)

while True:
    try:
        principal = float(input("enter Amount : "))
        rate = float(input("enter Interest Rate (do not include % symbol) : "))
        years = int(input("Enter Years : "))
        months = int(input("Enter Months : "))
        time = check_time(years, months)
        break
    except ValueError as e:
        print(e)

print(f'simple interest for the amount {principal} at intrest rate of {rate}% in {time} years is {(principal * rate * time) / 100}')
```

### 5. Python program to calculate compound interest 


###  6. Python program to check Armstrong Number 

```python
def is_amstrong(number : int)-> bool:
    digits = str(num)
    power = len(digits)
    total = sum(int(digit)**power for digit in digits )
    return total == number 


num = int(input("enter a number to check it is amstrong or not : "))

if is_amstrong(num):
    print(f'{num} is an amstrong number')
else:
    print(f'{num} is not an amstrong number')
```
### 7. Python program to find area of a circle 

```python
from math import pi 

def area_of_circle(radius : float)-> float:
    return pi*radius**2

radius = float(input("enter the radius of a circle to find area : "))
print(f'are of a circle with radius {radius} is {area_of_circle(radius)}')
```

### 8. Python program to find area of a cylinder 

```python 
from math import pi

def area_of_cylinder(radius: float, height : float)-> float:
    return 2*pi*radius* (radius + height)

radius = float(input("enter radius of cylinder : "))
height = float(input("enter height of cylinder : "))
print(f'area of cylinder with radius: { radius }, height : {height} is {area_of_cylinder(radius, height)}')
```

### 9. Python program to find volume of a cone 

```python
from math import pi

def volume_of_cone(radius : float, height : float)-> float:
    return (1/3) * pi * radius**2 * height

radius = float(input("enter radius of cone : "))
height = float(input("enter height of cone : "))
print(f'volume of cone with radius: { radius }, height : {height} is {volume_of_cone(radius, height)}')
```

### 10. Python program to check whether a number is prime or not 

```python
def is_prime(number : int)-> bool:
    if number < 2:
        return False
    for i in range(2 , number):
        if number % i == 0:
            return False
    return True

number = int(input("enter a number to check it is prime or not : "))
if is_prime(number):
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')
```

### 11. Python program to print all prime numbers in an interval 

```python
def is_prime(number : int)-> bool:
    if number < 2:
        return False
    for i in range(2 , number):
        if number % i == 0:
            return False
    return True

start ,end = map(int, input("enter two numbers to print the prime numbers in between the range  ").split())

primes = [i for i in range(start, end+1 ) if is_prime(i)]
print(f"Prime numbers between {start} and {end}: {primes}")
```
### 12. Python program for 𝑛th Fibonacci number 

```python
fibonacci_series = [0,1]
num = int(input("enter a number to find the fibonacci series : "))

for i in range(2, num+1):
    fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])

print(fibonacci_series)
```

### 13. Python program for sum of squares of first 𝑛 natural numbers 

1. with formula 
``` python
def sum_sq_natural_numbers(number : int)-> int:
    return int( 1/6 * number * (number+1 ) * (2*number + 1))

num = int(input("enter a number to find squre of first n natural numbers : "))
print(f'the sum squre of first {num} natural numbers is {sum_sq_natural_numbers(num)} ')
```

2. without formula 
```python
def sum_sq_natural_numbers(number : int)->int:  
    return sum(i**2 for i in range(1, number + 1))

num = int(input("enter a number to find squre of first n natural numbers : "))
print(f'the sum squre of first {num} natural numbers is {sum_sq_natural_numbers(num)} ')
```

### 14. Python program for cube sum of first 𝑛 natural numbers 

```python
def sum_cube_natural_numbers(number : int)->int: 
    # return int((1/2 * number * (number+1 ))**2)
    return sum(i**3 for i in range(1, number + 1))

num = int(input("enter a number to find squre of first n natural numbers : "))
print(f'the sum cobe of first {num} natural numbers is {sum_cube_natural_numbers(num)} ')
```

### 15. Python program to compute the LCM of two numbers 

```python
from math import lcm
def lcm_two_numbers(num1: int, num2:int)-> int:
    return lcm(num1, num2)


num1 , num2 = map(int, input("enteer two numbers two find there lcm seperated with space : ").split())
print(f"Lcm of {num1} , {num2} is {lcm_two_numbers(num1, num2 )}")
```

### 16. Python program to compute the GCD of two numbers 
```python
from math import gcd
def gcd_two_numbers(num1:int, num2:int)->int:
    return gcd(num1,num2)

num1 , num2 = map(int, input("enteer two numbers two find there gcd seperated with space : ").split())
print(f"Gcd of {num1} , {num2} is {gcd_two_numbers(num1, num2 )}")
```
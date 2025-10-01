# Python Programming Experiments

## Basic Level 

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
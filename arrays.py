## . Python program to find sum of array      
# arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

# print("sum of array elements:", sum(arr))

## 2. Python program to find largest element in an array 
# arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

# print("Largest element in the array:", max(arr))

## 3. Python program to find smallest element in an array      
# arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

# print("Smallest element in the array:", min(arr))

## 4. Python program for array rotation      

# def rotate_array(arr, k):
#     n = len(arr)
#     k = k % n
#     arr[:] = arr[n - k:] + arr[:n - k]
#     return arr

# arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
# k = int(input("Enter the number of rotations: "))

# rotated_arr = rotate_array(arr, k)
# print("Rotated array:", rotated_arr)

# 5. Python program for reversal algorithm for array rotation      

# def reverse_array(arr):
#     n = len(arr)
#     for i in range(n // 2):
#         arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
#     return arr

# arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

# reversed_arr = reverse_array(arr)
# print("Reversed array:", reversed_arr)

## 6. Python program to split the array and add the first part to the end

# arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
# k = int(input("enter the position of an element to split :  "))

# arr [:] = arr[k+1:] +  arr[:k] 
# print("splited array" ,arr)

##  7. Python program for finding reminder of array multiplication divided by n

# arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
# n = int(input("enter a number to find reminder of an mul(array)  :  "))
# product = 1
# for i in arr :
#     product *= i 

# print(f"The reminder of an array {arr} is {product/ n}")

## 8. . Python program to check if given array is monotonic 


def is_inc(arr:list):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
        
def is_dec(arr:list):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            return False
    return True

def is_monotonic(arr:list)-> bool:
    return is_dec(arr) or is_inc(arr)
    # if not(is_inc(arr)) and not(is_dec(arr)):
    #     return False
    # if is_inc(arr):
    #     return True
    # elif is_dec(arr):
    #     return True
    

    # for i in range(len(arr)-1):
    #     if arr[i] > arr[i+1]:
    #         print(arr[i+1])
    #         inc = False
    #         break
        
    # for i in range(len(arr)-1):
    #     if arr[i] < arr[i+1]:
    #         print(arr[i+1])
    #         dec = False
    #         break
    # if inc == True:
    #     return True
    # elif dec == False:
    #     return False

    # return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or \
    #    all(arr[i] >= arr[i+1] for i in range(len(arr)-1))


arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
print(f"array {arr} is {"monotonic" if is_monotonic(arr) else "not monotonic"}")

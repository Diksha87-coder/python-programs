#1. Find the sum of array elements. 

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
    
sum = 0

for i in range(n):
    sum = sum + arr[i]

print("Sum of array elements:", sum)

#2. Find the average of array elements. 

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

sum = 0

for i in range(n):
    sum = sum + arr[i]

avg = sum / n

print("Average of array elements:", avg)

#3. Find the largest element. 
arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = arr[0]

for i in range(n):
    if arr[i] > largest:
        largest = arr[i]

print("Largest element:", largest)

#4. Find the smallest element. 

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

smallest = arr[0]

for i in range(n):
    if arr[i] < smallest:
        smallest = arr[i]

print("Smallest element:", smallest)

#5. Count even and odd elements. 

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

even = 0
odd = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even elements:", even)
print("Odd elements:", odd)


#6. Count positive, negative, and zero elements. 

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

positive = 0
negative = 0
zero = 0

for i in range(n):
    if arr[i] > 0:
        positive = positive + 1
    elif arr[i] < 0:
        negative = negative + 1
    else:
        zero = zero + 1

print("Positive elements:", positive)
print("Negative elements:", negative)
print("Zero elements:", zero)


#7. Search for an element using linear search. 

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter element to search: "))

found = False

for i in range(n):
    if arr[i] == search:
        print("Element found at index:", i)
        found = True
        break

if found == False:
    print("Element not found")
    
#8. Reverse an array using a for loop.

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Original array:", arr)

reverse = []

for i in range(n - 1, -1, -1):
    reverse.append(arr[i])

print("Reversed array:", reverse)

 
#9.	Find the second-largest distinct element. 

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = arr[0]
second = None

for i in range(n):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] < largest:
        if second == None or arr[i] > second:
            second = arr[i]

if second == None:
    print("Second largest element does not exist")
else:
    print("Second largest element:", second)
    
    
#10.	Sort an array in ascending order without using sort(). 

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Array in ascending order:", arr)


#11.	Find the frequency of a given element. 

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter element to find frequency: "))

count = 0

for i in range(n):
    if arr[i] == search:
        count = count + 1

print("Frequency of", search, "is:", count)


#12.	Find common elements between two arrays. 

arr1 = []
arr2 = []

n1 = int(input("Enter size of first array: "))

for i in range(n1):
    num = int(input("Enter element: "))
    arr1.append(num)

n2 = int(input("Enter size of second array: "))

for i in range(n2):
    num = int(input("Enter element: "))
    arr2.append(num)

print("Common elements:")

for i in range(n1):
    for j in range(n2):
        if arr1[i] == arr2[j]:
            if arr1[i] not in arr2[:j] and arr1[i] not in arr1[:i]:
                print(arr1[i])
                
                
#13.	Separate even and odd elements. 

arr = []
even = []
odd = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

for i in range(n):
    if arr[i] % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

print("Even elements:", even)
print("Odd elements:", odd)


#14.	Find the sum of elements at even and odd indexes. 

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

even_sum = 0
odd_sum = 0

for i in range(n):
    if i % 2 == 0:
        even_sum = even_sum + arr[i]
    else:
        odd_sum = odd_sum + arr[i]

print("Sum at even indexes:", even_sum)
print("Sum at odd indexes:", odd_sum)


#15.	Remove duplicate elements from an array.

arr = []
unique = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

for i in range(n):
    if arr[i] not in unique:
        unique.append(arr[i])

print("Original array:", arr)
print("Array after removing duplicates:", unique)
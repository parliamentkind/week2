#1
"""
1. Given a one-dimensional array of 10 integers. Find the maximum element and compare other
elements with it. Output the number of less than the maximum and greater than the maximum
element.
2. Fill in a one-dimensional array of 10 integers from the keyboard, determine the
sum of those numbers that are >5.
"""

#1
l = int(input('Enter the length of array: '))
a = []
for i in range(l):
    print('Enter the element: ')
    a.append(int(input()))
print(max(a))
a.reverse()
print(a)

#2
a = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9]
b = 0
for i in a:
    b += i
m = (b / (len(a)+1))
for i in range(len(a)):
    if a[i] == 0:
        a[i] = m
print(m, a)

#2
"""
1. Given a one-dimensional array consisting of N integer elements. Enter an array from the
keyboard. Find the minimum element. Display the index of the minimum element on the screen.
2. Given an array of integers. Rewrite all positive elements in the second array, and the rest - in
the third.
"""

#1
l = int(input('Enter the length of array: '))
a = []
for i in range(l):
    print('Enter the elements: ')
    a.append(int(input()))
print(min(a))
for i in range(l):
    if a[i] == min(a):
        print(i)

#2
a = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]
p = []
n = []
for i in range(len(a)):
    if a[i] > 0:
        p.append(a[i])
    else:
        if a[i] == 0:
            p.append(a[i])
        else:
            n.append(a[i])
print('Positive integers: ', p)
print('Negative integers: ', n)

#3
"""
1. In a one-dimensional numeric array D of length n, calculate the sum of elements with odd
indices. Display the array D, the resulting amount.
2. Given a one-dimensional array of 8 elements. Replace all array elements less than 15 with
twice their values. Display the converted array on the monitor screen.
"""
#1
l = int(input('Enter the length of array: '))
a = []
for i in range(l):
    print('Enter the element: ')
    a.append(int(input()))
sum = 0
for i in range(len(a)):
    if a[i] % 2 != 0:
        sum += a[i]
print(a, sum)

#2
a = [1, -2, 33, -3, 55, -6, 7, -77]
for i in range(len(a)):
    if a[i] < 15:
        a[i] = (a[i] * a[i])
print(a)

#4
"""
1. Given an array of integers. Find the maximum element of the array and its ordinal
number.
2. Given a one-dimensional array of integer type. Get another array consisting only of odd
numbers in the original array, or report that there are no such numbers. Output the resulting array
in descending order of elements.
"""
#1
l = int(input('Enter the length of array: '))
a = []
for i in range(l):
    print('Enter the element: ')
    a.append(int(input()))
print(max(a))
for f in range(len(a)):
    if a[f] == min(a):
        print(f)

#2
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
b = []
for i in range(len(a)):
    if a[i] % 2 != 0:
        b.append(a[i])
        b.reverse()
print(b)

#5
"""
1. Given a one-dimensional array of 10 integers. Print pairs of negative numbers next to each
other.
2. Given an integer array of size 10. Create a new array by deleting all identical elements,
leaving them 1 time.
"""
#1
l = int(input("amount of elements: "))
b = [int(input("print element: ")) for i in range(l)]
c=[]
for i in range(a):
    if b[i] < 0:
        print(b[i+1])
    if b[i] == len(b) and b[i] < 0:
        print("no pair next")

#2
a = [1, 2, -3, 4, 4, 5, -5, 0, -7, 7, -6, -4, 10]
b = [*set(a)]
print(b)

#6
"""
1. Given a one-dimensional array of 10 integers. Find the maximum element and compare other
elements with it. Output the number of less than the maximum and greater than the maximum
element.
2. Fill in a one-dimensional array of 10 integers from the keyboard, determine the
sum of those numbers that are >5.
"""
#1
a = [1, 2, 3, 4, 5, -6, 7, -8, 7, -7, 9, 11]
l = 0
g = 0
print('Max of the array: ', max(a))
for i in range(len(a)):
    if a[i] < max(a):
        if a[i] > a[i-1]:
            l = a[i]
        else:
            l = a[i-1]
    else:
        if (a[i] > a[i-1]):
            g = a[i]
            if a[i] == max(a):
                print('There are no element > than max')
        else:
            g = a[i-1]
            if a[i-1] == max(a):
                print('There are no element > than max')
print('Element less than max: ', l)

#2
a = []
l = 10
b = 0
for i in range(l):
    a.append(int(input('Enter the array elements: ')))
for i in range(l):
    if a[i] > 5:
        b += a[i]
print(b)

#7
"""
1. Given an array of integers. Find the sum of elements with even numbers and the product
of elements with odd numbers. Withdraw the amount and work.
2. Swap the minimum element and the maximum element in a one-dimensional array.
"""
#1
l = int(input('Enter the length of array: '))
a = []
for i in range(l):
    print('Enter the element: ')
    a.append(int(input()))
odd = 0
even = 0
for i in range(len(a)):
    if a[i] % 2 != 0:
        odd = odd * a[i]
    else:
        even += a[i]
print('"+" of even elements: ', even)
print('"*" of odd elements: ', odd)

#2
l = int(input('Enter the length of array: '))
a = []
for i in range(l):
    print('Enter the element: ')
    a.append(int(input()))
max1 = a.index(max(a))
min1 = a.index(min(a))
max2 = max(a)
min2 = min(a)
a[max1] = min2
a[min1] = max2
print(a)

#8 -

#9
"""
1. Given a one-dimensional array consisting of N real elements. Enter an array from the
keyboard. Find and display the minimum modulo element. Display the array in reverse order.
2. Given arrays A and B of the same size 10. Print the original arrays. Swap their contents and
print the elements of the transformed array A first, and then the elements of the transformed array
B.
"""
#1
import math
n = int(input('Enter the length of array: '))
a = []
for i in range(n):
    print('Enter the elements: ')
    a.append(int(input()))
print(math.fabs(min(a)))
a.reverse()
print(a)

#2
a = [1, 2, 3, 4, 5, 6, 7, -7, 8, -9]
b = [11, -11, 20, 30, 45, 64, 43, -5, -18, 68]
print('Array "a": ', a)
print('Array "b": ', b)
c = []
for i in range(10):
    c.append(a[i])
    a[i] = b[i]
    b[i] = c[i]
print('Array "a": ', a)
print('Array "b": ', b)

#10
"""
1. Determine if there are duplicate elements in the list, if so, display this value, otherwise a
message about their absence.
2. Given a one-dimensional array of 15 elements. Array elements less than 10 are assigned zero
values, and elements greater than 20 are assigned 1. Display the original and converted arrays in
a line on the monitor screen.
"""
#1
a = []
n = 10
d = []
for i in range(n):
    a.append(int(input('Enter the 10 array elements: ')))
for i in range(n):
    if a[i] == a[i-1]:
        d.append(a[i])
if len(d) == 0:
    print('There are no duplicate elements')
else:
    print('Duplicate elements: ', d)

#2
a = []
n = 15
for i in range(n):
    a.append(int(input('Enter the 15 array elements: ')))
for i in range(15):
    if a[i] < 10:
        a[i] = 0
    if a[i] > 20:
        a[i] = 1
print(a)


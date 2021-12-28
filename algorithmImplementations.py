import math
import time

x = 0

# Compute the greatest common denominator given two integers
def gcd(m, n):
    if n > m:
        temp = n
        n = m
        m = temp 
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

# Print all prime numbers from 2 to n
def find_primes(n):
    nums = [0] * (n - 1)
    for i in range(2, n + 1):
        nums[i - 2] = i
    for x in range(2, math.floor(math.sqrt(n) + 1)):
        if nums[x - 2] != 0:
            y = x
            while x * y <= n:
                nums[x * y - 2] = 0
                y += 1

    for i in range(0, n - 1):
        val = nums[i]
        if (val != 0):
            print(val)

# Calculate the runtime of the fibonacci function
def test_fib(n):
    global x
    x = 0
    y1 = time.process_time()
    val = fibonacci(n)
    y2 = time.process_time()
    print("Value: " + str(val))
    print("Basic operations: " + str(x))
    print("Runtime: " + str(y2 - y1) + " seconds")
    return

# Calculate the nth number in the Fibonacci sequence
def fibonacci(n):
    global x
    if n < 2:
        return n
    x += 1
    return fibonacci(n - 2) + fibonacci(n - 1)

# Utility function
def print_x():
    global x
    print(str(x) + " operations")
    x = 0

# Test four sorting algorithms
def test_sorts():
    A = [2, 5, 3, 1, 8, 7, 6, 4]
    print("Unsorted array: " + str(A))
    bubble_sort(A)
    print("Bubble sorted array: " + str(A))
    B = [2, 5, 3, 1, 8, 7, 6, 4]
    select_sort(B)
    print("Selection sorted array: " + str(B))
    C = [2, 5, 3, 1, 8, 7, 6, 4]
    insert_sort(C)
    print("Insertion sorted array: " + str(C))
    D = [2, 5, 3, 1, 8, 7, 6, 4]
    insert_sort(D)
    print("Merge sorted array: " + str(D))

# Selection sort
def select_sort(A):
    if (len(A) <= 1):
        return
    for i in range(len(A) - 1):
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        temp = A[i]
        A[i] = A[min]
        A[min] = temp

# Bubble sort
def bubble_sort(A):
    if (len(A) <= 1):
        return
    for i in range(len(A) - 1):
        for j in range(1, len(A) - i):
            if (A[j] < A[j - 1]):
                temp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = temp

# Insertion sort
def insert_sort(A):
    n = len(A)
    if(n <= 1):
        return
    A.append(float('-inf'))
    for i in range(1, n):
        v = A[i]
        j = i - 1
        while v < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
    A.pop(n)

# Merge sort
def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A
    return merge(merge_sort(A[:math.floor(n / 2)]), merge_sort(A[math.floor(n / 2):]))

# Helper function for merge sort
def merge(A, B):
    C = []
    while len(A) > 0 and len(B) > 0:
        if A[0] <= B[0]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
    C.extend(A + B)
    return C

# Binary search
def binary_search(A, k):
    m = 0
    n = len(A) - 1
    while m <= n:
        m_index = math.floor((m + n) / 2)
        mid_el = A[m_index]
        if mid_el == k:
            return m_index
        elif k > mid_el:
            m = m_index + 1
        else:
            n = m_index - 1
    return -1

# Optimized sequential search
def search(A, k):
    A.append(k)
    i = 0
    while A[i] != k:
        i += 1
    if i != (len(A) - 1):
        return i
    return -1

# String matching
def str_match(s, p):
    i = 0
    n = len(s)
    m = len(p)
    while i < (n - m + 1):
        for j in range(m):
            if s[i + j] != p[j]:
                j -= 1
                break
        if j == m - 1:
            return i
        i += 1
    return -1

# Find largest element
def largest_element(aList):
    """ Identify the largest element in a list. """
    list_len = len(aList)
    if list_len == 1:
        return aList[0]
    return max(largest_element(aList[:math.ceil(list_len / 2)]), largest_element(aList[math.ceil(list_len / 2):]))

# Find index of first appearance of largest element in list
def largest_element_index(aList):
    """ Locate the largest element in a list. """
    largest = largest_element(aList)
    list_len = len(aList)
    for x in range(list_len):
        if aList[x] == largest:
            return x


            

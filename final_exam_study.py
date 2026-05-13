'''
1. Below is a function with several steps. For each numbered comment, fill in the Big-O runtime of that line or block,
then state the overall worst-case runtime of the function.
'''

def analyze_me(lst):
    n = len(lst)                         # 1. O(?)
    result = [0] * n                     # 2. O(?)
    total = 0                            # 3. O(?)
    for i in range(n):                   # 4. outer loop runs ? times
        for j in range(i + 1):          # 5. inner loop runs ? times
            total += lst[j]             # 6. O(?)
        result[i] = total / (i + 1)     # 7. O(?)
    return result                        # 8. O(?)

'''
A. Overall worst-case runtime: ___

B. What does this function actually compute? ___
'''

'''2.
The function below is supposed to use binary search to find a target value in a sorted list and return
its index (or -1 if not found). It runs without crashing but returns wrong answers. Identify the bug and fix it.
'''
def binary_search(lst, target):
    left = 0
    right = len(lst)          # bug is somewhere in here
    while left < right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid
        else:
            right = mid
    return -1

# Test cases — all should return the correct index or -1
print(binary_search([1, 3, 5, 7, 9], 7))   # expected: 3
print(binary_search([1, 3, 5, 7, 9], 1))   # expected: 0
print(binary_search([1, 3, 5, 7, 9], 6))   # expected: -1
print(binary_search([1, 3, 5, 7, 9], 9))   # expected: 4


'''
3. The function below correctly computes whether any two numbers in a list sum to a given target. However, it runs in O(n²).
Rewrite [has_pair_with_sum_fast] so it solves the same problem in O(n). You should not modify [has_pair_with_sum_slow]
HINT: Think about what data structure lets you check membership in O(1).
'''
def has_pair_with_sum_slow(lst, target):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] + lst[j] == target:
                return True
    return False

def has_pair_with_sum_fast(lst, target):
    pass  # your O(n) solution here

# Test cases
lst1 = [1, 4, 7, 2, 9]
lst2 = [1, 2, 3, 4, 5]
lst3 = [5, 5]

print(has_pair_with_sum_fast(lst1, 11))  # True  (2 + 9)
print(has_pair_with_sum_fast(lst2, 10))  # False
print(has_pair_with_sum_fast(lst3, 10))  # True  (5 + 5)
print(has_pair_with_sum_fast([], 5))     # False

# Funktion som är linjär O(n)
# Växer proportionellt med input
for x in lst:
    print(x)

def find_max(lst):
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

def count_occurrences(lst, target):
    count = 0
    for x in lst:
        if x == target:
            count += 1
    return count

def double_list(lst):
    result = []
    for x in lst:
        result.append(x * 2)
    return result

def linear_search(lst, target):
    for x in lst:
        if x == target:
            return True
    return False

# Funktionens tidskomplexitet ökar kvadratiskt O(n²)
# n*n O(n²)

def pairs(lst):
    for x in lst:
        for y in lst:
            print(x, y)

def has_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Dold kvadratisk (vanlig fälla)
#in är O(n)
# n × n

def check(lst):
    for x in lst:
        if x in lst:
            print(x)

# varje insert flyttar element → O(n)
# körs n gånger
# O(n²)
def build(lst):
    result = []
    for x in lst:
        result.insert(0, x)
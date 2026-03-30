# Funktionens tidskomplexitet ökar kvadratiskt O(n²)

import random

def insertion_sort(lst):
    result = []
    for item in lst:    # körs x gånger
        inserted = False
        index = 0
        while not inserted and index < len(result):     # kan gå upp till x gånger
            if item < result[index]:
                result.insert(index, item)
                inserted = True
            index += 1
        if not inserted:
            result.append(item)
    return result

# Använder seed för att få samma tal slumpmässigt för att kunna göra prestanda tester
def generate_list(size):
    random_list = random.Random(42)
    return [random_list.randint(0, 100000) for _ in range(size)]





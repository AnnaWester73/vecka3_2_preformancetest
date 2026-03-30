# Funktionens tidskomplexitet ökar kvadratiskt O(n²)

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






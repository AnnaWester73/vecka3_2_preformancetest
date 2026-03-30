from src.insertion_sort import insertion_sort

# Tom lista
def test_empty_list():
    assert insertion_sort([]) == []

# Ett tal
def test_single_element():
    assert insertion_sort([10]) == [10]

# Osorterad lista
def test_unsorted_list():
    assert insertion_sort([10, 8, 6, 4, 2, 0]) == [0, 2, 4, 6, 8, 10]

# Dubbletter i lista
def test_duplicates():
    assert insertion_sort([10, 8, 6, 4, 4, 2, 0]) == [0, 2, 4, 4, 6, 8, 10]

# Negativa tal i lista
def test_negative_numbers():
    assert insertion_sort([10, 8, 6, -1, 4, 2, 0]) == [-1, 0, 2, 4, 6, 8, 10]

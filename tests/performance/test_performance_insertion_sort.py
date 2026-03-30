import time
from src.insertion_sort import insertion_sort, generate_list

# Test med 3000 median 107ms
def test_insertion_sort_benchmark(benchmark):

    data = generate_list(3000)
    result = benchmark(insertion_sort, data)

    assert result == sorted(data)

def test_insertion_sort_performance():

    sizes = [1000, 2000, 3000, 4000, 5000]

    for size in sizes:
        data = generate_list(size)

        start = time.perf_counter()
        result = insertion_sort(data)
        perf_time = time.perf_counter() - start

        print(f" List size = {size} and time = {perf_time} sek")

        assert result == sorted(data)

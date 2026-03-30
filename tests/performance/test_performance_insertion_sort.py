from src.insertion_sort import insertion_sort, generate_list

# Test med 3000 median 107ms
def test_insertion_sort_benchmark(benchmark):

    data = generate_list(3000)
    result = benchmark(insertion_sort, data)

    assert result == sorted(data)

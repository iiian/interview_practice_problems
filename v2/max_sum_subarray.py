def max_sum_subarray(array):
    best = array[0]
    current = array[0]
    for num in array[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best

if __name__ == '__main__':
    actual = max_sum_subarray([0, -1, -1, -1])
    assert actual == 0, f'{actual}'
    actual = max_sum_subarray([1, 4, -5, 3, 3])
    assert actual == 6, f'{actual}'
    actual = max_sum_subarray([1, 4, -4, 3, 3])
    assert actual == 7, f'{actual}'
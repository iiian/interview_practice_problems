def longest_increasing_subsequence(array):
    lis = [1 for _ in array]

    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i]:
                lis[i] = max(lis[i], 1 + lis[j])

    return max(lis)


from testing import test_case

test_case(
    '(1) it should return the longest subsequence',
    longest_increasing_subsequence([2,4,3,6,1,3,8]),
    4
)

test_case(
    '(2) it should return the longest subsequence',
    longest_increasing_subsequence([3,6,9,1]),
    3
)
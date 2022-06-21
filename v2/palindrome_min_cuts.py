def is_palindrome(string, st, end):
    for i in range(st, (st + end) // 2):
        o = (end - 1) + (st - i)
        if string[i] != string[o]:
            return False
    return True

def palindrome_min_cuts(string):
    cache = {}
    def recurse(string, st, endx):
        k = string[st:endx]
        if k in cache:
            return cache[k]
        if is_palindrome(string, st, endx):
            cache[k] = 0
            return 0

        min_cuts = float('inf')
        for i in range(st+1, endx):
            cuts = 1 + recurse(string, st, i) + recurse(string, i, endx)
            min_cuts = min(cuts, min_cuts)
        cache[k] = min_cuts

        return min_cuts

    return recurse(string, 0, len(string))


if __name__ == "__main__":
    from testing import test_case

    test_case(
        "it should return the min number of cuts required to turn every substring into a palindrome",
        palindrome_min_cuts("aab"),
        1
    )

    test_case(
        "it should return the min number of cuts required to turn every substring into a palindrome",
        palindrome_min_cuts("aa"),
        0
    )

    test_case(
        "it should return the min number of cuts required to turn every substring into a palindrome",
        palindrome_min_cuts("aabbbacdeefaaceeecaafeedcx"),
        3
    )

    test_case(
        "it should return the min number of cuts required to turn every substring into a palindrome",
        palindrome_min_cuts("acdeefaaceeecaafeedc"),
        1
    )
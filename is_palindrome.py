def is_palindrome(test_string, st, count):
    for i in range(st, st + count):
        o = st - 1 - i
        if test_string[i] != test_string[o]:
            return False
    return True

if __name__ == "__main__":
    from testing import test_case

    test_case(
        "it should decide whether the string is a palindrome or not",
        is_palindrome("abba", 0, 4),
        True
    )

    test_case(
        "it should decide whether the string is a palindrome or not",
        is_palindrome("a", 0, 1),
        True
    )

    test_case(
        "it should decide whether the string is a palindrome or not",
        is_palindrome("ab", 0, 2),
        False
    )

    test_case(
        "it should decide whether the string is a palindrome or not",
        is_palindrome("bbbabbb", 0, 7),
        True
    )
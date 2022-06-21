def ways_to_decode(input_string):
    pass

if __name__ == "__main__":
    from testing import test_case
    test_case(
        "It should return the number of ways to decode the input sequence",
        ways_to_decode("12"),
        2
    )
    test_case(
        "It should return the number of ways to decode the input sequence",
        ways_to_decode("127"),
        2
    )
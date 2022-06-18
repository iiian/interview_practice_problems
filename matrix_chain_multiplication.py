def matrix_chain_multiplication(D):
    pass

if __name__ == "__main__":
    from testing import test_case

    test_case(
        "It should return the minimal number of operations required to multiply through",
        matrix_chain_multiplication([40,20,30,10,30]),
        26000
    )
    test_case(
        "It should return the minimal number of operations required to multiply through",
        matrix_chain_multiplication([10,20,30,40,30]),
        30000
    )
    test_case(
        "It should return the minimal number of operations required to multiply through",
        matrix_chain_multiplication([2,3,6]),
        36
    )
    test_case(
        "It should return the minimal number of operations required to multiply through",
        matrix_chain_multiplication([2,3]),
        0
    )
    test_case(
        "It should return the minimal number of operations required to multiply through",
        matrix_chain_multiplication([10,20,30]),
        6000
    )
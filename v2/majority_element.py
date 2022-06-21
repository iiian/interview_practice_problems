from collections import defaultdict

def majority_element(array):
    pass

if __name__ == "__main__":
    from testing import test_case

    test_case(
        "It should return the majority element",
        majority_element([2,2,2,2,2,3]),
        2
    )
    test_case(
        "It should return the majority element",
        majority_element([2,3,2,2,2,3,3,3,3]),
        3
    )
    test_case(
        "It should return the majority element",
        majority_element([2,3,3,2,2,2,2,3,3,3,3]),
        3
    )
    test_case(
        "It should return the majority element",
        majority_element([2,3,2,2,1,1,1,1,1,1,1,2,3,3,3,3]),
        1
    )
    test_case(
        "It should return the majority element",
        majority_element([1,0,1,0,1,0,1,0,1]),
        1
    )
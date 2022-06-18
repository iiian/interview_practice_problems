def quick_sort(array):
    pass

from testing import test_case, TestSuite
from random import shuffle

suite = TestSuite()
for i in range(0, 1000):
    def create_test(i):
        def test():
            array = list(range(i))
            input = array.copy()
            shuffle(input)
            return test_case(
                f"it should sort the array ({i+1})",
                quick_sort(input),
                array
            )
        return test
    suite.add_test(create_test(i))

suite.run_all()
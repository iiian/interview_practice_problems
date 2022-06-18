def test_case(description, actual, expectation):
    print(description)
    if actual != expectation:
        print(f'❌ failed, expected {expectation}, but got {actual}')
        return False
    else:
        print(f'✔ passed')
        return True

class TestSuite:
    def __init__(self):
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def run_all(self):
        pass_count = 0
        for test in self.tests:
            if test():
                pass_count += 1
        print(f'{pass_count}/{len(self.tests)} tests passed')
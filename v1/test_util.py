class Deferred:
  def __init__(self, process, *input):
    self.process = process
    self.input = input

  def evaluate(self):
    return self.process(*self.input)

  def __str__(self):
    return f'{self.process.__name__}({", ".join(map(str, [*self.input]))})'

def test(expectation, test_expression):
  print("TEST:")
  result = test_expression.evaluate()
  if expectation != result:
    print(f"\tfailed! expected {str(test_expression)} == {str(expectation)},\n\tbut was {result}")
    return False
  print(f"\tpassed! {str(test_expression)} == {str(expectation)}")
  return True

def assert_lt(left, right):
  if left > right:
    print(f"\tfailed! expected {str(left)} <= {str(right)}")
    return False
  return True

def passed(message):
  print(f"\tpassed! {message}")

def test_are_eq(expression_a, expression_b):
  print("TEST:")
  result_a = expression_a.evaluate()
  result_b = expression_b.evaluate()
  if result_a != result_b:
    print(f"\tfailed! expected {str(expression_b)} == {str(expression_a)},\n\tbut was {result_a} != {result_b}")
    return False
  print(f"\tpassed! {str(expression_b)} == {str(expression_a)} == {result_a}")
  return True

def test_suite(*tests):
  if all(tests):
    print("All tests passed.")
    return
  for index, result in enumerate(tests):
    if not result:
      print(f"Test #{index+1} failed")
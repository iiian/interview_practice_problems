from test_util import *

# how far it is from the character to it's corresponding bracket
ord_off = {
  ']': 2,
  '}': 2,
  ')': 1
}

def are_brackets_balanced(test_string):
  stk = []
  for i in range(len(test_string)):
    ch = test_string[i]
    if ch == '(' or ch == '[' or ch == '{':
      stk.append(ch)

    elif ch == ']' or ch == '}' or ch == ')':
      if len(stk) > 0 and ord(stk[len(stk) - 1]) + ord_off[ch] == ord(ch):
        stk.pop()
      else: return False

  return len(stk) == 0

test(
  True,
  Deferred(are_brackets_balanced, "[](){}")
)
test(
  False,
  Deferred(are_brackets_balanced, "](){}")
)
test(
  True,
  Deferred(are_brackets_balanced, "{()}[{}]([]){[]()}")
)
test(
  True,
  Deferred(are_brackets_balanced, "[([{}]{})[{[]}[()[]]{([]){([{}])}}]({()})]")
)
test(
  False,
  Deferred(are_brackets_balanced, "[([{}]{})[{[]}[()[]{([]){([{}])}}]({()})]")
)
test(
  False,
  Deferred(are_brackets_balanced, "((((((")
)
test(
  False,
  Deferred(are_brackets_balanced, "{}()[)")
)
test(
  True,
  Deferred(are_brackets_balanced, "foo(bar(baz([2,3,4]), { if null: return [] } //))")
)
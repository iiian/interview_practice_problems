from test_util import Deferred, test

def are_parens_balanced(test_string):
  balance = 0
  for i in range(len(test_string)):
    if test_string[i] == '(':
      balance += 1
    elif test_string[i] == ')':
      balance -= 1
      if balance < 0:
        return False
  return balance < 1

test(
  False,
  Deferred(are_parens_balanced, "()())")
)
test(
  True,
  Deferred(are_parens_balanced, "()()")
)
test(
  True,
  Deferred(are_parens_balanced, "(()((((())()))()()((()))))")
)
test(
  False,
  Deferred(are_parens_balanced, ")((()))")
)
test(
  True,
  Deferred(are_parens_balanced, "(((((())()())()()(((()))))())())")
)
test(
  True,
  Deferred(are_parens_balanced, "(ok(skip(test(th(i(s)i)s(a)j(our)ne)y(in)t(o)s(o(u(n(d)l)o)l)o)m(g)k)i(ll)me)!")
)
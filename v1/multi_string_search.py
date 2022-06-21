from test_util import *

# Given a search needles (string[]) and a haystack (string[]),
# return a mapping of string to whether the haystack contained it or not.
def multi_string_search(needles, haystack):
  def build_trie(haystack):
    trie = {}
    for string in haystack:
      cursor = trie
      for char in string:
        if char not in cursor:
          cursor[char] = {}  
        cursor = cursor[char]
      cursor['*'] = True
    return trie

  trie = build_trie(haystack)
  results = []
  for string in needles:
    ci = 0
    cursor = trie
    while ci < len(string):
      if string[ci] in cursor:
        cursor = cursor[string[ci]]
        ci += 1
      else: break
    results.append('*' in cursor and ci == len(string))
  return results
    
test(
  [True, True, False, False],
  Deferred(multi_string_search, ['truth', 'truthful', 'weak', 'fettid'], ['truth', 'truthful'])
)


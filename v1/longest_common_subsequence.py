
def longest_common_subsequence(str1, str2):
  M = [ [0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
  for i in range(1, len(str2)+1):
    c2 = str2[i-1]
    for j in range(1, len(str1)+1):
      c1 = str1[j-1]
      M[i][j] = max(
        M[i-1][j-1] + 1 if c2 == c1 else 0,
        M[i-1][j],
        M[i][j-1]
      )

  return M[i][j]
    
result = longest_common_subsequence('application', 'constellation')
print(result)
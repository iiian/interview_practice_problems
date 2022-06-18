def count_matching_subsequence(haystack, needle):
    N = len(needle)
    H = len(haystack)
    if H < N:
        return 0
    if H == N:
        return 1 if needle == haystack else 0
    cache = {}
    ncache = {}
    def recurse(h_start, n):
        if (h_start, n) in cache:
            return cache[h_start, n]
        if n == N:
            cache[h_start, n] = 1
            ncache[haystack[h_start:], needle[n:]] = 1
            return 1
        ways = 0
        for h in range(h_start, H):
            hc, nc = haystack[h], needle[n]
            if hc == nc:
                ways += recurse(h+1, n+1)
        ncache[haystack[h_start:], needle[n:]] = ways
        cache[h_start, n] = ways
        return ways
    return recurse(0, 0)

if __name__ == '__main__':
    assert count_matching_subsequence('rabbbit','rabbit') == 3, f"rabbbit test was {count_matching_subsequence('rabbbit','rabbit')}"

    assert count_matching_subsequence('nheaeeydsllteeack','needle') == 12, f"nheaeydslteack test was {count_matching_subsequence('nheaeydslteack','needle')}"
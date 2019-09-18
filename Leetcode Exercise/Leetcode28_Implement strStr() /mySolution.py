class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n, m = len(haystack), len(needle)
        for i in range(0, (n - m + 1)):
            if haystack[i: i+m] == needle:
                return i
        return -1
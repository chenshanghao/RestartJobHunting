class Solution:
    def checkPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        dict_char_count = {}
        for char in s1:
            if char in dict_char_count:
                dict_char_count[char] += 1
            else:
                dict_char_count[char] = 1
        for char in s2:
            if char in dict_char_count and dict_char_count[char] > 0:
                dict_char_count[char] -= 1
        return False
class Solution:
    def is_substring(self, string, sub):
        return string.find(sub) != -1

    def string_rotation(self, s1, s2):
        if len(s1) == len(s2) and len(s1) != 0:
            return self.is_substring(s1 + s1, s2)
        return False
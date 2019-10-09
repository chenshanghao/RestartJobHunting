class Solution:
    def unique(self, string):
        if len(string) > 128:
            return False
        char_set = [False for _ in range(128)]
        for char in string:
            ascii_val = ord(char)
            if char_set[ascii_val]:
                return False
            # Char already found in string
            char_set[ascii_val] = True
        return True


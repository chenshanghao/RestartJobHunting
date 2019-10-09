class Solution:
    def checkPermutation(self, s1: str, length: int) -> str:
        '''function replaces single spaces with %20 and removes trailing spaces'''
        new_index = len(s1)

        for i in reversed(range(length)):
            if s1[i] == ' ':
                # Replace spaces
                s1[new_index - 3: new_index] = '%20'
                new_index -= 3
            else:
                # Move characteres
                s1[new_index - 1] = s1[i]
                new_index -= 1
        return s1
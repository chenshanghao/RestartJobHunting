class Solution:
    def one_away(self, s1, s2):
        '''Check if a string can converted to another string with a single edit'''
        if len(s1) == len(s2):
            return self.one_edit_replace(s1, s2)
        elif len(s1) + 1 == len(s2):
            return self.one_edit_replace(s1, s2)
        elif len(s1) - 1 == len(s2):
            return self.one_edit_replace(s2, s1)

    def one_edit_replace(s1, s2):
        edited = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if edited:
                    return False
                return True
        return True

    def one_edit_insert(s1, s2):
        edited = False
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if edited:
                    return False
                edited = True
                j += 1
            else:
                i += 1
                j += 1
        return True

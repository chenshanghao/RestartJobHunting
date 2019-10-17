class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or k == 0:
            return 0
        dict_word_index = {}
        start_index = 0
        res = 1
        dict_word_index[s[start_index]] = 1
        
        for i in range(1, len(s)):
            if s[i] in dict_word_index:
                dict_word_index[s[i]] += 1
            else:
                dict_word_index[s[i]] = 1
                if len(dict_word_index) > k:
                    poiter = start_index
                    while len(dict_word_index) > k:
                        dict_word_index[s[poiter]] -= 1
                        if dict_word_index[s[poiter]] == 0:
                            del dict_word_index[s[poiter]]
                        poiter += 1
                    start_index = poiter
            res = max(res, i - start_index + 1)
        return res
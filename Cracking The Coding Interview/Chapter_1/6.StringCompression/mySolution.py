class Solution:
    def string_compression(self, s1):
        compressed = []
        counter = 0

        for i in range(len(s1)):
            if i != 0 and s1[i] != s[i - 1]:
                compressed.append(s[i - 1] + str(counter))
                counter = 0
            counter += 1

        # add last repeated character
        compressed.append(s[-1] + str(counter))

        # returns original string if compressed string isn't smaller
        return min(string, ''.join(compressed), key=len)



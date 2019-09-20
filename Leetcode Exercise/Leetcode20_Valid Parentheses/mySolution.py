class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            tmp = s[i]
            if tmp == '(' or tmp == '[' or tmp == '{':
                stack.append(tmp)
                continue
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and tmp != ')') or (top == '[' and tmp != ']') or (top == '{' and tmp != '}'):
                return False
        
        if stack:
            return False
        return True
        
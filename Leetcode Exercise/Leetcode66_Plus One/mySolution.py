class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        index = n - 1
        carry = 1
        while (carry and index >= 0):
            lastCarry = carry
            carry = (digits[index] + lastCarry) // 10
            digits[index] = (digits[index] + lastCarry) % 10
            index -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits
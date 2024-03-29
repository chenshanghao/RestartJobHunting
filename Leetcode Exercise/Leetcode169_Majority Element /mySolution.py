class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, candidate = 0, 0
        for num in nums:
            if num == candidate:
                cnt += 1
            elif cnt == 0:
                candidate = num
                cnt = 1
            else:
                cnt -= 1
        return candidate
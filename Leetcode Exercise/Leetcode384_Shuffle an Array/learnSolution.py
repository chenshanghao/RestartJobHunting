import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = self.nums[:]                      # copy list
        for i in range(len(res) - 1, -1, -1):   # start from end
            j = random.randrange(0, i + 1)      # generate random index
            res[i], res[j] = res[j], res[i]     # swap
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
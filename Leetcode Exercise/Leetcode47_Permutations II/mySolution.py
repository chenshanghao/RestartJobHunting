class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if n == 0:
            return res
        visited = [False] * n
        self.backtracking(sorted(nums), res, visited, [])
        return res
    
    def backtracking(self, nums, res, visited, tmp):
        if len(tmp) == len(nums):
            res.append(tmp[:])
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            tmp.append(nums[i])
            visited[i] = True
            self.backtracking(nums, res, visited, tmp)
            tmp.pop()
            visited[i] = False
            
        
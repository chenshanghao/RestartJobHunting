class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictNumCount = dict()
        res = []
        for num in nums1:
            if num in dictNumCount:
                dictNumCount[num] += 1
            else:
                dictNumCount[num] = 1
        for num in nums2:
            if num in dictNumCount:
                res.append(num)
                dictNumCount[num] -= 1
                if dictNumCount[num] == 0:
                    del dictNumCount[num]
        return res

# Q1. What if the given array is already sorted? How would you optimize your algorithm?
# -- Use two pointers. At start two pointers point to the first element of each array. 
# If it is equal, push it to the answer then move both pointers to next position. Otherwise, move the one with less value to the next position.

# Q2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
# Probably two pointers is better? Consider len(nums1) = m, len(nums2) = n, (m > n). 
# Although time complexity for both methods are O(m + n), space complexity for hash method is O(n), two pointer space complexity is O(1). 
# Also, two pointer method can avoid some edge cases when lists are sorted
# (ex: nums1 = [1,4], nums2 = [1,2,....,100], we just iterate through nums1 
#     and while loop ended before we reach the end of nums2, whereas in hash method, we need to iterate both lists).

# Q3. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
# Divide and conquer. Repeat the process frequently: Slice nums2 to fit into memory, process (calculate intersections), and write partial results to memory.





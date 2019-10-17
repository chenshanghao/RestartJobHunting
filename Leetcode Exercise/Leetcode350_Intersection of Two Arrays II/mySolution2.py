class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dict_num_count = {}
        for num in nums1:
            dict_num_count[num] = dict_num_count.get(num, 0) + 1
        for num in nums2:
            if num in dict_num_count:
                res.append(num)
                dict_num_count[num] -= 1
                if dict_num_count[num] == 0:
                    del dict_num_count[num]
        return res
        
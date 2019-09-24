class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals = sorted(intervals)
        res = [intervals[0]]
        intervals = intervals[1:]
        for interval in intervals:
            if interval[0] <= res[-1][1]:
                if interval[1] <= res[-1][1]:
                    continue
                else:
                    res[-1][1] = interval[1]
            else:
                res.append(interval)
        return res
        
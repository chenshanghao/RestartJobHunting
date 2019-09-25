"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0
        tmp = []
        for interval in intervals:
            tmp.append([interval.start, 1])
            tmp.append([interval.end, -1])
        tmp = sorted(tmp, key = lambda t: t[0])
        maxNum, n = 0, 0
        for timestamp in tmp:
            n += timestamp[1]
            maxNum = max(maxNum, n)
        return maxNum

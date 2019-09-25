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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals:
            return True
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start = sorted(start)
        end = sorted(end)
        n = len(intervals)
        for i in range(n-1):
            if end[i] > start[i+1]:
                return False
        return True
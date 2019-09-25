class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dictTaskCount = dict()
        maxCount = 0
        for task in tasks:
            if task in dictTaskCount:
                dictTaskCount[task] += 1
            else:
                dictTaskCount[task] = 1
            maxCount = max(maxCount, dictTaskCount[task])
        res = (maxCount - 1) * (n + 1)
        for task, count in dictTaskCount.items():
            if count == maxCount:
                res += 1
        return max(res,len(tasks))
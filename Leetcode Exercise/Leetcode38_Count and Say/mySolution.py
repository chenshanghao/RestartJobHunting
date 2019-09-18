class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(1, n):
            tmp = res[0]
            count = 1
            newRes = ''
            for j in range(1, len(res)):
                if res[j] == tmp:
                    count += 1
                else:
                    newRes = newRes + str(count) + str(tmp)
                    tmp = res[j]
                    count = 1
            res = newRes + str(count) + str(tmp)
        return res
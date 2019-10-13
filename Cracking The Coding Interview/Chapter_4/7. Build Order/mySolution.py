import collections

class Solution:
    def buildOrder(self, num: int, prerequisites: List[List[int]]) -> List[int]:
        int_degree = [0] * num
        out_list = [[] for _ in range(num)]
        res_list = []
        
        for p in prerequisites:
            int_degree[p[0]] += 1
            out_list[p[1]].append(p[0])
        
        queue = collections.deque()
        for i in range(num):
            if int_degree[i] == 0:
                queue.append(i)
                
        while queue:
            x = queue.popleft()
            res_list.append(x)
            for i in out_list[x]:
                int_degree[i] -= 1
                if int_degree[i] == 0:
                    queue.append(i)
        if len(res_list) == num:
            return res_list
        else:
            return []
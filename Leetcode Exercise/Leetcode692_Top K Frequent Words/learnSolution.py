import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dictWordCount = dict()
        for word in words:
            if word in dictWordCount:
                dictWordCount[word] += 1
            else:
                dictWordCount[word] = 1
        minHeap = [(-count, word) for word, count in  dictWordCount.items()]
        heapq.heapify(minHeap)
        return [heapq.heappop(minHeap)[1] for _ in range(k) ]
        
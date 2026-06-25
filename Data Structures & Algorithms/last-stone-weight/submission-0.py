class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 == s2:
                continue
            else:
                s1 -= s2
                heapq.heappush(stones, s1)
        if len(stones) == 1:
            return -stones[0] 
        else:
            return 0
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        ret = None
        for i in range(k):
            ret = heapq.heappop(nums)
        return -ret
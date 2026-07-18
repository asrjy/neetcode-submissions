class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        for i, num in enumerate(nums):
            nums_hash[num] = i
        for i, num in enumerate(nums):
            req = target - num
            if req in nums_hash.keys() and nums_hash[req] != i:
                return [min(i, nums_hash[req]), max(i, nums_hash[req])]
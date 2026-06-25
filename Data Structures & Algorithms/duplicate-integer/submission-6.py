class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flags = {}
        for num in nums:
            if flags.get(num, 0) == 1:
                return True
            flags[num] = 1
        return False
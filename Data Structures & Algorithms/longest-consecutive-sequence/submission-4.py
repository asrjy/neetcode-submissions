class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in nums:
            if (i-1) not in numSet:
                length = 1
                while (i + 1) in numSet:
                    length += 1
                    i += 1
                longest = max(length, longest)

        return longest
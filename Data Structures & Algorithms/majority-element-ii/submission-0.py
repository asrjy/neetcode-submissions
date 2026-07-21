class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        resultSet = set()
        counter = 0
        n = len(nums)
        i, j = nums[0], nums[0]
        for p in range(n):
            j = nums[p]
            if i == j:
                counter += 1
            else:
                i = nums[p]
                counter = 1
            if counter > n/3:
                resultSet.add(i)
        return list(resultSet)
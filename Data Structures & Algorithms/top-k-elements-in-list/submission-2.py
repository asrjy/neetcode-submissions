class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # countList = [[]] * (len(nums) + 1)
        countList = [[] for i in range(len(nums) + 1)]
        countDict = {}

        for num in nums:
            countDict[num] = 1 + countDict.get(num, 0)
        
        for num, count in countDict.items():
            countList[count].append(num)
        
        topK = []
        for i in range(len(countList) - 1, 0, -1):
            for num in countList[i]:
                topK.append(num)
                if len(topK) == k:
                    return topK

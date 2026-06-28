class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            if hm.get(n, 0) != 0:
                hm[n] += 1
            else:
                hm[n] = 1
        counts = sorted(list(hm.values()))[::-1]
        counts_k = counts[:k]
        res = []
        for k,v in hm.items():
            if v in counts_k:
                res.append(k)
        return res
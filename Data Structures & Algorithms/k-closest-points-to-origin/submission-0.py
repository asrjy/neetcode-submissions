class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists, ret = [], []
        for point in points:
            dist = (point[0]**2 + point[1]**2)**0.5
            dists.append([dist, point])
        heapq.heapify(dists)
        for i in range(k):
            ret.append(heapq.heappop(dists)[1])
        return ret
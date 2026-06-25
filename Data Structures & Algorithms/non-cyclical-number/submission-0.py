class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        visited.append(sum([int(i)**2 for i in str(n)]))
        n = visited[0]
        if n == 1:
            return True
        while True:
            temp = sum([int(i)**2 for i in str(n)])
            if temp in visited:
                return False
            elif temp == 1:
                return True
            else:
                visited.append(temp)
                n = temp
        
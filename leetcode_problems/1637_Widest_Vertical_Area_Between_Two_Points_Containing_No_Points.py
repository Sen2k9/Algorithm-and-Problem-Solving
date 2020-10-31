class Solution:
    def maxWidthOfVerticalArea(self, points) -> int:
        x_points = set()
        for x, y in points:
            x_points.add(x)
        ans = 0
        x_points = sorted(list(x_points))
        #print(x_points)

        for i in range(len(x_points)-1):
            ans = max(ans, x_points[i+1] - x_points[i])

        return ans

sol = Solution()
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(sol.maxWidthOfVerticalArea(points))

points = [[8,7],[9,9],[7,4],[9,7]]
print(sol.maxWidthOfVerticalArea(points))
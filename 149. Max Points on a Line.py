from collections import Counter
class Solution:
    def get_max_cnt(self, x):
        cnts = Counter(x)
        ans = [vals for (key,vals) in cnts.items()]
        return max(ans)
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
    
    # storing all of the between every pair of points in a list #
        slopes = []; np = len(points)
    
        for i in range(np):
            slopes_i = []
            for j in range(np):
                if points[i][0] != points[j][0]:
                    slopes_i.append( (points[i][1] - points[j][1])/(points[i][0] - points[j][0]) )
                if points[i][0] == points[j][0] and i!=j:
                    slopes_i.append('vert_'+str(points[i][0]))

            slopes.append(slopes_i)
    
        cnts = [self.get_max_cnt(x) for x in slopes]
        return max(cnts)+1

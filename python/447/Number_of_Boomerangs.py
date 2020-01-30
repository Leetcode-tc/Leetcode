class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # TypeError: unhashable type: 'list'  --> tuple(x)

        d = {tuple(x):collections.defaultdict(int) for x in points}
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                x, y = points[i], points[j]
                dis = (x[0]-y[0])**2 + (x[1]-y[1])**2
                d[(tuple(x))][dis] += 1

        cnt = 0
        for v in d.values():
            for vv in v.values():
                cnt += vv*(vv-1)
        return cnt


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # TypeError: unhashable type: 'list'  --> tuple(x)

        d = {tuple(x):collections.defaultdict(int) for x in points}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x, y = points[i], points[j]
                dis = (x[0]-y[0])**2 + (x[1]-y[1])**2
                d[tuple(x)][dis] += 1
                d[tuple(y)][dis] += 1
        cnt = 0
        for v in d.values():
            for vv in v.values():
                cnt += vv*(vv-1)
        return cnt
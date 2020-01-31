class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        s = set([0])
        q = [0]
        while q:
            cur = q.pop(0)
            for x in rooms[cur]:
                if x not in s:
                    s.add(x)
                    q.append(x)
        return len(s) == len(rooms)

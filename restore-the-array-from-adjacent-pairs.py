class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        ind = defaultdict(int)
        for start , end in adjacentPairs:
            d[start].append(end)
            d[end].append(start)
            ind[start] += 1
            ind[end] += 1
        
        q = deque()
        res =[]
        for key in ind:
            if ind[key] == 1:
                q.append(key)
        finale = q.pop()
        while q :
            cur = q.pop()
            res.append(cur)

            for neg in d[cur]:
                ind[neg] -= 1

                if ind[neg] == 1:
                    q.appendleft(neg)
        
        return res + [finale]
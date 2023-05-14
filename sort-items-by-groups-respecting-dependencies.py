class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        start = m + 1
        all_groups = set()
        all_in_group = defaultdict(set)
        for idx , g in enumerate(group):
            if g == -1:
                group[idx] = start 
                start += 1
            all_groups.add(group[idx])
            all_in_group[group[idx]].add(idx)
        
        group_level = defaultdict(list)
        in_group = {}

        for idx , tup in enumerate(beforeItems):

            after = group[idx] 

            for b in tup:

                before = group[b]

                if before != after:

                    group_level[before].append(after)
                
                else:

                    if after not in in_group:

                        in_group[after] = defaultdict(set)
                    
                    ing = in_group[after]

                    ing[b].add(idx)
        
        def top(_all , graph):

            indegree= defaultdict(int)

            for key in graph:
                for end in graph[key]:
                    indegree[end] += 1
            
            q = deque()

            for key in _all:
                if indegree[key] == 0:
                    q.append(key)
            
            res = []

            while q :

                cur = q.pop()
                res.append(cur)

                for neg in graph[cur]:

                    indegree[neg] -= 1

                    if indegree[neg] == 0:
                        q.appendleft(neg)
            
            # print(res , _all)
            if len(res) != len(_all):
                return []

            return res
        
        group_order = top(all_groups , group_level)

        if not group_order:
            return []
        
        finale = []
        for g in group_order:
            if g not in in_group:
                in_group[g] = defaultdict(list)
            in_order = top(all_in_group[g] , in_group[g])
            if not in_order:
                return []
            
            finale += in_order

        
        return finale
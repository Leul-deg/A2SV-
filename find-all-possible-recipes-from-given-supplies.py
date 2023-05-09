class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        d = defaultdict(int)
        graph  = defaultdict(list)
        for idx in range(len(recipes)):
            recipe = recipes[idx]
            ing = ingredients[idx]
            d[recipe] = len(ing)
            for f in ing:
                graph[f].append(recipe)
        q = deque(supplies)
        res = []
        seen = set()
        while q :

            cur = q.pop()

            for neg in graph[cur]:
                d[neg] -= 1
                if d[neg] == 0:
                    q.appendleft(neg)
                    seen.add(neg)
        # print(d, "ddddd")
        for key in d:
            if d[key] <= 0:
                res.append(key)
        
        return res
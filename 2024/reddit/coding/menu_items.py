class Solution:
    def findAllPossibleItemsExactMatch(self, items_map, budget):
        items = sorted(items_map.items(), key=lambda x: -x[1])
        def backtrack(items, budget, memo):
            result = []
            if budget == 0:
                return [[]]
            if (len(items), budget) in memo:
                return memo[(len(items), budget)]
            for i, item in enumerate(items):
                if budget < item[1]:
                    return result
                res = backtrack(items[i:], budget-item[1], memo)
                result += [[item[0]] + sol for sol in res]

            memo[(len(items), budget)] = result
            return result
        memo = {}
        return backtrack(items, budget, memo)

    def findAllPossibleItemsCombos(self, items_map, budget):
        items = sorted(items_map.items(), key=lambda x: -x[1])
        def backtrack(items, budget, memo):
            if (len(items), budget) in memo:
                return memo[(len(items), budget)]
            result = set()
            for i, item in enumerate(items):
                if budget < item[1]:
                    break
                res = backtrack(items[i:], budget-item[1], memo)
                result |= res
                result |= set([(item[0], ) + tuple(sol) for sol in res])
            
            if len(result) == 0:
                return set([()])

            memo[(len(items), budget)] = result
            return result
        memo = {}
        return backtrack(items, budget, memo)





sol = Solution()
res = sol.findAllPossibleItemsCombos({'Popcorn': 10, 'CocaCola': 4, 'Water': 2, 'Coffeeee': 3}, 10)
print(sorted(res))
res = sol.findAllPossibleItemsExactMatch({'Popcorn': 10, 'CocaCola': 4, 'Water': 2, 'Coffeeee': 3}, 10)
print(sorted(res))

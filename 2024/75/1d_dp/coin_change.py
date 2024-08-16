class Solution:
    def coinChange(self, coins, amount):
        def searchWithCache(coins, amount, cache):
            if amount in cache:
                return cache[amount]

            if amount == 0:
                cache[amount] = 0
                return cache[amount]

            if amount < 0:
                cache[amount] = math.inf
                return cache[amount]
            
            min_coins = math.inf
            for coin in coins:
                ret_coins = searchWithCache(coins, amount-coin, cache)
                min_coins = min(min_coins, ret_coins)

            cache[amount] = min_coins

            return min_coins

        cache = {}
        searchWithCache(coins, amount, cache)
        n = cache[amount]
        if n == math.inf:
            return -1
        return n

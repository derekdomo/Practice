def expression_operators(nums, target):
    res = []
    def dfs(i, path, cur_sum, pre_sum):
        if i == len(nums):
            if cur_sum == target:
                res.append(path)
            return
        n = 0
        for j in range(i, len(nums)):
            n = n * 10 + nums[j]
            if j > i and nums[i] == 0:
                break
            if j == 0:
                dfs(j+1, path+str(n), n + cur_sum, n)
            else:
                dfs(j+1, path+"+"+str(n), cur_sum + n, n)
                dfs(j+1, path+"-"+str(n), cur_sum - n, -n)
                dfs(j+1, path+"*"+str(n), cur_sum - pre_sum + pre_sum * n, pre_sum * n)

    dfs(0, "", 0, 0)
    return res

print(expression_operators([1,2,3], 6))
print(expression_operators([2,3,2], 8))
print(expression_operators([3,4,5,6,2,3,7,4,9,0], 9191))


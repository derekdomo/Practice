class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        exclusive_time = [0 for i in xrange(n)]
        stack = []
        for log in logs:
            info = log.split(":")
            cur_id = int(info[0])
            cur_t = int(info[2])
            cur_start = info[1] == 'start'
            if len(stack) == 0:
                stack.append([cur_id, cur_t, 0])
            else:
                if cur_start:
                    last_func = stack.pop()
                    last_func[2] += cur_t - last_func[1]
                    stack.append(last_func)
                    stack.append([cur_id, cur_t, 0])
                else:
                    last_func = stack.pop()
                    exclusive_time[last_func[0]] += last_func[2] + cur_t - last_func[1] + 1
                    if len(stack) != 0:
                        last_func = stack[-1]
                        last_func[1] = cur_t + 1

        return exclusive_time

sol = Solution()

print sol.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"])

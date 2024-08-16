'''
mod_given_new_access, action, mod_had_access, timestamp
每个level都需要写三个function：
1) mod_list constructor
2) can_remove_mod
3) get_mod_list
第二个level加了一个community的概念，同样需要写出三个function
第三个level需要demote 当前的mod，也就是当前mod得到access的时间往下调
'''

from collections import defaultdict

class ModertorController:
    
    def __init__(self):
        from collections import defaultdict
        self.mods = set()
        self.graph = defaultdict(set)
        self.inverted_graph = defaultdict()
        self.mod_pri = defaultdict()

    def _check_if_allowed(self, p, c):
        #if p == inverted_graph[c]:
        #    return True
        #return _check_if_allowed(p, inverted_graph[c])
        for pc in self.graph[p]:
            if pc == c:
                return True
            elif _check_if_allowed(self, pc, c):
                return True
        return False
    
    def get_mod_list(self):
        return list(self.mods)

    
    def process_log(self, log):
        p = log[2]
        c = log[0]
        action = log[1]
        if p not in existing_mod:
            self.exiting_mod.append(p)
        else:
            return False
        if action == 'add':
            if c in existing_mod:
                return False
            self.graph[p].add(c)
            self.inverted_graph[c] = p
            self.mod_pri[c] = ts
        else:
            if _check_if_allowed(p, c):
                self.existing_mod.remove(c)
                del self.mod_pri[c]
                for cc in self.mod_graph[c]:
                    self.graph[p].add(cc)
                    self.inverted_graph[cc] = p
                self.graph[p].remove(c)
                del inverted_graph[c]

            else:
                return False
        return True


class Solution:
    def directReport(self, teams):
        persons = set()
        has_managers = set()
        from collections import defaultdict
        direct_report = defaultdict(list)
        for team in teams:
            direct_report[team[0]] = team[1:]
            persons.add(team[0])
            for member in team[1:]:
                has_managers.add(member)   
                persons.add(member)
        
        no_managers = []
        for manager in direct_report:
            if manager not in has_managers:
                no_managers.append(manager)

        def dfs(direct_reports, manager, level):
            print(level * 3 * '.', manager)
            for report in direct_reports[manager]:
                dfs(direct_reports, report, level+1)

        def backtrackSkipReport(direct_reports, manager, skipLevel):
            if skipLevel == 0:
                return [[manager]]
            result = []
            for report in direct_reports[manager]:
                skips = backtrackSkipReport(direct_reports, report, skipLevel-1)
                result += skips
            return result
        
        #for manager in no_managers:
        #    dfs(direct_report, manager, 0)
        result = []
        for person in list(persons):
            cur = backtrackSkipReport(direct_report, person, 2)
            result += [[person] + skip for skip in cur]
        print(result)



sol = Solution()
sol.directReport([['a', 'b', 'c'], ['b', 'd'], ['d', 'e']])


def merge_accounts(accounts):
    # build graph
    # 1. owner -> emails
    # 2. email -> owner
    parents = {}
    emails = {}
    for ind, raw_list in enumerate(accounts):
        name = raw_list[0]
        for email in raw_list[1:]:
            parents[email] = ind
            emails[ind] = emails.get(ind, []) + [email]
    final_list = {}
    visited = {}
    for owner in emails:
        if owner in visited:
            continue
        final_list[owner] = {}
        dfs_visit(owner, owner, parents, visited, final_list, emails)
    res = []
    for owner in final_list:
        res.append([accounts[owner][0]] + sorted(final_list[owner].keys()))

    return res

def dfs_visit(owner, actual_owner, parents, visited, final_list, emails):
    visited[owner] = True
    for email in emails[owner]:
        final_list[actual_owner][email] = True
        alter_owner = parents[email]
        if alter_owner in visited:
            continue
        dfs_visit(alter_owner, actual_owner, parents, visited, final_list, emails)

print merge_accounts([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])



# dfs排列组合
def dfs(strs, used, path, all):
    if len(used) == len(strs):
        all.append(path)
    else:
        for i, str in enumerate(strs):
            if i not in used:
                used.add(i)
                dfs(strs, used, path+str, all)
                used.remove(i)

def permutation(strs):
    used = set()
    path = ""
    all = []
    dfs(strs, used, path, all)
    return all


print(permutation(["a","b","c"]))

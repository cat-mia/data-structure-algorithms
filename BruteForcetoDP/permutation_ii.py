ans = []

# permutation deduplicate
def process(s, path, index):
    if index == len(s):
        ans.append(path)
        return
    visited = [0]*26
    for j in range(index, len(s)):
        # j位置的字符可以来到i位置
        if visited[ord(s[j]) - ord('a')] == 0:
            visited[ord(s[j]) - ord('a')] = 1
            s[j], s[index] = s[index], s[j]
            process(s, path+s[index], index+1)
            s[index], s[j] = s[j], s[index]


process(['a','b','a'], "", 0)
print(ans)
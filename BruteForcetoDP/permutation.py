ans = []

def process(s, path, index):
    if index == len(s):
        ans.append(path)
        return
    for j in range(index, len(s)):
        s[j], s[index] = s[index], s[j]
        process(s, path+s[index], index+1)
        s[index], s[j] = s[j], s[index]


process(['a','b', 'c'], "", 0)
print(ans)
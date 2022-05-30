ans = []

# index之后所有字符都可以来到index位置
# index之前是固定的
def process(s, path, index):
    if index == len(s):
        ans.append(path)
        return
    for j in range(index, len(s)):
        # j位置的字符可以来到i位置
        s[j], s[index] = s[index], s[j]
        process(s, path+s[index], index+1)
        s[index], s[j] = s[j], s[index]


process(['a','b', 'c'], "", 0)
print(ans)
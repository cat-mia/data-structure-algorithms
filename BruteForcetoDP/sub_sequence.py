# 子串和子序列的区别
# 子串一定是原字符串的截取
# 子序列不一定是截取，是原字符串按顺序选取特定元素

ans = []

def process(s, path, index):
    if index == len(s):
        ans.append(path)
        return
    process(s, path, index+1)
    process(s, path+s[index], index+1)

process("abcd", "", 0)
print(ans)

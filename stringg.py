s = "dog cat cat dog"
for i in range(len(s)):
    stack = []
    if s[i] == " ":
        stack.append(s[:i+1])
print(stack)
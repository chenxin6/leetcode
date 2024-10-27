import sys


def is_merged_string(s):
    if s[0] != '<' or s[len(s) - 1] != '>':
        return False
    stack = []
    for char in s:
        if char == '<':
            stack.append(char)
        elif char == '>':
            if not stack:
                return False
            stack.pop()
    return not stack


input_str = "<te></te><st></st>"
for line in sys.stdin:
    a = line.split()
    input_str = a[0]


print("YES" if is_merged_string(input_str) else "NO")

for _ in range(int(input())):
    brackets, stack = input().split(), []
    balanced = True
    for i in brackets:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        else:
            if stack:
                top = stack.pop()
            else:
                balanced = False
                break
            if (top == "(" and i != ")") or (top == "[" and i != "]") or (top == "{" and i != "}"):
                balanced = False
                break
    if stack:
        print("NO")
    else:
        if balanced:
            print("YES")
        else:
            print("NO")

"""
2
[ ( { } ) ]
{ ( ] }

YES
NO
"""
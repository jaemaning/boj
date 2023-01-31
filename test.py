#9012 괄호
# 4949 균형잡힌 세상
import sys
input = sys.stdin.readline

n = input().rstrip()

while n != "." :
    result = []

    for le in n:
        if le == "(":
            result.append(1)
        elif le == ")":
            if result and result[-1] == 1:
                result.pop()
            else:
                print("no")
                break
        elif le == "[":
            result.append(2)
        elif le == "]":
            if result and result[-1] == 2:
                result.pop()
            else:
                print("no")
                break
    else:
        if result == []:
            print("yes")
        else:
            print("no")

    
    n = input().rstrip()

def isValid(s):
    dic = {')':'(',']':'[','}':'{'}
    stk = []
    for i in s:
        # opening brace
        if i not in dic:
            stk.append(i)
        else:
            if stk == []:
                return False
            if stk.pop() != dic[i]: # pop last element
                return False
    return stk == []
"""
Validate Parenthesis in a string and return True or False
"""


close = {
    '}':'{',
    ']':'[',
    ')':'('
}
def parenthesis_validation_using_for_loop(s):
    stack=[]
    for i in s:
        if i.isalpha():
            continue
        elif i in "[({":
            stack.append(i)
            #print("after appending {}, stack is {}".format(i,stack))
        elif i in "}])":
            #print(i,stack[-1],close[i],stack)
            #if (len(stack) == 0) or  (S[-1] + i not in {'()','{}','[]'}):
            if (len(stack) == 0) or (stack[-1] != close[i]):
                return False
            else:
                stack.pop()
                #print('after popping {}'.format(S))
    return True if len(stack)==0 else False

def parenthesis_validation_using_while_loop(s):
    stack=[]
    i=0
    while i < len(s):
        if s[i] in "[({":
            stack.append((s[i]))
            #print("after appending {}, stack is {}".format(s[i], stack))

        elif s[i] in "}])":
            #print(s[i], stack[-1], close[s[i]], stack)
            if (len(stack) == 0) or (stack[-1] != close[s[i]]):
                return False
            else:
                stack.pop()
                #print('after popping {}'.format(stack))
        i=i+1
    return True if len(stack)==0 else False

if __name__ == '__main__':
    print(parenthesis_validation_using_while_loop("()"))
    print(parenthesis_validation_using_while_loop(")("))
    print(parenthesis_validation_using_while_loop("[(])"))
    print(parenthesis_validation_using_while_loop("{()()}"))
    print(parenthesis_validation_using_while_loop("{{[]}}]"))
    print(parenthesis_validation_using_while_loop("a,{{[)]}}]"))
    print("*"*50)
    print(parenthesis_validation_using_for_loop("()"))
    print(parenthesis_validation_using_for_loop(")("))
    print(parenthesis_validation_using_for_loop("[(])"))
    print(parenthesis_validation_using_for_loop("{()()}"))
    print(parenthesis_validation_using_for_loop("{{[]}}]"))
    print(parenthesis_validation_using_for_loop("a,{{[)]}}]"))


#https://www.youtube.com/watch?v=QZOLb0xHB_Q
#https://www.youtube.com/watch?v=xY65bgfXJTk
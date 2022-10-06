open_parenthesis = ['(', '{', '[']
close_parenthesis = [')', '}', ']']
def checkBalance(userInput):
    #create a stack to populate
    stack = []
    for element in userInput:
        #add to stack if it is an open parenthesis
        if element in open_parenthesis:
            stack.append(element)
        #
        elif element in close_parenthesis:
            #grab the index of our array of closed parenthesis characters that
            #matches to the parenthesis in the array
            indexCloseArray = close_parenthesis.index(element)
            #if the stack is not empty, and if the current top of the stack matches the open parenthesis that would cancel out the current closed parenthesis
            if ((len(stack) > 0) and (open_parenthesis[indexCloseArray] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
      return True
    else:
      return False
print(checkBalance("()"))
print(checkBalance("((}))"))
print(checkBalance("(({}){})"))
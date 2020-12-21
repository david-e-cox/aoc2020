#!/usr/bin/python3

f=open('input.txt')
problems=f.read().split('\n')
problems=problems[:-1]
f.close()


def doPostFix(expression):
    # PostFix expression calculation(+,* only opeartors)
    stack=[]
    for c in expression:
        if c.isdigit():
            stack.append(int(c))
        elif c=='+':
            stack.append(stack.pop()+stack.pop())
        elif c=='*':
            stack.append(stack.pop()*stack.pop())
    return(stack[0])



def mkPostFix(ques,part):
    # Convert  inFix expression into a postFix expression
    # Part==1 has * and + equal in precedence
    # Part==2 has + above * in precedence
    expression=''
    stack=[]
    for c in ques.replace(' ',''):
        if c.isdigit():
            expression+=c
        elif (c=='+' or c=='*') and part==1:
            if len(stack)>0 and stack[-1]!='(':
                expression+=stack.pop()
            stack.append(c)
        elif c=='+' and part==2:
            stack.append(c)
        elif c=='*' and part==2:
            while len(stack)>0 and stack[-1]=='+':
                expression+=stack.pop()
            stack.append(c)
        elif c=='(':
            stack.append(c)
        elif c==')':
            done=False
            while not done:
                oper = stack.pop()
                if oper=='(':
                    done=True
                else:
                    expression+=oper
    # Finish with all operators left in stack
    for i in range(len(stack)):
        expression+=stack.pop()
    return(expression)


sumA=sumB=0
for line in problems:
    sumA+=doPostFix(mkPostFix(line,1))
    sumB+=doPostFix(mkPostFix(line,2))
    
print("The solution to part A is {0:d}".format(sumA))
print("The solution to part B is {0:d}".format(sumB))


val = input()
stack =[]

def valid(val) :
    for i in range(len(val)) :
        if val[i] == "{" :
            stack.append(val[i])
        elif val[i] == "}":
            if len(stack)>=1 :
                stack.pop()
            else :
                print("유효하지 않은 중괄호 쌍입니다.")
                return
    if len(stack) >= 1:
        print("유효하지 않은 중괄호 쌍입니다.")
    else : 
        print("유효한 중괄호 쌍입니다.")
    return

valid(val)

import sys

def count(m, li):
    cnt = 0
    for i in range(len(li)):
        temp = li[i]
        while m<temp:
            temp-=m
            cnt +=1
    return cnt

def binary_search(f, b, li):
    m=(f+b)//2
    cnt = count(m, li)
    if cnt < 10:
        return binary_search(f-1, m+1, li) #재귀문에 return 쓰지 않으면 None 뜸
    elif cnt > 10:
        return binary_search(m+1, b-1, li) #재귀문에 return 쓰지 않으면 None 뜸
    else :
        n = m
        while True:
            n += 1
            check = count(n,li)
            if check == 10: continue
            break
        return n-1


#put numbers in lan
lan = [int(input()) for i in range(4)] 

# set front = smallest input num , set back = sum//10
front = 1
back = 215
mid = (front+back)//2

print(binary_search(front, back, lan))

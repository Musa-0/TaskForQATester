cyklops = int(input())
param_eyes = list(map(int,input().split(" ")))
param_eyes.sort()
i = 0
count = 0
while i<cyklops-1:
    if param_eyes[i]+1>=param_eyes[i+1]:
        count+=1
        i+=2
    else:
        count+=1
        i+=1
print(count)



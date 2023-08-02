cyklops = int(input())
param_eyes = list(map(int,input().split(" ")))
param_eyes.sort()
i = 0
count = 0
while i<cyklops:
    if i==cyklops-1:
        count+=1
        break
    if param_eyes[i]+2>=param_eyes[i+1]:
        count+=1
        i+=2
    else:
        count+=1
        i+=1
print(count)



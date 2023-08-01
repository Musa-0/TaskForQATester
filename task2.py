price = int(input())
money = int(input())
change = money-price

arr = [5000,2000,1000,500,200,100,50,10,5,2,1]

result = []
for i in arr:
    result.append(change//i)
    change=change%i

answer = ""
for i in range(11):
    if result[i]==0:
        continue
    answer+=f"{arr[i]} руб:{result[i]} шт., "

print(answer[:-2])


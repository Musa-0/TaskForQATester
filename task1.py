num = int(input())
sum = 1
if num<1:
    sum=0

for i in range(2, num+1):
    flag=True
    for j in range(2,i//2+1):  #для проверки на простое число, требуется проверить лишь половину от всех чисел до i, не стоит обходить все числа от 2 до i
        if i%j==0:
            flag=False
    if flag:
        print(i)
        sum+=i
print(sum)

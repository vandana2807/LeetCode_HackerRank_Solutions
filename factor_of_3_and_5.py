#factor of 3 and 5
low = 200
high = 405
count = 0
for i in range(low,high+1):
    num = i
    while (num % 3 == 0):
        num /= 3
    while (num % 5 == 0):
        num /= 5
        
    if (num == 1):
        count=count+1
print(count)

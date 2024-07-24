# find the even num divisible by 3 within 100 to 1000
count = 0
for x in range(100,1000):
    if(x%2==0 and x%3==0):
        print(x,end=' ')
        count = count+1
print("the total number of even num divisible by 3 : ",count)
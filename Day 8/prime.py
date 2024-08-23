count=0
num=int(input("Enter a number: "))
for i in range(1,num+1):
    if((num)%i==0):
        count=count+1

if count==2:
    print("The number is  prime")
else:
    print("The number is not prime")
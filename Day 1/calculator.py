num1=int(input("Enter a 1st number "))
operator=input("Enter operatort(+,-,*,/): ")
num2=int(input("Enter a 2nd number "))
if operator=="+":
    result=num1+num2
    print("Answer is ",result)
elif operator=="-":
    result=num1-num2
    print("Answer is ",result)
elif operator=="*":
    result=num1*num2
    print("Answer is ",result)
elif operator=="/":
    result=num1/num2
    print("Answer is ",result)
else:
    print("invalid operator")
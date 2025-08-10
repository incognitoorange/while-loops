number=int(input("Enter a number"))
sum=0
x=number
while x>0:
    y=x%10
    sum+=y**3
    x//=10
if  number==sum:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstrong number")
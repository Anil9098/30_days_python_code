#task 1
# make a program number is divisible by 2 or not
a=int(input("enter a number \n "))
if( a%2==0):
    print("number is divisible by 2 ")
else:
    print("number is not divisible by 2")
    
#task 2
#make a program percentage is grade A or not
p=int(input("enter your percentage \n "))
if (p>=90) :
    print("you got 'A' grade")
elif(p>=80 and p<90 ):
    print("you got 'B' grade" )
elif (p>=70 and p<80 ):
    print("you got 'c' grade")
elif(p>=60 and p<70):
    print("you got 'D' grade")
else:
    print("you are fail")
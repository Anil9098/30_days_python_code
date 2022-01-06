#task 1
#calculate compound interest
p=int(input("enter principle \n"))
t=int(input("enter time in years \n"))
r=int(input("enter rate \n"))
A=p*((1+r/100)**t)
print("amount =",A)
CI=A-p
print("compound interest =",CI)

#task 2
# calculate percentage
O =int(input("enter your marks \n"))
T =int(input("enter total marks \n"))
P = (O/T)*100
print("percentage =",P)

#task 3
#print only first second and middle string only
s=input("enter a string \n")
print(s[0:1])
print(s[:2])

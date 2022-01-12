print("welcome to our online shop \n ")
print("product -vivo pro : price 9999 \n if you want to buy type 1")
print("product - boat speakers : price 999 \n if you want to buy type 2")
print("product - Mi watch : price 999 \n if you want to buy type 3")
print("product - googles : price 99 \n if you want to buy type 4")
a=int(input("type number of product that you choose in list : "))

if a==1:
    print(" Thanks for selecting Vivo pro mobile phone \n")
    print(" If you have  coupon code - DIS12 \n ")
    d=input(" Type coupon code to get discount \n ")
    if (d=="DIS12"):
        print(9999-(9999*5/100))
    else:
        print("Sorry,you don't get any discount.you have to pay : \n",9999)
elif(a==2):
            print("Thanks for selecting boat speakers \n")
            print(" If you have  coupon code - DIS45 \n ")
            d=input(" Type coupon code to get discount \n ")
            if (d=="DIS45"):
                print(999-(999*5/100))
            else:
                print("Sorry,you don't get any discount.you have to pay : \n",999)
elif(a==3):
    print("Thanks for selecting mi watch \n")
    print(" If you have  coupon code - DIS56 \n ")
    d=input(" Type coupon code to get discount \n ")
    if (d=="DIS56"):
        print(999-(999*5/100))
    else:
        print("Sorry,you don't get any discount.you have to pay : \n",999)
elif(a==4):
    print("Thanks for selecting googles \n")
    print(" If you have  coupon code - DIS67 \n ")
    d=input(" Type coupon code to get discount \n ")
    if (d=="DIS67"):
        print(99-(99*5/100))
    else:
        print("Sorry,you don't get any discount.you have to pay : \n",99)
else:
    print("you don't have selected any item \n ")
    print("Thanks for visiting our online shop \n1")
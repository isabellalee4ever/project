menu={
   "frappuccino":5.00,
   "cappuccino":4.30,
   "hot chocolate":4.00,
   "chocolate chip cookie":3.00,
   "sugar cookie": 2.00,
   "latte":5.50,
   "iced tea":4.00,
   "brownie":2.50,
}
# print(menu)
tax=1.1025

# order=input("what would you like to order? Type exit to exit")
print("menu")
for i in menu:
    print(i,": $"+str(menu[i]))
order=input("what would you like to order? Type exit to exit ")
price=0
reciept={}
while order!="exit":
   num=int(input("how many do you want to order?"))
   price+=menu[order]*num 
   tempprice=menu[order]*num
   reciept[order + " x " + str(num)]=tempprice
   order=input("what would you like to order? Type exit to exit ")
reciept["subtotal"]="$"+str(price)
reciept["tax"]=str(round((tax-1)*100, 2))+"%"
reciept["total with tax"]="$"+str(round(price*tax, 2))
print("your total price is $", round(price*tax, 2))
print("reciept")
for i in reciept:
   print(i,": $"+str(reciept[i]))




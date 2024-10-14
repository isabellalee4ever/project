menu={
   "frappuccino":5.00,
   "cappuccino":4.30,
   "hot chocolate":4.00,
   "choclate chip cookie":3.00,
   "sugar cookie": 2.00,
   "latte":5.50,
   "iced tea":4.00,
   "brownie":2.50,
}
# print(menu)

# order=input("what would you like to order? Type exit to exit")
for i in menu:
    print(i,": $"+str(menu[i]))

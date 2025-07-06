# print("hello world!")
# age = 45
# print("age after 5 years is :",age + 5)
# print(type(True))
# print(int(True))
# x = 10
# y = x > 5 and x > 15
# print(int(y))
# print(int(float("0.5")))
itemname = (input("enter item name : "))
quantity = (int(input("number of items : ")))
price = (float(input("enter price of 1 item : ")))
subtotal = price * quantity
GST = 0.18 * subtotal
print("----------------------invoice--------------------------")
print("itemname : ",itemname)
print("quantity : ",quantity)
print("subtotal : ",subtotal)
print("GST(18%) : ",GST)
print("total    : ",GST + subtotal)
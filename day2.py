count = 1
product1 = input(f"enter product {count} : ")
price1 = float(input(f"enter price of product {count} : "))
product2 = input(f"enter product {count + 1} : ")
price2 = float(input(f"enter price of product {count + 1} : "))
product3 = input(f"enter product {count + 2} : ")
price3 = float(input(f"enter price of product {count + 2} : "))
total_cost = price1 + price2 + price3
print("-" * 30)
print(f"product 1 : {product1}  and price : {price1}")
print(f"product 2 : {product2}  and price : {price2}")
print(f"product 3 : {product3}  and price : {price3}")
print(f"total cost : {total_cost}")
print("-" * 30)




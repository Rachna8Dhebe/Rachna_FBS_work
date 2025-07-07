cost_price = float(input("Enter cost price of the book: "))
discount = float(input("Enter discount percentage: "))
selling_price = cost_price - (cost_price * discount / 100)
print("Selling Price of the book:", selling_price)

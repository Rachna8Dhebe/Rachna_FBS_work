interior_area=float(input("Enter the area"))
interior_cost=float(input("Enter the cost"))
exterior_area=float(input("Enter the area"))
exterior_cost=float(input("Enter the cost"))
int_cost=interior_cost*interior_area
ext_cost=interior_cost*interior_area
painting_cost=int_cost+ext_cost
print("Cost of painting",painting_cost)

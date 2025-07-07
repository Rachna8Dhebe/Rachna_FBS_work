feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))
total_inches = feet * 12 + inches
centimeters = total_inches * 2.54
meters = int(centimeters // 100)
remaining_cm = centimeters % 100
print(f"Distance = {meters} meters and {remaining_cm:.2f} centimeters")
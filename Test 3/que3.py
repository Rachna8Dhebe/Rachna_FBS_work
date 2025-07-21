n = int(input("Enter number of employees: "))

total_salary_all = 0 

for i in range(n):
    basic = float(input(f"\nEnter basic salary for employee {i+1}: "))

    if basic < 20000:
        da = basic * 0.10
        ta = basic * 0.12
        hra = basic * 0.15
    else:
        da = basic * 0.15
        ta = basic * 0.18
        hra = basic * 0.20

    total_salary = basic + da + ta + hra
    print(f"Total salary of employee {i+1}: {total_salary:.2f}")
    
    total_salary_all += total_salary

print(f"\nTotal salary of all employees: {total_salary_all:.2f}")

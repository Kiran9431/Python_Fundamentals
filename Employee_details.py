FirstName = input("Employee_name: ")
LastName = input("Employee_name: ")
CurrentPosition = input("Current Position: ")
DOB = input("date of birthday: ")
Company = input("Company: ")
Email = input("Email address: ")


MonthlySalary = float(input("Monthly salary (AED):" ))
Bonus = float(input("Bonus (months): "))

AnnualPackage = (MonthlySalary * 12) + (MonthlySalary * Bonus)

print("\n----- Employee Details -----")
print("Employee Name:", FirstName, LastName)
print("Current Position:", CurrentPosition)
print("Date of Birth:", DOB)
print("Company:", Company)
print("Email address:", Email)
print("Monthly Salary:", MonthlySalary)
print("Annual Package:", AnnualPackage, "AED")


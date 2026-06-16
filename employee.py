import pandas as pd

# Load CSV
df = pd.read_csv("employee.csv")

# Average Salary
avg_salary = df["Salary"].mean()
print("Average Salary:", avg_salary)

# Department Count
dept_count = df["Department"].value_counts()
print("\nDepartment Count:")
print(dept_count)

# Filter Employees
threshold = 60000
high_salary = df[df["Salary"] > threshold]

print("\nEmployees with Salary > 60000")
print(high_salary)

# Export Results
high_salary.to_csv("high_salary_employees.csv", index=False)

print("\nFiltered data exported successfully.")
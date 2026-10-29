
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read employee details from the CSV file
# Expected columns: Name, Department, Salary
df = pd.read_csv("employee.csv")

# 2. Display employee names, departments, and salaries
print("Employee Details")
print(df[["Name", "Department", "Salary"]].to_string(index=False))

# 3. Calculate the average salary for each department
avg_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department")
print(avg_salary.round(2))

# 4. Identify the highest-paid employee
top = df.loc[df["Salary"].idxmax()]

print("\nHighest Paid Employee")
print(f"Name: {top['Name']}")
print(f"Department: {top['Department']}")
print(f"Salary: {top['Salary']}")

# 5. Bar chart comparing average salaries by department
plt.figure(figsize=(8, 5))
avg_salary.plot(kind="bar", color="steelblue")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Histogram showing the distribution of employee salaries
plt.figure(figsize=(8, 5))
plt.hist(df["Salary"], bins=10, color="seagreen", edgecolor="black")

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

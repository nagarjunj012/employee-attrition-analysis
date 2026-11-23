import pandas as pd
import matplotlib.pyplot as plt

employees = pd.read_csv("data/employee_attrition.csv")

print(employees)

print("\nNumber of rows and columns:")
print(employees.shape)

print("\nColumn names:")
print(employees.columns)

employee_who_left = (employees["attrition"] == "Yes").sum()
total_employee = len(employees)
attrition_rate = employee_who_left / total_employee * 100

print("\nEmployees who left : ",employee_who_left)
print("Total employees : ", total_employee)
print("Attrition rate : ", round(attrition_rate,2),"%")

attrition_by_department = employees.groupby("department")["attrition"].apply(
    lambda values : (values == "Yes").sum() / len(values) * 100)

print("\n Attrition By Department : ")
print(attrition_by_department.round(2))

attrition_by_role = employees.groupby("job_role")["attrition"].apply(
    lambda values : (values == "Yes").sum() / len(values) * 100)

print("\nAttrition by role")
print(attrition_by_role.round(2))

employees["service_group"] = employees["years_at_company"].apply(
    lambda years : "1-2 years" if years <=2 else "3+ years"
)

attrition_by_service = employees.groupby("service_group")["attrition"].apply(
    lambda values : (values == "Yes").sum() /len(values) * 100
)

print("\n Attrition by service")
print(attrition_by_service.round(2))

attrition_by_department.plot(kind="bar", color="steelblue")

plt.title("Attrition Rate by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()
plt.show()

attrition_by_role.plot(kind="bar", color="darkorange")

plt.title("Attrition Rate by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

attrition_by_service.plot(kind="bar", color="seagreen")

plt.title("Attrition Rate by Length of Service")
plt.xlabel("Length of Service")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()
plt.show()
salary = float(input())

readj_index = 0

if (salary <= 400):
    readj_index = 0.15
elif (salary >= 400.01 and salary <= 800):
    readj_index = 0.12
elif (salary >= 800.01 and salary <= 1200):
    readj_index = 0.1
elif (salary >= 1200.01 and salary <= 2000):
    readj_index = 0.07
elif (salary > 2000):
    readj_index = 0.04

new_salary = (salary*readj_index) + salary
diff = new_salary - salary
percentage = int(readj_index * 100)

print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {diff:.2f}")
print(f"Em percentual: {percentage} %")

import csv

#Read into the employeepay.csv file 
employees = open('employeepay.csv', 'r')

employee_file = csv.reader(employees, delimiter = ',')

next(employee_file)

for record in employee_file:
    salary = int(record[3])
    bonus = float(record[4])
    calc_bonus = salary * bonus
    calc_total = salary + (salary * bonus)

    print("First Name: ", record[1])
    print("Last Name: ", record[2])
    print("Salary: $", format(salary, ',.2f'), sep = '')
    print("Bonus Amount: $", format(calc_bonus, ',.2f'), sep = '')
    print("Total Pay: $", format(calc_total, ',.2f'), sep = '')

    input()


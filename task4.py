import random as rd
import locale

places = ["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgaon", "Hyderabad"]

def rand_emp_details():
    while True:
        emp_id = rd.randint(1, 9999)
        emp_location = rd.choice(places)
        emp_salary = rd.randint(20000, 150000)
        locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
        formatted_salary = locale.format_string('%d', emp_salary, grouping=True)
        
        yield f"Employee ID: {emp_id}\nEmployee Location: {emp_location}\nEmployee Salary: {formatted_salary}\n"


emp_num_str = input("Enter the number of employee details required : ")
    
if emp_num_str == "":
    print("Exiting the program.")
else:
    if emp_num_str.isnumeric():
        emp_num = int(emp_num_str)
        emp_gen = rand_emp_details()

        for i in range(emp_num):
            print(next(emp_gen))
    else:
        print("Invalid input, Please enter a number")

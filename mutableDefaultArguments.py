# def add_emplyee(emp, emp_list=[]):
#     emp_list.append(emp)
#     print(emp_list)

# emps = ['John', 'Jane']

# add_emplyee('Corey')
# add_emplyee('John')
# add_emplyee('Jane')

# When the obove code is run it will kwwping adding to employee


def add_emplyee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)


EMPS = ["John", "Jane"]

add_emplyee("Corey")
add_emplyee("John")
add_emplyee("Jane")
add_emplyee("Jamal", EMPS)

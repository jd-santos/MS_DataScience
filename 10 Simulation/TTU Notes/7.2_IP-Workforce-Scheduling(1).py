# Example: Workforce Scheduling

from pulp import *

# Creates a dictionary for the hourly staff demand
staffDemand = {"8-9": 5, 
            "9-10": 12,
            "10-11": 15,
            "11-noon": 12,
            "noon-1": 11,
            "1-2": 18,
            "2-3": 17,
            "3-4": 19,
            "4-5": 14}

permanentEmployee = 5

# Creates the prob variable to contain the problem data
prob = LpProblem("Transportation Problem",LpMinimize)

x1 = LpVariable("shift1", 0, cat='Integer')
x2 = LpVariable("shift2", 0, cat='Integer')
x3 = LpVariable("shift3", 0, cat='Integer')
x4 = LpVariable("shift4", 0, cat='Integer')
x5 = LpVariable("shift5", 0, cat='Integer')
x6 = LpVariable("shift6", 0, cat='Integer')


# The objective function is added to prob first
prob += x1+x2+x3+x4+x5+x6, "Sum of part time staffs"


# The capacity constraints are added to prob for each hour staff demand

prob += x1 >= staffDemand["8-9"] - permanentEmployee, "Staff demand 8-9 am"
prob += x1 + x2 >= staffDemand["9-10"] - permanentEmployee, "Staff demand 9-10 am"
prob += x1 + x2 + x3 >= staffDemand["10-11"] - permanentEmployee, "Staff demand 10-11 am"
prob += x1 + x2 + x3 + x4 >= staffDemand["11-noon"] - permanentEmployee, "Staff demand 11-noon"
prob += x2 + x3 + x4 + x5 >= staffDemand["noon-1"] - permanentEmployee, "Staff demand noon-1"
prob += x3 + x4 + x5 + x6 >= staffDemand["1-2"] - permanentEmployee, "Staff demand 1-2"
prob += x4 + x5 + x6 >= staffDemand["2-3"] - permanentEmployee, "Staff demand 2-3"
prob += x5 + x6 >= staffDemand["3-4"] - permanentEmployee, "Staff demand 3-4"
prob += x6 >= staffDemand["4-5"] - permanentEmployee, "Staff demand 4-5"

print(prob)

prob.solve()

print("Status:", LpStatus[prob.status])

print("objective=", value(prob.objective))

for v in prob.variables():
	print(v.name, "=", v.varValue)
# Portfolio Investment Risk Modeling

from pulp import *

prob = LpProblem("My LP Problem", pulp.LpMinimize)

x1 = LpVariable('Cisco', lowBound = 0, upBound = 200)
x2 = LpVariable('Microsoft', lowBound = 0, upBound = 200)
x3 = LpVariable('Intel', lowBound = 0, upBound = 200)
x4 = LpVariable('BofA', lowBound = 0, upBound = 200)
x5 = LpVariable('FirstBank', lowBound = 0, upBound = 200)
x6 = LpVariable('ING', lowBound = 50, upBound = 200)

# Objective function
prob += (14.02)*x1 + 10.57*x2 + 13.22*x3 + (9.36)*x4 + (7.61)*x5 + 2.39*x6, "Obj"
# Constraints
prob += x1 + x2 + x3 + x4 + x5 + x6 == 500, "Portfolio" 
prob += 0.08*x1 +  0.06*x2 + 0.05*x3 + 0.07*x4 + 0.04*x5 + 0.02*x6 >= 25, "Return"
prob += x4 + x5 >= x1+ x2 + x3, "Balance"

print(prob)

prob.solve() 
print("status: " + LpStatus[prob.status]) 

for variable in prob.variables():
     print("{}* = {}".format(variable.name, variable.varValue)) 
     
print(value(prob.objective))


# We add these lines for sensitivity analysis
print("\n Sensitivity Analysis:")

for name, c in prob.constraints.items():
    print("\n{}: Slack={}, Shadow Price = {}".format(name, c.slack, c.pi)) # OR
#    print("\n", name, ":", ", Slack=", c.slack, ", Shadow Price=", c.pi)

print("\n ========================================")

for variable in prob.variables():
     print("\n{}* = {},   Reduced Cost = {}".format(variable.name, variable.varValue, variable.dj)) 























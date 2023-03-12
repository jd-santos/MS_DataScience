from pulp import *

# Instantiate our problem class
prob = LpProblem("Cost minimizing blending problem", pulp.LpMinimize)

ep = LpVariable('kg_eco_pork', lowBound = 0)
ew = LpVariable('kg_eco_wheat', lowBound = 0)
es = LpVariable('kg_eco_strarch', lowBound = 0)
pp = LpVariable('kg_prem_pork', lowBound = 0)
pw = LpVariable('kg_prem_wheat', lowBound = 0)
ps = LpVariable('kg_prem_strarch', lowBound = 0)

# Objective function 
prob += 4.32 * (ep + pp) + 2.46 * (ew + pw) + 1.86 * (es + ps), "Obj"

# Constraints
# 350 economy and 500 premium sausages at 0.05 kg
prob += ep + ew + es == 350 * 0.05
prob += pp + pw + ps == 500 * 0.05

# Economy has >= 40% pork, premium >= 60% pork
prob += ep >= 0.4*(ep + ew + es) 
prob += pp >= 0.6*(pp + pw + ps) 

# Sausages must be <= 25% starch
prob += es <= 0.25*(ep + ew + es) 
prob += ps <= 0.25*(pp + pw + ps) 

# We have at most 30 kg of pork, 20 kg of wheat and 17 kg of starch available
prob += ep + pp <= 30
prob += ew + pw <= 20
prob += es + ps <= 17

print(prob)
# Solve our problem
prob.solve()

print(LpStatus[prob.status])

for variable in prob.variables():
    print("{} = {}".format(variable.name, variable.varValue))
    
print("Z* = ", value(prob.objective))
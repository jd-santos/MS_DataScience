# Example: WYNDOR GLASS CO. 
# Max: Z = 3x_1 + 5x_2
# S.t.
#  x_1        <= 4
#        2x_2 <= 12
# 3x_1 + 2X_2 <= 18
# X_1 and X_2 >= 0 

# Model in Python 
from pulp import * 
# Define the Model
prob = LpProblem("WYNDOR GLASS CO.", LpMaximize) 
x1 = LpVariable('x_1', lowBound = 0) 
x2 = LpVariable('x_2', lowBound = 0) 
# Objective function 
prob += 3*x1 + 5*x2, "Obj" 
# Constraints 
prob += x1 <= 4  
prob += 2*x2 <= 12 
prob += 3*x1 + 2*x2 <= 18 
print(prob)

prob.solve() 
print("status: " + LpStatus[prob.status]) 

for variable in prob.variables():
     print("{}* = {}".format(variable.name, variable.varValue)) 
     
print(value(prob.objective))


# **Conclusions**

# The OR team used this approach to find that the optimal solution is $x_1 = 2$, $x_2 = 6$, with $Z = 36$. 
# This solution indicates that the Wyndor Glass Co. should produce products 1 and 2 at the rate of 2 batches 
# per week and 6 batches per week, respectively, with a resulting total profit of $36,000 per week. 
# No other mix of the two products would be so profitable *according to the model*.
# Import PuLP modeller functions
from pulp import *

# Creates the problem
prob = LpProblem("Transportation Problem",LpMinimize)

# Creates a list of variables containing all the possible routes for transport
mar_clev = LpVariable('mar_clev', lowBound = 0)
mar_balt = LpVariable('mar_balt', lowBound = 0)
mar_chig = LpVariable('mar_chig', lowBound = 0)
mar_phoe = LpVariable('mar_phoe', lowBound = 0)
min_clev = LpVariable('min_clev', lowBound = 0)
min_balt = LpVariable('min_balt', lowBound = 0)
min_chig = LpVariable('min_chig', lowBound = 0)
min_phoe = LpVariable('min_phoe', lowBound = 0)

# The objective function is added to prob first
prob += 12.6*mar_clev + 14.35*mar_balt + 11.52*mar_chig +  17.58*mar_phoe + 9.75*min_clev + 16.26*min_balt + 8.11*min_chig +  17.92*min_phoe
        
# The capacity constraints are added to prob for each supply node (plant)
prob += mar_clev + mar_balt + mar_chig + mar_phoe <= 1500
prob += min_clev + min_balt + min_chig + min_phoe <= 800

# The demand minimum constraints are added to prob for each demand node (dc)
prob += mar_clev + min_clev >= 150
prob += mar_balt + min_balt >= 350
prob += mar_chig + min_chig >= 500
prob += mar_phoe + min_phoe >= 1000

print(prob)

prob.solve()

print("Status:", LpStatus[prob.status])

for variable in prob.variables():
    print("{} = {}".format(variable.name, variable.varValue))
    
print("Z* = ", value(prob.objective))


# We add these lines for sensitivity analysis
print("\n Sensitivity Analysis: ")

for name, c in prob.constraints.items():
	print("\n", name, ":", ", Slack=", c.slack, ", Shadow Price=", c.pi)

for v in prob.variables():
  print ("\n", v.name, "=", v.varValue, ", Reduced Cost=", v.dj)


    


        

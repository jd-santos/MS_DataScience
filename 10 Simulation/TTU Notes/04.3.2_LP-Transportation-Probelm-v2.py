# Import PuLP modeller functions
from pulp import *

# Creates a list of all the supply nodes
plant = ["Marietta","Minneapolis"]

# Creates a dictionary for the capacity of supply
capacity = {"Marietta": 1200, 
            "Minneapolis": 800}

# Creates a list of all distribution centers
dc = ["Cleveland", "Baltimore", "Chicago", "Phoenix"]

# Creates a dictionary for the number of units of demand for each DC
demand = {"Cleveland": 150,
        "Baltimore": 350,
        "Chicago": 500,
        "Phoenix": 1000}

# Creates a list of costs of each transportation path
costs = [#DC
         #Clev   Balt   Chic   Phoe
         [12.60, 14.35, 11.52, 17.58],#Marie  Plant
         [9.75 , 16.26, 8.11 , 17.92] #Minne
         ]

# Creates the prob
prob = LpProblem("Transportation Problem",LpMinimize)

# Creates a list of tuples containing all the possible routes for transport
Routes = [(i,j) for i in range(0,len(plant)) for j in range(0, len(dc))]

# A dictionary called route_vars is created to contain the referenced variables (the routes)
route_vars = LpVariable.dicts("Route",(plant, dc), lowBound = 0)

# The objective function is added to prob first
prob += lpSum([route_vars[plant[i]][dc[j]]*costs[i][j] for (i,j) in Routes]), "Sum of Transporting Costs"


# The capacity constraints are added to prob for each supply node (plant)
for i in plant:
    prob += lpSum([route_vars[i][j] for j in dc]) <= capacity[i], "Sum of Products out of plant %s"%i


# The demand minimum constraints are added to prob for each demand node (dc)
for j in dc:
    prob += lpSum([route_vars[i][j] for i in plant]) >= demand[j], "Sum of Products into DC %s"%j
    
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
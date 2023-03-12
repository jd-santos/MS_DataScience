# 6 Data Structures
## Overview
- Two dimensions
	- Entity
		- Observable behavior, information, or thing
		- E.g. individuals, states, companies, etc
	- Time/count
		- How many times an entity occurs over a period of time

### Cross-sectional data
- Multiple entities at a point in time
- E.g. Data on 420 California school districts in 1999
### Time-series data
- A single entity over multiple times
- I.e. multiple observations
- Data on daily sales of Amazon between 2005 and 2009
### Panel data
Multiple entities over multiple times: “Cross-sectional time-series data”
#### Why Use Panel Data? 
- Unobserved or unmeasured factors
	- These won’t appear in regression/multiple regression
- Factors that vary across entities but not over time
- Factors that could cause omitted variable bias 
	- If an omitted variable does not change over time, then changes in Y over time can’t be caused by that variable
## Omitted Variable Bias
- Leaving out relevant variables
- The OLS regression coefficient on a regression will be biased when there is some other variable omitted from the regression with the following properties:
	- The omitted variable is correlated with the regressor AND
	- The Omitted variable is a determinant of Y
	- I.e. it is correlated with X and is a determinant of Y 
- Important least-square assumption is violated:
	- The error term is independent of the x’s
	- $E(u_i|X_i) = 0$ will not be true
## Using Panel Data to Address Omitted Variable Bias
- Panel data helps eliminate this bias when the omitted variables are constant over time within a given state
- If the unknown variable does not change between time periods, then any change to Y cannot be caused by that variable
	- Finding the difference between the same equation from two different time periods removes the omitted variable, even if it is unobserved
## Fixed Effects Model
- "Common trends assumption"
	- If there's some unobserved confounder, it can differ in levels across the treatment group and control group, but changes in time have to affect each group the same
- Exception: Fixed effects (or individual effect)
	- Variable that doesn't change over time
- A strength of panel data is that fixed variables can remain unobserved, the value can be different in treatment and control group without affecting causality
	- Doesn't violate common trends assumption
### The Model
$Y_{it} = β_0 + β_1X_{it} + β_2Z_i + u_{it}$
- i is an entity = 1...n
- T is time = 1...n
- Z = unobserved variable
- Multiple entities and times
- The intercept is unique to a particular i, but the slope is the same for all other values of i
	- Parallel lines
- This shows that variables can still be compared, as the unobserved fixed variables only affect intercept 
	- It is fixed over time
	- E.g. car safety between states
		- Might vary from state to state, but changes (slope) equally
### Time Fixed Effects Model
- An omitted model might vary over time instead of observation
- E.g. Car safety between states
	- Safer cars and changes in national laws
	- Intercepts will now change over time 
	- However, all states are affected equally
$Y_{it} = β_0 + β_1X_{it} + β_2S_t + u_{it}$
- Notice the that $β_2S_t$ is now indicating time, not entity as in the above model
	

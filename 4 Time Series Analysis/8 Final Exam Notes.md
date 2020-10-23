# 8 Final Exam Notes
## Module 1
- Finding lower and upper bounds
	- Coefficient -/+ CI(given) * standard error
		- Minus: lower bound
		- Plus: Upper
- Find t-stat
	- Coefficient / std error
## Module 2
- Predicted change based on variable change
	- Do the formula for both and subtract
- OLS estimator is derived from minimizing SoS of residuals
- If estimated slope coefficient is zero, r-squared equals zero
- F stat tests the null hypothesis that all slope coefficients are zero

# Module 6
- Omitting a variable when there are two independent variables
	- Has an effect on the coefficient of included variable if they are related
- Difference equation
	- Sort data if needed
	- Create new columns by subtracting required variables
	- Use as Y and X values in regression 
- Time fixed effects regressions are useful in dealing with omitted variables if they are constant across entities but vary over time 
- Dummy variables
	- Create separate columns for each variable
	- if(sourcecolumn=dummycolumnheader, 1, 0)
	- See /Tools/6.0_Fatality.xlsx 
	- Exclude one dumm year for reasons
	- Use all dummy columns and any other variables as X in regression

# Module 7
- Predicting revenue based on previous data
	- Y is revenue
	- X is days and all dummy variables for week
		- Remember to leave out one to not overfit
	- Intercept + (coeff * variable) + (coeff2 * variable2)...
		- If a coefficient is not significant (p-value), it can be considered zero
- Autoregressive Distributed Lag (ADL) models include: lags of dependent variable and additional predictive variables
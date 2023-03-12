# 3-NonLinear Regression
## Overview
- Nonlinear relationships
	- Data is not best explained by a straight line
	- Does not change at a constant rate
		- The marginal effect of X is not constant
		- The effect on Y of a change in X depends on the value of X
	- Approaches
		- Convert nonlinear relationship to linear relationship
		- Use polynomials
## Conversion of Nonlinear to Linear 
### Polynomials in X
- The regression function is approximated by a quadratic, cubic, or higher degree polynomial 
	- $Y_i = β_0 + β_1Χ_i + β_2Χ_i^2 +...+ u_i$
	- Same as linear multiple regression model
		- Regressors are powers of X
		- Estimation, hypothesis test, etc is the same as before with OLS
		- Coefficients are hard to interpret but the function works
- Quadratic specifications 
	- Two independent variables
	- $TestScore_i = β_0 + β_1Income_i + β_2(Income_i)^2 +u_i$
	- Downside
		- Quadratic equation eventually curves down
		- Doesn't make logical sense
	/Images/3.0-Quadratic Regression.png
	/Images/3.1-Quadratic Regression Ex.png
	- Excel Methods
		- Manual
			- Square X variable in separate column
			- Layout > trendline > more > polynomial 
				- Order: 2 for quadratic
			- Check $R^2$ and compare to linear 
		- Regression
			- Data Analysis > Regression
			- Input X and Y range
				- For X range use X and $X^2$ columns
- Cubic specifications
	- Two independent variables
	- $TestScore_i = β_0 + β_1Income_i + β_2(Income_i)^2 + β_3(Income_i)^3 + u_i$
- Hypothesisisis
	- $H_0$:Population coefficients on $Income^2$ and $Income^3$ = 0
	- $H_1$: At least one of these coefficients is nonzero
	- The hypothesis that population regression is linear is rejected at the 1% significance level against the alternative that it is a polynomial of a degree up to 3
### Logarithmic transformations
- Y or X is transformed by taking its logarithm 
- We have the option to take the logarithm of either the independent or dependent variable, or both
	- One or both will be logarithmic or linear
#### Log Regression Functions
- linear-linear
	- Standard regression
	- $Y_i = β_0 + β_1X_i + u_i$
- linear-log
	- Take log of only X
	- $Y_i = β_0 + β_1ln(X_i) + u_i$
	- Computer Y before and after change in X
		- Before: $Y = β_0 + β_1ln(X)$
		- After: $Y + ΔY = β_0 + β_1ln(X + ΔΧ)$
	- Subtract: After - Before
		- Pretend you know how to do this algebra
		- $ΔY = β_1ln(X + ΔΧ - ln(X))$
	- More magic algebra to break down right side
		- $ln(X + ΔΧ - ln(X)) = \left( 1 + \frac{Δx}{x} \right)\cong\frac{Δx}{x}$
	- Therefore ΔY is equivalent to:
		-  $ΔY \cong β_1\frac{Δx}{x} = 0.01β_1$ * % change of X 
	-  Interpretation
		-  1% increase in X -> 0.01 increase in ln(x) -> $0.01β_1$ increase in Y
- log-linear
	- Take log of only Y
	- $ln(Y_i) =β_0 + β_1X_i + u_i$
	- Skipping similar algebra as above to land at:
		- $\frac{ΔY}{Y} \con β_1ΔX$
	- One unit increase in X -> $β_1$ increase in ln(Y) -> $100β_1$ % increase in Y
- log-log
	- Take log of both
	- $ln(Y_i) = β_0 + β_1ln(X_i) + u_i$
	- At this point prof informs us that we don't need to know these formulas so I'm done typing them
	- This one happens to be the formula for elasticity tho so that's neat
- We need to be careful in interpretation when quantifying the impact on Y by X 
- Interpreting Log Values Resource:
	- https://data.library.virginia.edu/interpreting-log-transformations-in-a-linear-model/
#### Estimation Results Example
- Linear-Log
	- Test Score vs. ln(Income)
	- Now that we have a linear model with ln(Income) we can proceed with OLS
		- Test score = 557.8 + 36.42 * ln($Income_i$)
	- A 1% increase in Income is associated with an increase of 0.36 points of TestScore
	- All other normal regression tools apply Joe Rogan would literally be a less conservative moderator than any of the dem primary hosts 

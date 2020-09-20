# Linear Regression
## Overview
- Using one line to describe a dataset
	- Line that 'fits' the data
- The goal is to estimate the causal effect on Y of a unit change in X
- Ultimately we are trying to find the *slope* of the best-fit line
## Process
- Terminology
	- n = number of observations
	- i = nth observation 
	- X = independent variable or regressor
	- Χ = error?
	- Y = depedendent variable
	- $β_{0}$ = intercept
	- $β_{1}$ = slope
	- $μ_{i}$ = regression error
- Regression formula
==**$y = β_{1}x + β_{0}$**==
	- m = slope
		 - $β_{1} = \frac{ΔY}{ΔX}$ 
	- = Change in Y for unit change in X
- $β_{1}$ and $β_{0}$ are population parameters
	- $β_{0}$: slope
	- $β_{1}$: y-intercept
	- If we don't know slope, we must estimate it from the data
### Regression Error
==**$Y_{i} -(β_{0} + (β_{1}X_{i}))$**==
- Squared difference between actual values of $Y_{I}$ and the predicted value $(b_{0} + b_{1}X_{i})$
	- Values are squared to get rid of negatives but still account for their magnitude 
- May consist of omitted factors that influence Y other than the variable X 
- Includes error in the measurement of Y
## Ordinary Least Square (OLS)
- Estimator of unknown parameters (coefficient) $b_{0}$ and $b_{1}$ from the data

==**$min_{b_{0},b_{1}} \sum\limits_{i=1}^n [Y_{i}-(b_{0} + b_{1}X_{i})]^{2}$**==

- Minimization of the average squared difference between actual values of $Y_i$ and the predicted value based on the estimated line
	- $Y_i$ = actual values/observations 
	- $(b_{0} + b_{1}X_{i})$ = predicted values
- Can be solved using calculus 
### Estimation Interpretation
- Example: test scores and student-teacher ratio (STR)
	- $\frac{ΔTest Score}{ΔSTR} = -2.28$
	- This implies istricts with one more student-per-teacher on average have test scores that are 2.28 points lower
- Y-intercept
	- How much of the independent variable (X) with zero of the dependent variable (Y)
	- In the example, this would be the test scores with zero students per teacher
		- Sometimes the intercept isn't realistically meaningful 
### OLS Process: Math
- Start with single row (observation):
	- Determine prediction based on regression formula
		- $y = β_{1}x + β_{0}$
	- Find the error
		-  Observation - Predicted value
	-  Square that error
-  Repeat this process and get the square of every row/observation
	-  Sum all of those rows
### OLS Process: Excel
- Automanually
/Images/2-OLS_Excel_Setup.png
	- Enter formulas into each column
		- Be sure to use $ to lock intercept and slope
	- Use SUM() to sum all squares
- Regression (Data Analysis Add-In)
/Images/2.2-OLS_Excel_Regression_Menu.png
/Images/2.3-OLS_Excel_Regression_Output.png
- Using Solver (Add-In)
/Images/2-OLS_Excel_Solver.png
	- Plug your sum of squares into Objective
	- Select Min
	- Plug intercept and slope into changing variable cells
	- Output will be minimization
	- Compare this minimization to the regression
		/Images/2.4-OLS_Excel_Regression_Compare.png
## Interpretation and Measure of Fit
-Concepts
	- Measure of fit
	- t-statistics
	- Significance level
	- Confidence interval
	- P-value
- Breaking down STATA output
	/Images/2.3-OLS_Excel_Regression_Output.png
	- R Square
		- How much the dependent variable can be explained with the independent variable
	- Adjusted R Scale
	- Standard Error
		- STD of regression
	- F
		- Test whether the slope coefficient is statistically significant
	- Coefficients
		- Estimation of the intercept and slope 
	- Standard error
		- Standard deviation over estimated coefficient
	- How reliable the estimation of coefficients are
	- t State
		- 1:1 match with P-value
	- P-value
		- Probability we can reject the null hypothesis
- There are two methods to determine measure of fit: 
	- Regression $R^2$
	- Standard error the regression (SER)
### Regression ($R^2$)
- $R^2$
	- Measures the fraction of the variance of Y that is explained by X
	- Unitless and ranges between zero (no fit) and one (perfect fit)
- Deriving $R^2$
	- $Y_{i} = \hat{Y}_i + \hat{u}_i$
		- Restated: $Y_i$ = OLS Prediction + OLS residual
		- $Y_{i}$
			- Dependent variable
		- $\hat{u}_i$ 
			- Estimated error count
			- Also called residual
		- $\hat{Y}_i$ 
			- Estimated/predicted value
	- sample var(Y) = sample var($\hat{Y}_i$) + sample var ($\hat{u}_i$)
	- Total sum of Squares (SS) = "explained" SS + "residiual" SS
- Definition of $R^2$:
	- $R^2 = \frac{Explained Sum of Squares}{Total Sum of Squares}$
	==**$\frac{\sum\limits_{i=1}^n [(\hat{Y}_{i}-\overline{\hat{Y}})^2}{\sum\limits_{i=1}^n [(Y_{i}-\overline{Y})^2}$**==
	- $R^2$ = 0 means ESS = 0
	- $R^2$ = 0 means ESS = TSS
	- $0 \leq R^2 leq 1$
	- For single X regression, $R^2$ is the square of the correlation coefficient between X and Y 
	- If slope coefficient is 0, $R^2$ should also be 0
### Standard Error of the Regression (SER)
- Measures the spread of the distribution of $u$
- Similar to the sample standard deviation of OLS residuals
$\sqrt{\frac{1}{n-2} \sum\limits_{i=1}^n \hat{u}_i^2}$
- n is not normal n, but is instead realted to the df and unbiased estimator
### Hypothesis Test
- $H_0$: The estimated coefficient is the same as a hypothesized value
- $H_a$: The estimated coefficient and hypothesized value differ 
- $t-stat = \frac{Estimator-Hypothesized Value}{Std Error of the Estimator}$
- Significance level
	- Pre-specified probability of incorrectly rejecting the null when it is true
- Confidence interval
	- Estimated interval for the parameter
	- Conditional on the pre-specified significance level
- P-value
	- Probability of drawing a statistic (like slope coefficient) 
	- Sometimes called marginal significance 
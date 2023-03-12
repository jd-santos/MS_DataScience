# 5 Binary Dependent Variables
## Overview
Two options when the dependent variable is binary:
- Linear probability model
	- If you don't care that the variable is binary
	- Typically doesn't fit data as well
- Probit and Logit regression models
	- Nonlinear equations that better fit the data
### Linear Probability Model
Start with the basic linear probability model:
$Y_i =  β_0 + β_1Χ_i + u_i$
- Least square assumption gets rid of u
- Probability of 0 is 0
We end up with:
$Pr(Y = 1|X) =  β_0 + β_1Χ_i$
- The probability of Y = 1 conditional on X
- $β_1$ is the change in predicted probability per unit change in X 
/Images/5.0-Binary Y Linear Prob.png
- Note how poor of a fit this is
	- This is why we have nonlinear models
- Advantages
	- Simple to estimate and interpret
	- Inference is the same as multiple regression
- Disadvantages
	- Predicted probabilities can be <0 or >1 which is uesless 
	- The change in predicted probability for a change in X is the same for all values of X
		- Doesn't make sense either
- What we want
	- Predicted value is between 0 and 1 inclusive
	- The impact of X on probability of Y conditional on X can actually vary
### Probit Model
- Models the probability that Y=1 using the **cumulative standard normal distribution function, Φ(z)**
- Cumulative standard normal distribution function, Φ(z)
	- $z = β_0 +β_1X$
	- Called the z-value or z-index 
$Pr(Y = 1|X) = z = β_0 +β_1X$
- After evaluating, plug the result into a z table for probability
- Estimating variable effect
	- Calculate the probability of both 1 and 0 as dummy variables 
	- Subtract one from the other, the difference in probability is the overall effect
### Logit Regression Model
- Models the probability of Y=1 given x as the...
- **Cumulative standard logistic distribution function**
	- Evaluated at $z = β_0 +β_1X$
$Pr(Y = 1|X) = F(β_0 +β_1X)$
- Same as Probit with F instead of Φ
- Where F is the cumulative logistic distribution function:
$F(β_0 +β_1X)=\frac{1}{1+e^{-(β_0 +β_1X)}}$

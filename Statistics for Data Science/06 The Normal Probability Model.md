---
Title: The Normal Probability Model
Author: Jonathan De Los Santos
---
# 06 The Normal Probability Model

- Normal Random Variable
	- A continuous random variable whose probability distribution defines a standard bell-shaped curve
	- Defined by parameters μ and σ^2^ 
		- Mean locates the center
		- Variance controls the spread 
		- Variance is used rather than SD like discrete variables, to represent this difference the variance is usually written like '5^2^' rather than '25'
- **Standard Normal Distribution**
	- (μ = 0; σ^2^ = 1)
- Probabilities are areas under the curve 
	/Images/06_Area_under_curve.png
	- Probability of a single point is considered to be zero since continuous is only concerned with intervals
		- Therefore 0 < X < 1  is the same as 0 <= X <= 1
	- Normal distributions with different μ's
		- Shift the same distribution along x-axis by the amount change of µ
	- Normal distribution with different variances
			/Images/06_different_variances.png
		- "Spread" of the curve changes
- **Z-Score**
	- The number of standard deviations a data value is from the mean
	- $Z = \frac{X-\overline{X}}{S}$
	```{r}
	# Finding Z-Score
	
	gpa = c(3.2, 3.1, 2.8, 3.9, 3.2)
	salary = c(90000, 80000, 75000, 92000, 145000)
	# Scale displays Z-scores of each item
	scale(gpa)
	scale(salary)
	```

- **Standardizing** to find Normal Probabilities
	- Normally not needed due to lookup tables or software
	- Start by converting X into a z-score
		/Images/06_Standardizing_Example.png
	```{r}
	# Finding Probability of NRM
	
	# P(X>5000)
	mean = 4000
	sigma = 738
	
	# Use pnorm for continuous
	# pnorm is cumulative value that gives probabilty up to a point (x < point) 
	# We want greater than 5000, so 1-pnorm
	1 - pnorm(5000, mean, sigma)
	
	# You can also convert to z-score first
	z = (5000 - mean)/sigma
	1 - pnorm(z)
	```
	
- **Empirical Rule**
	/Images/06_Empirical_Rule.png	
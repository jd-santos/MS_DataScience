# 4-Interaction and Dummy Effects
## One Binary Variable
- Sometimes a regressor (X) is binary
	- Male/female
	- Control group/experimental group
- We can use dummy variables to represent them
	- Usually 0 and 1 
- However, $β_1$ doesn't make sense as 'slope' if X is binary
- $Y_i = β_0 + β_1X_i + u_i$, where X is binary (0 or 1)
	- When $X_i = 0$
		- $Y_i = β_0 + u_i$
		- Mean of $Y_i is β_0$
		- $Ε(\frac{Y_i}{X_i} = 0) = β_0$
	- When $X_i = 1$
		- $Y_i = β_0 + β_1 + u_i$
		- Mean of $Y_i is β_0 + β_1$
		- $Ε(\frac{Y_i}{X_i} = 1) = β_0 + β_1$
	- $β_1 = Ε(\frac{Y_i}{X_i} = 1) - Ε(\frac{Y_i}{X_i} = 0)$
		- Difference in group means between $X_i = 0$ and $X_i = 1$
- Logarathimic y
	- When log(y) is the dependent variable, the coefficient on the dummy variable can be multiplied by 100 to create the percentage difference in y c/p
## Two Binary Variables
- Independent
	- $Y_i = β_0 + β_1D_{1i} + β_2D_{2i}+u_i$
		- Where $D_{1i}$ and $D_{2i}$ are binary
	- $β_1$ is the effect of changing $D_1 = 0$ to $D_1 = 1$. this doesn't depend on the value of $D_2$
- Dependent
	- The variables interact with each other as well as the dependent variable 
	- $D_{1i}*D_{2i}$ is the "interaction" term and treated as its own regressor $β_3$
	- $Y_i = β_0 + β_1D_{1i} + β_2D_{2i}+β_3(D_{1i}*D_{2i})+u_i$
	- The effect of $D_1$ depends on $D_2$
	- $β_3$ increment of effect of $D_1$ when $D_2$ = 1
		- or to the effect of $D_2$ when $D_1$ = 1
	/Images/4.1-Two Binary Var Ex.png
## Binary and Continuous Variables
- $Y_i = β_0 + β_1X_i + β_2D_i+u_i$
	- $D_i$ is binary, X is continuous
- For effect of X to depend on D, we need another interaction term as regressor $β_3$ ($D_i*X_i$)
	- $Y_i = β_0 + β_1X_i + β_2D_i+ β_3(D_i*X_i) + u_i$
- If D = 0
	- $Y_i = β_0 + β_1X_i + u_i$
	- D = 0 regression line
	- $B_0$ is intercept and $B_1$ is slope
- If D = 1
	- $Y_i = β_0 + β_1X_i + β_2+ β_3X_i + u_i$
		 = $(β_0 + β_2) + (β_1+β_3)X_i + u_i$
		 - $(β_0 + β_2)$ is intercept
		 - $(β_1+β_3)X_i$ is slope
 /Images/4.2-Binary-Cont Graphs.png
## Excel
- Create new column for any categorical variables and transform to 0s and 1s
	- Can use if formula in excel:
		- =if(D5="Yes",1,0)
		- If yes, returns 1
		- If no, returs 0
- Data -> data analysis -> regression
	- Input dependent variable column
	- Input range of all independent variable columns
	- Get output, look for P-values below 0.05
- Output
	- Examine P-values of variables
	- Build equation with intercept and coefficients of variables
		- For dummy variables, the coefficient is "switched on" when the dummy = 1
		- If the dummy is zero, the coefficient has no effect
# Review of Prediction and Analytics
## Prediction Framework
- Dependent variable
	- In regression/prediction framework, the thing you want to predict is the 
	- Continuous 
		- E.g. price
	- Discrete
		- E.g. voting, yes or no
- Independent variable
	- What we want to base our prediction on 
	- We can use multiple independent variables to help predict dependent variable
		- As long as they have an effect on the outcome of our prediction
## Analytics
- Correlation
	- Quantifying relationships
	- Excel:
		- Simple option, use the formula:
			- `=correl(column1,column2)`
		- Better option, data analysis add-in:
			- Choose 'correlation' from the UI 
- Regression
	- Quantifying causality 
	- Need to be careful how you interpret these models
		- Which variable is affecting which? 
	- Regression analysis is available in Excel Data Analysis toolkit
		- Y-Range: dependent variable
		- X-Range: independent variable
- Correlation coefficient
	- Strength of relationship between two variables
		- Negative number: inverse relationship
		- Zero: no relationship
		- Positive number: positive relationship
	- If your independent variable increases by 1, what will be the effect on your dependent variable?
		- If coefficient = 0.7, dependent variable will increase by 0.7
	- Represented by *r* 
## Model Framework
### Moderating vs. Mediating Variables
- Mediating variable
	- A variable that accounts for the relation between one variable and another
	- The independent steps that link an independent variable to a dependent variable
- Moderating variable
	- Influence the *relationship* between an independent and dependent variable by increasing, decreasing, or sometimes reversing a relationship
	- Can sometimes confound research when these are unknown
- Extraneous variables
	- Not an intended part of the study 
	- Can affect the relationship without researchers knowning
	- Adds 'noise' to the relationship
	- Good research tries to account for these to isolate the independent variable
		- One method is to ensure that all extraneous variables are present while changing to the independent condition 
### Variable Observations
- Example: Husband and Wife height (see dataset)
- With only two variables there are still multiple relationships that could be occurring: 
	- Husband height affects wife height
	- Wife height affects husband height
	- Both heights affect each other (mutual dependency) 
	- There is no correlation between variables
- For three variables
	- Can require multiple regression model
	- A and B affect C
	- A affects B and C
	- A affects B, which then affects C
	- A affects C, B affects the *relationship*
		- In our example if A and C are husband and wife heights respectively, B might be the country 
	- Variables all affect each other (mutual dependency) 


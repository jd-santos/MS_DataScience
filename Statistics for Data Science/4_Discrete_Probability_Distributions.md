# 05_Discrete_Probability_Distributions
## Bernoulli Random Variable
- Bernoulli trials are random events with three characteristics:
	- Two possible outcomes (success or failure, 0 or 1, etc) 
	- Fixed probability of success for each outcome
	- Variables are independent
- Definition
	- A random variable *B* with two possible values 
	- 1 = success and 0 = failure
	- E(*B*)=p
		- Var(*B*)=p(1-p)
## Random Variables for Counts
- The sum of independent and identical-distribution (IID) Bernoulli random variables is *Y*
- *Y*
	- Number of successes in n Bernoulli trials
	- Defined by parameters (n) and (p)
		- Each trial (n) has probability of success (p)
- **Properties of Binomial Random Variables**
	- Mean and Variance
		- E(Y) = np
			- Number of trials * the probability of each trial
		- Var(Y) = np(1-p)
			- Variance of random variables p(1-p) times number of variables\
	- Consists of two parts:
		- The number of sequences that have *Y* successes in n attempts
		- The probability of a specific sequence of Bernoulli trials with *Y* success in n attempts
	- Binomial probability for *Y* success in n trials
		- P(*Y* = y)= nC~y~p^Y^(1-p)^n-y^
		- nC~y~: "n choose y"
			- Calculated (n!/(y!(n-y!))
		- Range of random variable *Y* is 0-n because you can have zero success to at most, n success


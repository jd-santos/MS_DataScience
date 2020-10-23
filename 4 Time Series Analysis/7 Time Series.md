# Time Series Data
## Overview
- Time series data are collected on the same observational unit/entity at multiple time periods
	- Evenly spaced numerical data
- Forecast based only on past values
	- Assumes that factors influencing the past, present, and future will continue 
- Scatter diagrams are heavily used 
- The time trajectory of a variable is produced by the interaction of four components 
### Four Components
- Trends (Secular)
	- The gradual, long-run evolution of variables
- Seasonal
	- A regular pattern of variability
- Cyclical
	- The time path of a series is sometimes influenced by cyclical forces
	- E.g. housing market declining in a recession 
- Irregular (White noise)
	- Unexpected, non-recurring factors that affect a series 
	- E.g. coronavirus 
## Forecasting
- Forecasting and estimation of causal effects are different objects
	- In forecasting, biased coefficients are less important and $R^2$ matters
- Utilizing the past behavior of a time series variable to predict the future behavior of the variable
	- Use the past values of Y to forecast $Y_t$
$\hat{Y}_{t+1} = f(Y_t, Y_{t-1}, Y_{t-2},...)$
	- t = time
- Ultimately we are trying to forecast a time series variable for which we already have prior year data
### Forecasting Evaluation Techniques
#### Mean Absolution Deviation (MAD)
$\sum\limits_{i=1}^n \frac{|Y_i - \hat{Y}_i|}{n}$
- Absolute deviation over observations
#### Mean Absolute Percent Error (MAPE) 
$\frac{100}{n}\sum\limits_{i=1}^n \frac{|Y_i - \hat{Y}_i|}{Y_i}$
- Same but percentage
#### Mean Square Error (MSE)
$\sum\limits_{i=1}^n \frac{(Y_i - \hat{Y}_i)^2}{n}$
- Actual value minus predicted value squared over the number of observations
- Similar to least square estimation
#### Root Mean Square Error (RMSE)
$\sqrt{MSE}$
- Usually most popular
## Time Series Techniques
- The components (trend, seasonal, cycles, random variation) can't always be easily identified 
- It is usually impossible to know which technique is best for a particular dataset
	- We may need to try several and select one that seems to work best 
### Moving Average
- Assigns equal weight to all previous observations
$\hat{Y}_{t+1} = \frac{Y_t + Y_{t-1} + Y_{t-k+1}}{k}$
- k = number of previous values we are averaging
	- We need to which k works best
- All observations have the same weight
### Weighted Moving Average
- Like moving average, but with different weights assigned to previous observations
- $\hat{Y}_{t+1} = w_1Y_t + w_2Y_{t-1} +...+w_kY_{t-k+1}$
> where $0 \leq w_i \leq 1$ and $\sum w_i = 1$
	- w = weight
	- Sum of weights must be equal to 1 
- We must determine values for k and the weights for a better model
### Exponential Smoothing
- Similar to weighted moving average, different weight can be assigned to previous observations
- $\hat{Y}_{t+1} = αY_t + α(1-α)Y_{t-1} + α(1-α)^2Y_{t-2}+...+ α(1-α)^nY_{t-n}$
	- $\hat{Y}_{t+1} = \hat{Y}_t = α(Y_t - \hat{Y}_t)$
	- where $0 \leq α \leq 1$
### Autoregression (AR) Model
- Using simple regression model where $Y_t$ is regressed against its own lagged values
- **Order of the autogregression** 
	- The number of lags used as regressors 
- First order autoregression 
	- AR(1): $Y_t = β_0 + β_1Y_{t-1} +u_t$
- Pth order
	- AR(p): $Y_t = β_0 + β_1Y_{t-1} +...+ β_pY_{t-p} + u_t$
#### Autoregressive Distirubte Lag Model (ADL)
- We can add more variables (X) that may be predictors of Y in addition to lagged values
- Autogressive distributed lag model with p lags of Y and r lags of X, ADL (p,r)
-  $Y_t = β_0 + β_1Y_{t-1} +...+ β_pY_{t-p} + δ_1Χ_{t-1} + ... + δ_rΧ_{t-r} + u_t$
### Techniques in Excel
#### Moving Average and Mean Absolute Deviation
/Images/7.0_Excel_1.png
#### Root Mean Square Issue
/Images/7.1_Excel_RMSE.png
#### Weighted Moving Average
/Images/7.2_Excel_Weighted-MA.png
#### Exponential Smoothing
/Images/7.3_Excel_Exp-Smoothing.png
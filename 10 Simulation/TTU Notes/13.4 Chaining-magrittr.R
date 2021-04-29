

library(simmer)

library(magrittr)

# We run functions inside of each other
sqrt(sum(16,9))
# With Chaining
sum(16, 9) %>%
  sqrt()

# Another example
set.seed(123)
# We run functions inside of each other
mean( rnorm( sample(100:200, size = 10000, replace = T) , 0, 1) )

# With Chaining
set.seed(123)
sample(100:200, size = 10000, replace = T) %>%
rnorm(0, 1) %>%
mean()

# The shortcut for chaining is CTRL + SHIFT + M 
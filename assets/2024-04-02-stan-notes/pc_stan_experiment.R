library(tidyverse)

simulate_Q_once <- function(alpha, mu1, mu2, sd1, sd2) {
  
  # Step 1: Generate X1 and X2
  
  X1 <- rnorm(1, mean = mu1, sd = sd1)
  X2 <- rnorm(1, mean = mu2, sd = sd2)
  
  # Step 2: Generate R_i from a Bernoulli distribution with probability alpha
  
  R <- rbinom(1, size = 1, prob = alpha)
  
  # Step 3: Generate L_i from a Bernoulli distribution with probability 0.5
  
  L <- rbinom(1, size = 1, prob = 0.5)
  
  # Step 4: Compute F_i
  
  Q <- R*pmin(X1, X2)+(1-R)*(L*X1+(1 - L)*X2)
  
  return(Q)
  
}


# Initialize a data frame to store the results
results <- data.frame(Q = numeric(), Alpha = factor())

# Define the alpha values and number of simulations
alpha_values <- c(0.25, 0.5, 0.75)
n_simulations <- 5000

# Perform simulations
for (alpha in alpha_values) {
  for (i in 1:n_simulations) {
    Q_draw <- simulate_Q_once(alpha, mu1=15, mu2=20, sd1=3, sd2=3)
    results <- rbind(results, data.frame(Q = Q_draw, Alpha = as.factor(alpha)))
  }
}

# Plotting the results using ggplot2
ggplot(results, aes(x = Q, fill = Alpha)) +
  geom_density(alpha = 0.4) +
  labs(title = "Distribution of Q for Different Values of Alpha (Rate of Price Comparison)",
       x = "Q (Observed Price)",
       y = "Density") +
  scale_fill_manual(values = c("0.25" = "blue", "0.5" = "red", "0.75" = "green"),
                    name = "Alpha") +
  theme_minimal() -> g

ggsave(g, path="~/Documents/Research/fossj117.github.io/figs/2024-04-02-stan-notes/dist.png")

library(knitr)

# Calculate mean and SD for each alpha
summary_stats <- results %>%
  group_by(Alpha) %>%
  summarise(
    Mean = mean(F),
    SD = sd(F)
  )

# Print summary statistics to check
print(summary_stats)

# Convert to HTML table
html_table <- kable(summary_stats, format = "html", digits = 3, caption = "Mean and SD of F for Each Alpha")

# To display in R Markdown or an R environment that supports HTML output
html_table

### Simulate to get E[min(X_1, X_2)]

X1 <- rnorm(10000, mean = 15, sd = 3)
X2 <- rnorm(10000, mean = 20, sd = 3)
exp_the_min <- mean(pmin(X1, X2)) #14.77504
exp_Q <- results %>% filter(Alpha=="0.75") %>% select(Q) %>% colMeans()
mu_bar <- (20+15)/2

alpha_est <- (exp_Q-mu_bar)/(exp_the_min-mu_bar)

library(rstan)
library(bayesplot)

(results %>% filter(Alpha == "0.25"))$Q -> Q25
(results %>% filter(Alpha == "0.5"))$Q -> Q50
(results %>% filter(Alpha == "0.75"))$Q -> Q75

fit25 <- stan(
  file = "~/Documents/Research/fossj117.github.io/assets/2024-04-02-stan-notes/model.stan",  # Path to your Stan model file
  data = list(N=5000, Q=Q25),
  chains = 4,
  iter = 2000,
  warmup = 500,
  seed = 1234, 
  control=list(adapt_delta=0.99), 
  cores = 4
)

fit50 <- stan(
  file = "~/Documents/Research/fossj117.github.io/assets/2024-04-02-stan-notes/model.stan",  # Path to your Stan model file
  data = list(N=5000, Q=Q50),
  chains = 4,
  iter = 2000,
  warmup = 500,
  seed = 1234, 
  control=list(adapt_delta=0.99), 
  cores=4
)

fit75 <- stan(
  file = "~/Documents/Research/fossj117.github.io/assets/2024-04-02-stan-notes/model.stan",  # Path to your Stan model file
  data = list(N=5000, Q=Q75),
  chains = 4,
  iter = 2000,
  warmup = 500,
  seed = 1234, 
  control=list(adapt_delta=0.99), 
  cores=4
)

# Check fits
check_all_diagnostics(fit25)
check_all_diagnostics(fit50)
check_all_diagnostics(fit75)

fit_to_df <- function(fitobj, name){
  alphas <- extract(fitobj)$alpha 
  new_df <- data.frame(alpha = alphas, name = name)
  return(new_df)
}

alphas25 <- fit_to_df(fit25, "25")
alphas50 <- fit_to_df(fit50, "50")
alphas75 <- fit_to_df(fit75, "75")

all_alphas <- rbind(alphas25, alphas50, alphas75)

vlines_data <- data.frame(
  name = c("25", "50", "75"),
  xintercept = c(0.25, 0.5, 0.75)
)

all_alphas %>% 
  ggplot(aes(x=alpha)) + geom_histogram(bins=100) + facet_grid(name~.) + theme_bw() + 
  xlab("Alpha") + 
  ylab("Count") + 
  ggtitle("Posterior Alphas from Stan MCMC Runs on Simulated Data") + 
  geom_vline(data = vlines_data, aes(xintercept = xintercept), color = "red", linetype = "dashed", lineweight=1.2)

all_alphas %>% 
  group_by(name) %>% 
  summarise(
    mean = mean(alpha)
  , q025 = quantile(alpha, 0.025)
  , q975 = quantile(alpha, 0.975)
  ) -> means_cred_int

html_table2 <- kable(means_cred_int, col.names = c("True Alpha", "Posterior Mean", "95% CI lower", "95% CI upper"), format = "html", digits = 3, caption = "Means and Credible Intervals")

# To display in R Markdown or an R environment that supports HTML output
html_table2


## Simulate other draws from mu and sigma. 

mu1<-15 
mu2<-20 
sd1<-3 
sd2<-3

X1s <- rnorm(1000, mean = mu1, sd = sd1)
X2s <- rnorm(1000, mean = mu2, sd = sd2)

fit25_normals <- stan(
  file = "~/Documents/Research/fossj117.github.io/assets/2024-04-02-stan-notes/model_normals.stan", 
  data = list(N=5000, Q=Q25, K=1000, X1=X1s, X2=X2s),
  chains = 4,
  iter = 2000,
  warmup = 500,
  seed = 1234, 
  control=list(adapt_delta=0.99), 
  cores = 4
)

check_all_diagnostics(fit25_normals)

print(fit25_normals)


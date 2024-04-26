library(tidyverse)
library(knitr)

# Setup
n_sims <- 10000

get_i_thresh <- function(n_sims, sigma_d, beta) {
  
  e_0 <- runif(n_sims)
  e_1 <- runif(n_sims)
  
  d_0 <- rnorm(n = n_sims, mean = 0, sd = sigma_d)
  d_1 <- rnorm(n = n_sims, mean = 0, sd = sigma_d)
  
  i_thresh <- pmin(pmax((beta + e_0 + d_0 - (e_1 + d_1))/(2*beta), 0), 1)
  
  return(i_thresh)
}

beta_vals <- c(1)
sigma_d_vals <- seq(0, 1.5, 0.5)

results <- expand.grid(sigma_d = sigma_d_vals, beta = beta_vals, stringsAsFactors = FALSE)
results$i_thresh <- mapply(get_i_thresh, n_sims, results$sigma_d, results$beta, SIMPLIFY = FALSE)

results_long <- results %>%
  mutate(id = row_number()) %>%
  unnest(i_thresh) %>%
  rename(i_thresh_value = i_thresh) %>%
  group_by(sigma_d, beta) %>%
  mutate(mean_i_thresh = mean(i_thresh_value))

results_long %>% 
  ggplot(aes(x=i_thresh_value)) + 
  geom_histogram(bins = 30) +
  facet_grid(factor(sigma_d, labels = paste("Sigma:", sigma_d_vals))~.,
             scales = "free") +
  theme_bw(base_size = 20) +
  labs(title = "Distribution of i threshold for recommending c_1", 
       subtitle = "Viewers greather than thresholed get c_1; Fixing beta=1; 10000 simulations", 
       x = "Threshold Value (for recommending c_1)",
       y = "Frequency")


## 2 dimensional

# Simulate a range of sigma_d values and beta values
sigma_d_vals <- seq(0, 0.5, 0.1)
beta_vals <- seq(0, 1, 0.25)

# Create a data frame to store the results
results <- expand.grid(sigma_d = sigma_d_vals, beta = beta_vals, stringsAsFactors = FALSE)

# Apply the function for each combination of sigma and beta and store the results
results$i_thresh <- mapply(get_i_thresh, n_sims, results$sigma_d, results$beta, SIMPLIFY = FALSE)

results_long <- results %>%
  mutate(id = row_number()) %>%
  unnest(i_thresh) %>%
  rename(i_thresh_value = i_thresh) %>%
  group_by(sigma_d, beta) %>%
  mutate(mean_i_thresh = mean(i_thresh_value))

results_long %>% 
  ggplot(aes(x=i_thresh_value)) + 
  geom_histogram(bins = 30, fill = "blue", color = "black") +
  geom_text(aes(label = sprintf("Mean: %.2f", mean_i_thresh), y = Inf, x = Inf), 
            vjust = 1.5, hjust = 1.5, size = 3.5, color = "red") +
  facet_grid(vars(factor(sigma_d, labels = paste("Sigma:", sigma_d_vals))), 
             vars(factor(beta, labels = paste("Beta:", beta_vals))), 
             scales = "free") +
  theme_bw() +
  labs(title = "Distribution of i_thresh for various sigma_d and beta",
       x = "i_thresh value",
       y = "Frequency")


# Next step

run_simulation <- function(n_sims, sigma_d, beta) {
  
  e_0 <- runif(n_sims)*3
  e_1 <- runif(n_sims)*3
  
  d_0 <- rnorm(n = n_sims, mean = 0, sd = sigma_d)
  d_1 <- rnorm(n = n_sims, mean = 0, sd = sigma_d)
  
  # Above this threshold, you get c1
  i_thresh <- pmin(pmax((beta + e_0 + d_0 - (e_1 + d_1))/(2*beta), 0), 1)
  i_1_watch<-1-sqrt(e_1/beta) # above this, watch 1
  i_0_watch<-sqrt(e_0/beta) # below this, watch 0

  share_watch_1 <- 1-pmax(i_1_watch, i_thresh)
  share_watch_0 <- pmin(i_0_watch, i_thresh)
  share_watch_none <- 1-share_watch_1-share_watch_0
  
  return(data.frame(i_thresh, i_1_watch, i_0_watch, share_watch_1, share_watch_0, share_watch_none, sigma_d, beta))
}

results <- rbind(run_simulation(10000, sigma_d = 0, beta=1), 
                 run_simulation(10000, sigma_d = .5, beta=1), 
                 run_simulation(10000, sigma_d = 1, beta=1), 
                 run_simulation(10000, sigma_d = 1.5, beta=1))

results %>% 
  mutate(share_watch = 1 - share_watch_none) %>% 
  ggplot(aes(x=share_watch)) + 
  geom_histogram() + 
  facet_grid(.~sigma_d) + theme_bw(base_size = 14) + 
  xlab("Share that watch anything (Platform welfare)") + 
  ylab("Share in Facet") + 
  ggtitle("Distribution of Platform Welfare (by sigma_delta = prediction quality)")

results %>% 
  ggplot(aes(x=share_watch_1)) + 
  geom_histogram() + 
  facet_grid(.~sigma_d) + theme_bw(base_size = 14) + 
  xlab("Share that watch 1") + 
  ggtitle("Distribution of Creator 1 welfare (by sigma_delta = prediction quality)")

results %>% 
  mutate(share_watch = 1 - share_watch_none) %>% 
  group_by(sigma_d) %>% 
  summarise(
    mean_creator1 = mean(share_watch_1)
    , sd_creator1 = sd(share_watch_1)
    , mean_plat = mean(share_watch)
    , sd_plat = sd(share_watch)
  ) %>% kable(digits = 2, caption = "Mean and SD creator and platform welfare by sigma_delta", col.names = c("Sigma", "Mean Creator", "SD Creator", "Mean Platform", "SD Platform"))


results <- rbind(run_simulation(10000, sigma_d = 0, beta=2), 
                 run_simulation(10000, sigma_d = .5, beta=2), 
                 run_simulation(10000, sigma_d = 1, beta=2), 
                 run_simulation(10000, sigma_d = 1.5, beta=2))

results %>% 
  mutate(share_watch = 1 - share_watch_none) %>% 
  ggplot(aes(x=share_watch)) + 
  geom_histogram() + 
  facet_grid(.~sigma_d) + theme_bw(base_size = 14) + 
  xlab("Share that watch anything (Platform welfare)") + 
  ylab("Share in Facet") + 
  ggtitle("Distribution of Platform Welfare (by sigma_delta = prediction quality)")

results %>% 
  ggplot(aes(x=share_watch_1)) + 
  geom_histogram() + 
  facet_grid(.~sigma_d) + theme_bw(base_size = 14) + 
  xlab("Share that watch 1") + 
  ggtitle("Distribution of Creator 1 welfare (by sigma_delta = prediction quality)")

results %>% 
  mutate(share_watch = 1 - share_watch_none) %>% 
  group_by(sigma_d) %>% 
  summarise(
    mean_creator1 = mean(share_watch_1)
    , sd_creator1 = sd(share_watch_1)
    , mean_plat = mean(share_watch)
    , sd_plat = sd(share_watch)
  ) %>% kable(digits = 2, caption = "Mean and SD creator and platform welfare by sigma_delta", col.names = c("Sigma", "Mean Creator", "SD Creator", "Mean Platform", "SD Platform"))

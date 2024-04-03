functions {
  // Log likelihood for the given complex density function
  real complex_log_likelihood(real q, real alpha, real mu1, real mu2, real sigma1, real sigma2) {

    real log_pdf_1 = normal_lpdf(q | mu1, sigma1);
    real log_pdf_2 = normal_lpdf(q | mu2, sigma2);
    real log_cdf_1 = normal_lcdf(q | mu1, sigma1);
    real log_cdf_2 = normal_lcdf(q | mu2, sigma2);

    // precompute some things
    real log_alpha = log(alpha);
    real log_one_minus_alpha = log(1-alpha);
    real log_f1q_plus_f2q = log_sum_exp(log_pdf_1, log_pdf_2);

    real log_fm_q = log(
        exp(log_pdf_1) + exp(log_pdf_2) - (exp(log_pdf_1)*exp(log_cdf_2) + exp(log_pdf_2)*exp(log_cdf_1))
    );

    real final = log_sum_exp(
        log_alpha + log_fm_q, log_one_minus_alpha - log(2) + log_f1q_plus_f2q
    );

    return(final);
  }
}
data{
    int<lower=0> N; // Number of observations
    vector[N] Q; // Observed prices
}
model {
  // Empty model block
}
generated quantities {

    real mu1=15;
    real mu2=20;
    real sigma1=3;
    real sigma2=3;
    real alpha_step = 0.1;

    for(j in 1:10){
        real alpha = j*alpha_step;
        real ll = 0;
        for (i in 1:N) {
            ll += complex_log_likelihood(Q[i],alpha, mu1, mu2, sigma1, sigma2);
        }
        print("alpha = ", alpha, ", sum of complex_log_likelihoods = ", ll);
    }
}
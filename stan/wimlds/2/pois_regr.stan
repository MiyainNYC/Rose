data {
int<lower = 1> N;
int<lower = 1> M;
matrix[M,N] X;
real y[N];
}

parameters {
vector[M] beta;
real alpha;
}

model {
beta[1] ~ normal(0,10);
beta[2] ~ normal(0,0.005);
beta[3] ~ normal(0,);
alpha ~ #;
k ~ poisson_log(X' * beta +alpha);
}


generated quantities {
real k_ppc[N];
{
vector[N] mu = X' * beta +alpha;
for (n in 1:N){
if (mu[n] >20){
print('Poisson rate saturated!');
mu[n]=20;
}
k_ppc [n] = poisson_log_rng(mu[n]);
}
}
}
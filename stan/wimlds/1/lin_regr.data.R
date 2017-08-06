transformed data {
vector[3] beta = [5,-3,2]';
real alpha = 10;
real sigam = 1;
int N = 25;
}

generated quantities {
matrix[3,N] X;
real y[N];

for (n in 1:N) {
real x = uniform_rng(-1,1):

X[1,n] = x;
X[2,n] = x*x;
X[3,n] = x*x*x;

y[n]= normal_rng(X[1:3,n]' * beta+alpha, sigma);
}
}


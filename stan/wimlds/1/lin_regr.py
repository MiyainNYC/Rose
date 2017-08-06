import pystan
import stan_utility
import matplotlib
import matplotlib.pyplot as plot

##################################################
##### Simulate data and write to file
##################################################

model = stan_utility.compile_model('gen_data.stan')
fit = model.sampling(seed=194838, algorithm='Fixed_param', iter=1, chains=1,n_jobs=1)

data = dict(N = 25, M = 3,
            X=fit.extract()['X'][0,:,:], y = fit.extract()['y'][0,:])

pystan.stan_rdump(data, 'lin_regr.data.R')

##################################################
##### Fit model and check diagnostics
##################################################

# Read in data from Rdump file
data = pystan.read_rdump('lin_regr.data.R')

# Fit posterior with Stan
model = stan_utility.compile_model('lin_regr.stan')
fit = model.sampling(data=data, seed=194838,n_jobs=1)

# Check sampler diagnostics
print(fit)

sampler_params = fit.get_sampler_params(inc_warmup=False)
stan_utility.check_div(sampler_params)
stan_utility.check_treedepth(sampler_params)
stan_utility.check_energy(sampler_params)

# Check visual diagnostics
fit.plot()
plot.show()

##################################################
##### Visualize posterior
##################################################

light="#DCBCBC"
light_highlight="#C79999"
mid="#B97C7C"
mid_highlight="#A25050"
dark="#8F2727"
dark_highlight="#7C0000"

# Plot parameter posteriors
params = fit.extract()

f, axarr = plot.subplots(2, 3)
for a in axarr[0,:]:
    a.xaxis.set_ticks_position('bottom')
    a.yaxis.set_ticks_position('none')
for a in axarr[1,:]:
    a.xaxis.set_ticks_position('bottom')
    a.yaxis.set_ticks_position('none')

axarr[0, 0].set_title("beta_1")
axarr[0, 0].hist(params['beta'][:,0], bins = 25, color = dark, ec = dark_highlight)
axarr[0, 0].axvline(x=5, linewidth=2, color=light)

axarr[0, 1].set_title("beta_2")
axarr[0, 1].hist(params['beta'][:,1], bins = 25, color = dark, ec = dark_highlight)
axarr[0, 1].axvline(x=-3, linewidth=2, color=light)

axarr[0, 2].set_title("beta_3")
axarr[0, 2].hist(params['beta'][:,2], bins = 25, color = dark, ec = dark_highlight)
axarr[0, 2].axvline(x=2, linewidth=2, color=light)

axarr[1, 0].set_title("alpha")
axarr[1, 0].hist(params['alpha'], bins = 25, color = dark, ec = dark_highlight)
axarr[1, 0].axvline(x=10, linewidth=2, color=light)

axarr[1, 1].set_title("sigma")
axarr[1, 1].hist(params['sigma'], bins = 25, color = dark, ec = dark_highlight)
axarr[1, 1].axvline(x=1, linewidth=2, color=light)

plot.show()

# Perform a posterior predictive check by plotting
# posterior predictive distributions against data
f, axarr = plot.subplots(2, 2)
for a in axarr[0,:]:
    a.xaxis.set_ticks_position('bottom')
    a.yaxis.set_ticks_position('none')
for a in axarr[1,:]:
    a.xaxis.set_ticks_position('bottom')
    a.yaxis.set_ticks_position('none')

axarr[0, 0].set_title("y_1")
axarr[0, 0].hist(params['y_ppc'][:,0], bins = 25, color = dark, ec = dark_highlight)
axarr[0, 0].axvline(x=data['y'][0], linewidth=2, color=light)

axarr[0, 1].set_title("y_5")
axarr[0, 1].hist(params['y_ppc'][:,4], bins = 25, color = dark, ec = dark_highlight)
axarr[0, 1].axvline(x=data['y'][4], linewidth=2, color=light)

axarr[1, 0].set_title("y_10")
axarr[1, 0].hist(params['y_ppc'][:,9], bins = 25, color = dark, ec = dark_highlight)
axarr[1, 0].axvline(x=data['y'][9], linewidth=2, color=light)

axarr[1, 1].set_title("y_15")
axarr[1, 1].hist(params['y_ppc'][:,14], bins = 25, color = dark, ec = dark_highlight)
axarr[1, 1].axvline(x=data['y'][14], linewidth=2, color=light)

plot.show()

# Assumes fit output from Stan

##################################################
##### Plot divergent and non-divergent iterations
##################################################

fit = model.sampling(data=data, seed=194838)

nondiv_params, div_params = stan_utility.partition_div(fit)

light="#DCBCBC"
light_highlight="#C79999"
mid="#B97C7C"
mid_highlight="#A25050"
dark="#8F2727"
dark_highlight="#7C0000"
green="#00FF00"

plot.gca().set_xlabel("name1")
plot.gca().set_ylabel("name2")
plot.scatter(nondiv_params['name1'], nondiv_params['name2'], color = mid_highlight, alpha=0.1)
plot.scatter(div_params['name1'], div_params['name2'], color = green, alpha=0.5)
plot.show()

##################################################
##### Plot GP posterior predictive quantiles
##################################################

data = pystan.read_rdump('gp_regr.data.R')
params = fit.extract()

N = data['N']
N_test = data['N_test']

cmap = matplotlib.cm.get_cmap('Reds')
I = len(params['f'])
buff = 0.25 * I

x = data['x']
x_test = data['x_test']
x_cat = [None] * (N + N_test)
for n in range(N):
    x_cat[2 * n] = x[n]

for n in range(N_test):
    x_cat[2 * n + 1] = x_test[n]

Q = [ [None] * (N + N_test) for l in xrange(9)]
P = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for n in range(N + N_test):
    if n % 2 == 0:
        idx = n / 2
        y_ppc = [ y_ppc[idx] for y_ppc in params['y_ppc'] ]
        for m in range(9):
            Q[m][n] = numpy.percentile(y_ppc, P[m])
    else:
        idx = (n - 1) / 2
        y_ppc = [ y_ppc[idx] for y_ppc in params['y_test_ppc'] ]
        for m in range(9):
            Q[m][n] = numpy.percentile(y_ppc, P[m])

plot.fill_between(x_cat, Q[0], Q[8], facecolor=light, color=light)
plot.fill_between(x_cat, Q[1], Q[7], facecolor=light_highlight, color=light_highlight)
plot.fill_between(x_cat, Q[2], Q[6], facecolor=mid, color=mid)
plot.fill_between(x_cat, Q[3], Q[5], facecolor=mid_highlight, color=mid_highlight)
plot.plot(x_cat, Q[4], color=dark)

plot.scatter(data['x'], data['y'], color = "white", s=40, zorder = 3)
plot.scatter(data['x'], data['y'], color = "black", zorder = 4)

plot.scatter(data['x_test'], data['y_test'], color = "white", s=40, zorder = 3)
plot.scatter(data['x_test'], data['y_test'], color = "blue", zorder = 4)

plot.gca().set_xlim([-10, 10])
plot.gca().set_xlabel("x")
plot.gca().set_ylim([-5, 10])
plot.gca().set_ylabel("y")
plot.show()

##################################################
##### Plot realizations of posterior predictive GP
##################################################

for i in range(I):
    y = params['y_ppc'][i]
    y_test = params['y_test_ppc'][i]
    y_cat = [None] * (N + N_test)
    for n in range(N):
        y_cat[2 * n] = y[n]
    for n in range(N_test):
        y_cat[2 * n + 1] = y_test[n]
    plot.plot(x_cat, y_cat, color = cmap((i + buff) / (I + 2 * buff)))

plot.scatter(data['x'], data['y'], color = "white", s=40, zorder = 3)
plot.scatter(data['x'], data['y'], color = "black", zorder = 4)

plot.scatter(data['x_test'], data['y_test'], color = "white", s=40, zorder = 3)
plot.scatter(data['x_test'], data['y_test'], color = "blue", zorder = 4)

plot.gca().set_xlim([-10, 10])
plot.gca().set_xlabel("x")
plot.gca().set_ylim([-5, 10])
plot.gca().set_ylabel("y")

plot.show()

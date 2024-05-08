import pyro
import pyro.distributions as dist

def conditioned_scale_file(obs, guess=8.5): 
    weight = pyro.sample("weight", dist.Normal(guess, 1.))
    measurement = pyro.sample("measurement", dist.Normal(weight, 1.), obs=obs)
    return measurement

def eight_school_file(J, sigma, y=None):
    mu = pyro.sample('mu', dist.Normal(0, 5))
    tau = pyro.sample('tau', dist.HalfCauchy(5))
    with pyro.plate('J', J):
        theta = pyro.sample('theta', dist.Normal(mu, tau))
        pyro.sample('obs', dist.Normal(theta, sigma), obs=y)


def eight_schools_noncentered_file(J, sigma, y=None):
    mu = pyro.sample('mu', dist.Normal(0, 5))
    tau = pyro.sample('tau', dist.HalfCauchy(5))
    with pyro.plate('J', J):
        nu = pyro.sample('nu', dist.Normal(0., 1.))
        theta = mu + tau * nu
        pyro.sample('obs', dist.Normal(theta, sigma), obs=y)


def hmm_file(weather_seq, clothes_seq, n_weather_cat, transition_prior, emission_prior, n_data_observations):
    # independent draws
    with pyro.plate("prob_plate", n_weather_cat):
        transition_prob = pyro.sample("transition_prob", dist.Dirichlet(transition_prior))
        emission_prob = pyro.sample("emission_prob", dist.Dirichlet(emission_prior))

    # start with first weather category
    weather_cat = weather_seq[0] 
    
    # evolve in time
    for t in range(n_data_observations):
        if t > 0:
            weather_cat = pyro.sample("weather_{}".format(t), 
                                   dist.Categorical(transition_prob[weather_cat]),
                                   obs=weather_seq[t])
        pyro.sample("clothes_{}".format(t), 
                    dist.Categorical(emission_prob[weather_cat]), 
                    obs=clothes_seq[t])
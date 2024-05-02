import pyro
import pyro.distributions as dist

def conditioned_scale_file(obs, guess=8.5): 
    weight = pyro.sample("weight", dist.Normal(guess, 1.))
    measurement = pyro.sample("measurement", dist.Normal(weight, 1.), obs=obs)
    return measurement

def eight_school_file(J, sigma, y=None):
    #to do: implement the model
    return


def eight_schools_noncentered_file(J, sigma, y=None):
    #to do: implement the model
    return


def hmm_file(weather_seq, clothes_seq, n_weather_cat, transition_prior, emission_prior, n_data_observations):
    # independent draws
    with pyro.plate("prob_plate", n_weather_cat):
        transition_prob = pyro.sample("transition_prob", dist.Dirichlet(transition_prior))
        emission_prob = pyro.sample("emission_prob", dist.Dirichlet(emission_prior))

    # start with first weather category
    weather_cat = weather_seq[0] 
    
    # evolve in time
    #to do
    return
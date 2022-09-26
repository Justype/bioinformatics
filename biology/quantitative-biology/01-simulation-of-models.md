# Intro to Simulation of Models

## Characters of Biological Data

- scales vary dramatically: 1 nm to 1 km, 1 ms to 1 year
- multi scale modeling
  - mutation in viral genome => change of prevalence

**focus on the mathematical concepts**

1. can be used into different scales
2. data can be interpreted by different methods

# Ordinary Differential Equations (ODE)

常微分方程

ODE is an equation that describes the rate of change(**derivative** 导数) of a quantity using a mathematical equations.

Usage in Biology:

1. to specify different hypotheses (often mutually exclusive) and then explore the possible emerging behaviors
2. to test if our model is consistent with the data

get the derivative of x(t)

$\frac{d}{dt}x(t) = f(x(t))$
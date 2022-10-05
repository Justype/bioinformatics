# Statistical Distribution

| Distribution      | Use Case                                          |
| :---------------- | :------------------------------------------------ |
| Binomial          | x over n trials **with** replacement              |
| Normal            |                                                   |
| Poisson           |                                                   |
| Hypergeometric    | x over n **without** replacement                  |
| Geometric         | Number of failure in Bernoulli before success     |
| Negative Binomial | Probability of x failures before the r th success |

| R Command | Usage                                         |
| :-------- | :-------------------------------------------- |
| dXXX      | **density** (height) of distribution at x     |
| pXXX      | **cumulative density** of distribution at x   |
| qXXX      | **quantile** of x in the defined distribution |
| rXXX      | generate random numbers from a distribution   |

- with replacement 放回
- without 不放回

## Discrete or Continuous

## Distributions

### Bernoulli Distribution

- Probability of success for a single binary trial ( the output is binary)
- π = probability of success, x = number of times you want x to occur, in this case 1 or 0.

$$
f(x) = \pi ^x (1-\pi)^{1-x} \ \ x=1\ or\ 2
$$

### Binomial Distribution

- a combination of Bernoulli trials that are independent and identically distributed

$$
f(x) = \begin{pmatrix} n \\ x \end{pmatrix}
\pi ^x (1-\pi)^{n-x}
$$

### Uniform Distribution

- The probability is the same no matter what value.
- a is the lower limit and b is the upper.

$$f(x) = \frac{1}{{b-a}'}$$

### Normal Distribution

- The expected value is the average
- The function is symmetric around the mean
- Produces output that is continuous and independent.
- Two parameters: 
  - 𝜇 = mean
  - 𝜎 = standard deviation ( square root of variance)

$$X \sim \mathcal{N}(\mu,\,\sigma^{2})$$

$$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac12(\frac{x-\mu}{\sigma})^2}$$

### Poisson Distribution

[CUHK Poisson](http://www.obg.cuhk.edu.hk/ResearchSupport/StatTools/Poisson_Exp.php)

[Deduction Binomial => Poisson](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/poisson-distribution/v/poisson-process-1)

- Similar to binomial distribution
- Counts the number of successes in a trial
- But no limit on number of successes since it is over time or space.
- If n is large and p is low, 
- approximates binomial.
- One parameter λ (lambda)
- which is mean and variance

- E(X) = λ

$$ f(x) = \frac{e^\lambda \lambda^x}{x!} $$

### Hypergeometric Distribution

- Probability of x successes over n trials without replacement.
- Binomial is with replacement.
- n is the number of trials
- M is the number of items of group of interest
- N is the number of items selected

$$
f(x) =\frac{
    \begin{pmatrix} M \\ x \end{pmatrix}
    \begin{pmatrix} N-M \\ n-x \end{pmatrix}
}
{
    \begin{pmatrix} M \\ x \end{pmatrix}
}
$$

### Geometric Distribution

Number of failure in Bernoulli trial before success.

$$f(x)=\pi(1-\pi)^x$$

### Negative Binomial Distribution

- Probability of x Bernoulli failures before the rth success.
- used in RNA seq

$$
f(x)=\begin{pmatrix}
    x+r-1\\
    r-1
\end{pmatrix}
\pi^r(1-\pi)^x
$$

## R commands for distribution

- rbinom: generate random numbers from a binomial distribution
- dbinom: density (height) of distribution at x
- pbinom: cumulative density of distribution at x
- qbinom: quantile of x in the defined distribution

My Understanding

- dnorm: get the y by the x ?
- pnorm: get the area by the x
- qnorm: get the x by the quantile
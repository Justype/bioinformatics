# Parameters and Statistics

|                    |                           |
| :----------------- | :------------------------ |
| Expectation        |                           |
| Variance           |                           |
| Standard Deviation | $ SD(X) = \sqrt{Var(X)} $ |

Standard Error? Sampling Distribution

## Expected Value

$$
E(X) = \sum_x xf(x)
$$

$$
E(X) = \int_{-\infin}^\infin xf(x)dx
$$

## Variance and Standard Deviation

Variance quantifies the amount of dispersion of the data.

$$
Var(X) = E[X-E(X)]^2
$$

Standard deviation is the square root of variance

$$
SD(X) = \sqrt{Var(X)}
$$

## Statical Analysis

- You cannot get the exact statical value of a large population

## Estimators

### Arithmetic Mean

算数平均数

$$
\overline{X} = \frac{\sum _{i=1}^{n}X_i}{n} 
$$

### Geometric Mean

几何平均数

$$
GM = \sqrt{\prod _{i=1}^{n}X_i}
$$

### Harmonic Mean

调和平均数

### Trimmed Mean

- Cut off the outliers

### Mode

众数


### Median

中位数


## Sample Variance

The sum of squared deviations divided by n-1.

$$
S^2 = \frac{\sum_{i=1}^n(x_i-\overline{X})^2}{n-1}
= \frac{\sum_{i=1}^n x_i^2 -n\overline{X}^2}{n-1}
$$

- The n-1 is for degrees of freedom. It provides the number of independent variables that are able to estimate the parameter. 
- It’s -1 because we know the mean of the sample.

- The more n is, the more correct the estimated value is.

### Sample coefficient of variation

It is simply scaling standard deviation by dividing it with the arithmetic mean

$$\frac{SD(X)}{E(X)}$$

Compare different methods

### Interquartile range IQR

First and third quartile are 25% and 75% of the values sorted.

numbers out this range are outliers

NOTE: There are several ways to calculate quartile. (you must specify it in R, default if type=7)

# Sample Distribution


## Standard error

标准误

The standard deviation of the sampling distribution is called the standard error

Since standard deviation is square root of variance, the standard error is standard deviation of sampling distribution divided by square root of n

## Central Limit Theorem

There are two main statements:
- If the parent distribution is normal with mean 𝜇 and variance 𝜎2 then sample distribution is normal with mean 𝜇 and variance 𝜎2 over n
- Regardless of what the original distribution is, as n gets large, the sample distribution will become normal.
- A sample size of 30 is usually considered as cutoff.

## Other Distributions

- The sampling distribution of the population variance is a 𝝌2 distribution.
- The **ratio of two variance** from two population is an F distribution.
- A t-distribution is created using a t-statistic which is the difference between the sample mean and population mean divided by the the standard error.
- These will all serve important when we start working with null hypothesis in the next chapter.

F distribution (compare any other distributions)

## Confidence Intervals

95% will fall in this range

Confidence intervals provide a range where if the population was to be sampled, it’s mean will be present X% of the time. The most common values used for X is 95%.

Confidence intervals do NOT represent the probability that the mean is within the range.



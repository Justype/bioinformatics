# Hypothesis Testing

## Null Hypothesis

The null hypothesis (Ho) is often the statement that there is simply no effect or no difference between either two sample populations.

## Significance Testing



### P-value

The probability getting this distribution.


### Interpretation of significance

If the p-value is low and the $H_O$ is rejected, it doesn’t mean the $H_O$ is wrong. It means that there is **a small probability** to get the test statistic score if $H_O$ was true.

#### Upper, Lower, two-tailed tests

[slides](slides/06-1-hypothesis-testing.pdf#page=9)

![](assets/upper-lower-two-tailed.png)

## One sample z-test

Z distribution (standard normal distribution)

have entire population

## One sample t-test

have the sample values.

## inferences for two population means

### unpaired
  
$\overline{X}-\overline{Y} \sim N[\mu_X -\mu_Y, (\sigma_X^2/n_X+\sigma_Y^2/n_Y)]$


### paired

D for difference

$t*=\frac{\overline{X}_D-D_0}{S_D/\sqrt{n}}$
  - $X_D = X_A - X_B$ so $\overline{X_D} = \overline{X_A} - \overline{X_B}$
  - $D_0 = 0$

#### Equal and Not equal Variance

For unpaired t-test

[slides](slides/06-1-hypothesis-testing.pdf#page=15)

## Type I II Errors

- Type I: reject but you should
- Type II: accept but you shouldn't

## Wilcoxon signed-rank test

non-parametric equivalent to a paired t-test

compare medians instead of means''

rank is normal distributed ?


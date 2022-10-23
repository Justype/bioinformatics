# Cheat Sheet

ML: make prediction using current datasets

| Type           | data              |
| :------------- | :---------------- |
| supervised     | labeled           |
| unsupervised   | no label          |
| semisupervised | partially labeled |

Steps

1. study data
2. select model
3. train it
4. apply model to predict

Main Challenges: algorithm and data source

# Machine Learning

    [Machine Learning is the] field of study that gives computers the ability to learn without being explicitly programmed.
    —Arthur Samuel, 1959

    A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.
    —Tom Mitchell, 1997

## Terminology

- *training set*
- *training instance* (*example*)
- *training data*
- *data mining* : discover pattern from a large amount of data

Spam Filter

## Good at

[Hands on ML Page 33](hands-on-machine-learning.pdf#page=33)

1. automatic evolve without intervention
2. solution require a lot of hand-tuning
3. too complex problems (for traditional approaches)
4. problems with no known algorithm
5. get insights about complex problems and big data

## Types

- under human supervision: *supervised*, *unsupervised*, *semisupervised*, *reinforcement learning*
- learn incrementally on the fly: *online*, *batch*
- comparing new data to known OR detect patterns and build model *instance-based*, *model-based*

[Hands on ML Page 34](hands-on-machine-learning.pdf#page=34)

### Supervised

most common types: 

1. *classification*: add class to each email (spam or ham)
2. *regression*: predict a *target* numeric value with a set of *features* called *predictors*: predict the price of a car with mileage, age, brand

most important supervised learning algorithms:

- k-Nearest Neighbors
- Linear Regression
- Logistic Regression
- Support Vector Machines (SVMs)
- Decision Tree and Random Forests
- Neural networks

### Unsupervised

most important unsupervised learning algorithms:

- Clustering
  - K-Means
  - DBSCAN
  - Hierarchical Cluster Analysis (HCA)
- Anomaly detection and novelty detection
  - One-class SVM
  - Isolation Forest
- Visualization and dimensionality reduction
  - Principal Component Analysis (PCA)
  - Kernel PCA
  - Locally-Linear Embedding (LLE)
  - t-distributed Stochastic Neighbor Embedding (t-SNE)
- Association rule learning
  - Apriori
  - Eclat

- Clustering: subdivide each group into smaller groups
- Visualization: preserve as much structure as they can => how data organized => may find unsuspected patterns.

#### Dimensionality Reduction

simplify the data without losing too much information

- merge several correlated features into one

benefits

1. run faster
2. less disk and memory occupation
3. perform better in some cases

#### Anomaly and Novelty Detection

- novelty detection: only normal data during training
- anomaly detection: more tolerant, small percentage of outliers

#### Association Rule Learning

find relations between attributes

- people who buy BBQ sauce and chips also tend to buy steak.

### Semisupervised

partially labeled training data.

Use case: Google Photo

1. clustering: find the different people
2. label: users label who they are


### Reinforcement Learning

- *agent*: the learning system
- *reward*: good results
- *penalty*: bad returns
- *policy*: the best strategy learned by itself

the agent learns things by itself

1. observe
2. act using policy
3. get results (reward or penalty)
4. update policy
5. continue 1-4 until an optimal policy

[Hands on ML Page 41](hands-on-machine-learning.pdf#page=41)

Example: AlphaGo

### Batch VS Online Learning

#### Batch Learning

also called *offline learning*

- system trained, then run **without learning anymore**
- if you want to update it, you should use full dataset (both new and old) to train it again. stop the old one and start the new one.
  - it can be performed automatically
  - train the data daily or weekly

#### Online Learning

train the system incrementally by feeding it data or by small groups (*mini batches*)

great for

- systems which receive data as a flow and need to adapt to change rapidly or autonomously (stock price)
- limited computing resources
- huge datasets: learn by pieces

cons:

- if bad data in, performance down
  - data from broken sensor
  - *monitor needed*
    - turn off learning while performance down
    - monitor input data

*out-of-core learning*: 

- huge datasets cannot fit in memory
- is done offline but called online learning
  - so online learning is actually *incremental learning*

*learning rate*: how fast should adapt to changing data

- too fast: forget old pattern
- too slow: inertia

### Instance-Based VS Model-Based Learning

[Hands on ML Page 44](hands-on-machine-learning.pdf#page=44)

how ML systems generalize

#### Instance-Based Learning

measure of similarity => compare new cases to learned examples

- spam filter: number of words in common

#### Model-Based Learning

generalize from examples to a model => use that model to predict

- *model selection*: select a model to interpret examples
- *utility function (fitness function)*: to measure how good the model is
- *cost function*: how bad the model is
- *training*: find parameters which make the model fits best to data
- if all went well, it will make good prediction. If not
  - use more attributes
  - get more or better data
  - more powerful model

Steps

1. study data
2. select model
3. train it
4. apply model to predict

## Main Challenges

1. Good Data
  - noise
  - bias
  - irrelevant features
2. Good algorithm
  - overfitting: regularization
  - underfitting
3. Testing

### Data

Good data source sometimes is more powerful than the model.

training set must be representative of the incoming data.

- *sampling noise* nonrepresentative data as a **result of chance**
- bias
  - sampling bias
  - nonresponse bias
- irrelevant features => use *feature engineering*
  - *feature selection*: 
  - *feature extraction*: combining features to one
  - new features by gathering new data

### Overfitting and Underfitting

#### Overfitting the Training Data

Happens when fitting relatively too complex model to the data. the model will consider the noise.

solutions

1. simplify the model: select model with fewer parameters
2. more training data
3. reduce noise (fix error, remove outliers)

Solution: regularization

occurs when model is too simple to learn the structure of data.

how to fix

1. powerful model with more parameters
2. better features
3. reducing the constraints on the model 
   - (e.g. reducing the regularization hyperparameter)

## Testing and Validation

split datasets into two:

- training set (80%)
- testing set (20%, depends on the size)

- *training error*: while training
- *generalization error*: while testing

errors and fitting

- if training error > generalization error
  - underfitting
- if training error < testing error
  - overfitting


### Hyperparameter Tuning and Model Selection

If not sure which model to choose. Just train all the models and test them.

Solution on generalization error is much higher than training

*holdout validation*: hold out part of the training set as *validation set* (aka dev set)

![holdout](https://www.oreilly.com/api/v2/epubs/9781098125967/files/assets/mls3_0125.png)

size of validation set:

- too small -> may select suboptimal model
- too big -> smaller remaining training set

solution: *cross validation*

- using many small validation sets
- model evaluated once per validation set, then trained on the rest of the data
- drawback: training time

### Data Mismatch

The data you got mismatches the production.

- like: web picture is different from those taken on mobile

If the training error < generalization error, two possible cause:

1. overfitting
2. data mismatch

determine which is the cause: *train-dev set* (drawn from training sets)

| cause       | train-dev | validation |
| :---------- | :-------- | :--------- |
| mismatch    | great     | poor       |
| overfitting | poor      | poor       |


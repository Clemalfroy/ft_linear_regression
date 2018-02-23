
# SUBJECT of : ft_linear_regression

## An introduction to machine learning

_Résumé: In this project, you will implement your first machine learning algorithm._


## Table des matières

- #### I Préambule
- #### II Introduction
- #### III Objective
- #### IV General instructions
- #### V What you have to do
- #### VI Bonuses
- #### VII Peer-evaluation


# Chapitre I

# Préambule

“A computer program is said to learn from experience E with respect to some
class of tasks T and performance measure P, if its performance at tasks in
T, as measured by P, improves with experience E.”

```
Tom M. Mitchell
```

# Chapitre II

# Introduction

Machine learning is a growing field of computer science that may seem a bit compli-
cated and reserved only to mathematicians. You may have heard of neural networks or
k-means clustering and don’t undersdand how they work or how to code these kinds of
algorithms...

But don’t worry, we are actually going to start with a simple, basic machine learning
algorithm.


# Chapitre III

# Objective

The aim of this project is to introduce you to the basic concept behind machine lear-
ning. For this project, you will have to create a program that predicts the price of a car
by using a linear function train with a gradient descent algorithm.

We will work on a precise example for the project, but once you’re done you will be
able to use the algorithm with any other dataset.


# Chapitre IV

# General instructions

```
In this project you are free to use whatever language you want.
```
You are also free to use any libraries you want as long as they do not do all the work
for you. For example, the use of python’s numpy.polyfit is considered cheating.

```
You should use a language that allows you to easily visualize your
data : it will be very helpful for debugging.
```

# Chapitre V

# What you have to do

You will implement a simple linear regression with a single feature - in this case, the
mileage of the car.

```
To do so, you need to create two programs :
```
- The first program will be used to predict the price of a car for a given mileage.
    When you launch the program, it should prompt you for a mileage, and then give
    you back the estimated price for that mileage. The program will use the following
    hypothesis to predict the price :

```
estimatePrice ( mileage ) = θ 0 + ( θ 1 * mileage )
```

```
Before the run of the training program, theta0 and theta1 will be set to 0.
```
- The second program will be used to train your model. It will read your dataset
    file and perform a linear regression on the data.
    Once the linear regression has completed, you will save the variables theta0 and
    theta1 for use in the first program.
    
# Chapitre VI

# Bonuses

```
Here are some bonuses that could be very useful :
```
- Plotting the data into a graph to see their repartition.
- Plotting the line resulting from your linear regression into the same graph, to see
    the result of your hard work!
- A program that calculates the precision of your algorithm.

```
... and any other bonuses that make your program more awesome.
```

# Chapitre VII

# Peer-evaluation

Your program will be reviewed by humans only, so you are free to organize your files
whatever way you want.

```
Here are the points that your peer-corrector will have to check :
```
- The absence of libraries that do the work for you
- The use of the specified hypothesis
- The use of the specified training function



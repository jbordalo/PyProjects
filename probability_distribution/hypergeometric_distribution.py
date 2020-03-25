from math import sqrt
import sys

# CONSTANTS
E = "="
LT = "<"
GT = ">"
LET = "<="
GET = ">="
ACCURACY = 6

# MATH PREREQUISITES

def fact (x):
    if (x == 0): return 1
    return x * fact(x-1)

print (fact(30))

def combinations(n, k):
    return fact(n) / (fact(k) * fact(n-k))

# DOMAIN FUNCTIONS

def hyperProb (population, successes, sample, x):
    return combinations(successes, x)*combinations(population-successes, sample-x)/combinations(population, sample)

def lesserProb (population, successes, sample, x):
    prob = 0
    for i in range(x):
         prob += hyperProb(population, successes, sample, i)
    return prob

def lesserEqualProb (population, successes, sample, x):
    prob = hyperProb(population, successes, sample, x)
    for i in range(x):
         prob += hyperProb(population, successes, sample, i)
    return prob

def greaterProb (population, successes, sample, x):
    prob = 0
    for i in range(x, min(sample, successes)):
         prob += hyperProb(population, successes, sample, i+1)
    return prob

def greaterEqualProb (population, successes, sample, x):
    prob = hyperProb(population, successes, sample, x)
    for i in range(x, min(sample, successes)):
         prob += hyperProb(population, successes, sample, i+1)
    return prob

def expectedValue (population, successes, sample):
    return sample*successes/population

def variance (population, successes, sample):
    return expectedValue(population, successes, sample)*((population-successes)/population)*((population-sample)/(population-1))

def standardDeviation (population, successes, sample):
    return sqrt(variance(population, successes, sample))

# GUI FUNCTIONS

def notation (population, successes, sample):
    return "X~H({},{},{})".format(population, successes, sample)

def hyperProbString(op, value):
    return "P(X{}x)={}".format(op, round(value, ACCURACY))

# OUTPUT

# N = int(input("Population, N: "))
# M = int(input("Successes, M: "))
# n = int(input("Sample, n: "))
# x = int(input("x: "))

def show (N, M, n, x):
    print(hyperProbString(E, hyperProb(N, M, n, x)))
    print(hyperProbString(LT ,lesserProb(N, M, n, x)))
    print(hyperProbString(LET ,lesserEqualProb(N, M, n, x)))
    print(hyperProbString(GT ,greaterProb(N, M, n, x)))
    print(hyperProbString(GET ,greaterEqualProb(N, M, n, x)))
    print("Expected Value, E(X)={}".format(round(expectedValue(N, M, n), ACCURACY)))
    print("Variance, V(X)={}".format(round(variance(N, M, n), ACCURACY)))
    print("Standard Deviation, σ(X)={}".format(round(standardDeviation(N, M, n), ACCURACY)))

"""
TODO:
Failing when samples > value
"""

def main():
    if (len(sys.argv) != 4):
        print("<usage>: _.py population successes sample")
        return 1
    N = int(sys.argv[1])
    M = int(sys.argv[2])
    n = int(sys.argv[3])

    print(notation(N, M, n))

    while (True):
        x = int(input("x: "))
        if (x > n):
            print("The number of samples must be smaller than the number of sample successes.")
        elif (x > M):
            print("The number of successes in the sample must be less than or equal to the number of successes in the population.")
        else:
            show(N, M, n, x)

main()

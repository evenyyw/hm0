import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import pandas as pandas
import platform

# enter your name, e-mail address and github id below
YOUR_NAME = 'John Smith'
YOUR_EMAIL = 'john.smith@yale.edu'
YOUR_GITHUB_ID = 'jsmith123'

#######################################################
# sample from a standard normal distribution to test numpy
sample = np.random.normal(loc=0, scale=1, size=1000)

# calculate the mean and standard deviation of these samples to test pandas
series = pandas.Series(sample)
print('Mean:', series.mean())
print('Standard Deviation:', series.std())

# print the cdf of a normal distribution at 0 to test scipy
print('The standard normal distribution at x=0:', norm.cdf(0))

# draw histogram to test mathplotlib
plt.hist(sample, bins='auto')
plt.title(YOUR_NAME + '\n'+YOUR_EMAIL + ', @'+YOUR_GITHUB_ID + '\nPython version: ' + platform.python_version())
plt.savefig(YOUR_NAME+'.png')


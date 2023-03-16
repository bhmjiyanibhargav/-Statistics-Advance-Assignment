#!/usr/bin/env python
# coding: utf-8

# # question 01
What is Estimation Statistics? Explain point estimate and interval estimate.
Estimation statistics is a branch of statistics that deals with estimating population parameters from sample statistics. In other words, it is a set of techniques used to estimate unknown values or characteristics of a population based on information obtained from a sample.

Point estimate refers to a single numerical value that is used to estimate an unknown population parameter. For example, if we want to estimate the population mean from a sample, the sample mean would be a point estimate of the population mean. Similarly, if we want to estimate the population proportion of a certain characteristic, the sample proportion would be a point estimate of the population proportion.

Interval estimate, on the other hand, refers to a range of values that is used to estimate an unknown population parameter. The range is defined by a lower and an upper bound, which are calculated using the sample statistics and a certain level of confidence. The level of confidence is a measure of how confident we are that the true population parameter lies within the interval estimate. The most commonly used level of confidence is 95%, which means that we are 95% confident that the true population parameter lies within the interval estimate.

Interval estimate is more informative than point estimate, as it provides a range of plausible values for the population parameter, instead of a single value. However, interval estimate is generally less precise than point estimate, as it has a wider range of values. The width of the interval estimate depends on the sample size, the level of confidence, and the variability of the population. As the sample size increases, the width of the interval estimate decreases, and as the level of confidence increases, the width of the interval estimate increases.
# # question 02
Write a Python function to estimate the population mean using a sample mean and standard
deviation.
# In[1]:


import math

def estimate_population_mean(sample_mean, sample_std_dev, sample_size):
    # calculate the standard error of the mean
    std_error = sample_std_dev / math.sqrt(sample_size)
    
    # calculate the lower and upper bounds of the interval estimate with a 95% confidence level
    lower_bound = sample_mean - 1.96 * std_error
    upper_bound = sample_mean + 1.96 * std_error
    
    # return the interval estimate
    return (lower_bound, upper_bound)


# # question 03
What is Hypothesis testing? Why is it used? State the importance of Hypothesis testing.
Hypothesis testing is a statistical method used to make inferences about a population based on a sample. It involves testing a null hypothesis and an alternative hypothesis using sample data and a specified level of significance.

In hypothesis testing, the null hypothesis is a statement or assumption about the population that is tested against an alternative hypothesis, which is the opposite of the null hypothesis. The goal of hypothesis testing is to determine whether there is enough evidence to reject the null hypothesis and accept the alternative hypothesis.

Hypothesis testing is used in many fields, including science, engineering, social sciences, and business. It is used to test a wide range of research questions, such as whether a new drug is effective, whether a marketing campaign is successful, or whether a new manufacturing process is efficient.

The importance of hypothesis testing lies in its ability to provide a formal and objective approach to testing research questions. By using statistical methods to analyze data, researchers can make informed decisions based on evidence rather than intuition or personal biases. Hypothesis testing also allows researchers to quantify the level of uncertainty associated with their conclusions and to assess the strength of the evidence supporting their hypotheses.

In addition, hypothesis testing is an essential component of the scientific method, as it helps to ensure that scientific research is rigorous, reliable, and reproducible. It provides a framework for testing hypotheses and making conclusions based on evidence, which is critical for advancing scientific knowledge and improving our understanding of the world around us.
# # question 04
Create a hypothesis that states whether the average weight of male college students is greater than
the average weight of female college students.
Null Hypothesis: The average weight of male college students is not significantly different from the average weight of female college students.

Alternative Hypothesis: The average weight of male college students is significantly greater than the average weight of female college students.

Symbolically, this can be represented as:

H0: μmale = μfemale

Ha: μmale > μfemale

Where H0 represents the null hypothesis and Ha represents the alternative hypothesis, and μ represents the population mean weight of male and female college students, respectively.
# # question 05
Write a Python script to conduct a hypothesis test on the difference between two population means,
given a sample from each population.
# In[2]:


import numpy as np
from scipy import stats

# Define the two populations
pop1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pop2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Take random samples from each population
sample1 = np.random.choice(pop1, size=5, replace=False)
sample2 = np.random.choice(pop2, size=5, replace=False)

# Compute the sample means and variances
mean1 = np.mean(sample1)
mean2 = np.mean(sample2)
var1 = np.var(sample1, ddof=1)
var2 = np.var(sample2, ddof=1)

# Compute the test statistic and p-value using a two-sample t-test
t_stat, p_val = stats.ttest_ind(sample1, sample2, equal_var=False)

# Set the significance level
alpha = 0.05

# Print the results of the hypothesis test
print("Sample 1 mean: ", mean1)
print("Sample 2 mean: ", mean2)
print("Sample 1 variance: ", var1)
print("Sample 2 variance: ", var2)
print("Test statistic: ", t_stat)
print("p-value: ", p_val)

if p_val < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
import numpy as np
from scipy import stats

# Define the two populations
pop1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pop2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Take random samples from each population
sample1 = np.random.choice(pop1, size=5, replace=False)
sample2 = np.random.choice(pop2, size=5, replace=False)

# Compute the sample means and variances
mean1 = np.mean(sample1)
mean2 = np.mean(sample2)
var1 = np.var(sample1, ddof=1)
var2 = np.var(sample2, ddof=1)

# Compute the test statistic and p-value using a two-sample t-test
t_stat, p_val = stats.ttest_ind(sample1, sample2, equal_var=False)

# Set the significance level
alpha = 0.05

# Print the results of the hypothesis test
print("Sample 1 mean: ", mean1)
print("Sample 2 mean: ", mean2)
print("Sample 1 variance: ", var1)
print("Sample 2 variance: ", var2)
print("Test statistic: ", t_stat)
print("p-value: ", p_val)

if p_val < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

    


# # question 06
What is a null and alternative hypothesis? Give some examples.
In statistical hypothesis testing, a null hypothesis and an alternative hypothesis are two opposing statements used to test a research question or hypothesis.

The null hypothesis (H0) is a statement that there is no significant difference between the sample data and the population, or that any observed difference between the sample and population data is due to chance or sampling error. In other words, the null hypothesis assumes that there is no effect or relationship between the variables being tested. The null hypothesis is usually denoted by H0.

The alternative hypothesis (Ha) is a statement that there is a significant difference or relationship between the sample data and the population, or that any observed difference is not due to chance or sampling error. In other words, the alternative hypothesis assumes that there is an effect or relationship between the variables being tested. The alternative hypothesis is usually denoted by Ha.

Here are some examples of null and alternative hypotheses:

Research question: Does a new medication reduce blood pressure?
Null hypothesis: The new medication does not reduce blood pressure.

Alternative hypothesis: The new medication reduces blood pressure.

Research question: Is there a difference in test scores between two groups of students?
Null hypothesis: There is no significant difference in test scores between the two groups of students.

Alternative hypothesis: There is a significant difference in test scores between the two groups of students.

Research question: Is there a relationship between age and income?
Null hypothesis: There is no relationship between age and income.

Alternative hypothesis: There is a relationship between age and income.

Research question: Does a new teaching method improve student performance?
Null hypothesis: The new teaching method does not improve student performance.

Alternative hypothesis: The new teaching method improves student performance.

In each of these examples, the null hypothesis assumes that there is no effect or relationship between the variables being tested, while the alternative hypothesis assumes that there is an effect or relationship. The choice of null and alternative hypotheses depends on the research question and the specific hypothesis being tested.
# # question 07
Write down the steps involved in hypothesis testing.
Here are the general steps involved in hypothesis testing:

State the research question: The first step in hypothesis testing is to clearly define the research question or problem that needs to be addressed.

Formulate the null and alternative hypotheses: The next step is to formulate the null and alternative hypotheses, which are opposing statements that will be tested using statistical methods.

Choose the appropriate statistical test: The choice of statistical test depends on the type of data being analyzed, the sample size, and the research question. Common statistical tests include t-tests, ANOVA, correlation analysis, and regression analysis.

Set the significance level: The significance level (alpha) is the threshold for accepting or rejecting the null hypothesis. Typically, alpha is set to 0.05 or 0.01, which means that there is a 5% or 1% chance of rejecting the null hypothesis even if it is true.

Collect the data: Data must be collected in a way that minimizes bias and is representative of the population of interest.

Calculate the test statistic and p-value: The test statistic measures the difference between the sample data and the null hypothesis, while the p-value measures the probability of observing the test statistic assuming the null hypothesis is true.

Make a decision: Based on the p-value and significance level, decide whether to reject or fail to reject the null hypothesis.

Interpret the results: If the null hypothesis is rejected, it means there is evidence to support the alternative hypothesis. If the null hypothesis is not rejected, it means there is not enough evidence to support the alternative hypothesis.

Draw conclusions and make recommendations: The final step is to draw conclusions based on the results of the hypothesis test and make recommendations for further research or action.

These steps may vary slightly depending on the research question, the type of data being analyzed, and the statistical test used, but the general framework remains the same.
# # question 08
Define p-value and explain its significance in hypothesis testing.
In statistical hypothesis testing, the p-value is a measure of the evidence against the null hypothesis. Specifically, the p-value is the probability of obtaining a test statistic as extreme or more extreme than the observed value, assuming the null hypothesis is true.

If the p-value is very small (usually less than the significance level, which is often set to 0.05), it suggests that the observed data is unlikely to have occurred by chance if the null hypothesis is true. This means that we reject the null hypothesis and conclude that there is evidence to support the alternative hypothesis. On the other hand, if the p-value is not small (greater than the significance level), it suggests that the observed data is likely to have occurred by chance if the null hypothesis is true. This means that we fail to reject the null hypothesis and conclude that there is not enough evidence to support the alternative hypothesis.

The p-value is an important tool in hypothesis testing because it provides a quantitative measure of the strength of evidence against the null hypothesis. It helps to ensure that conclusions are based on objective evidence rather than subjective interpretation. In addition, the p-value can be used to compare the results of different studies or experiments, as it provides a standardized measure of the strength of evidence against the null hypothesis. However, it is important to note that the p-value alone does not provide conclusive evidence, and should be considered along with other factors such as effect size, sample size, and study design.
# # question 09
Generate a Student's t-distribution plot using Python's matplotlib library, with the degrees of freedom
parameter set to 10.
# In[3]:


import numpy as np
import matplotlib.pyplot as plt

# Set degrees of freedom
df = 10

# Generate x values for t-distribution plot
x = np.linspace(-4, 4, 1000)

# Calculate y values for t-distribution plot
y = stats.t.pdf(x, df)

# Create plot
plt.plot(x, y, label=f"df = {df}")

# Add plot details
plt.xlabel("t-value")
plt.ylabel("Probability density")
plt.title("Student's t-distribution")
plt.legend()

# Show plot
plt.show()


# # question 10
Write a Python program to calculate the two-sample t-test for independent samples, given two
random samples of equal size and a null hypothesis that the population means are equal.
# In[4]:


import numpy as np
from scipy.stats import ttest_ind

# Generate two random samples with equal size
sample1 = np.random.normal(5, 1, 100)
sample2 = np.random.normal(6, 1, 100)

# Calculate the two-sample t-test
t_statistic, p_value = ttest_ind(sample1, sample2)

# Print the results
print("Two-Sample t-test Results:")
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")
if p_value < 0.05:
    print("Reject null hypothesis: Population means are not equal.")
else:
    print("Fail to reject null hypothesis: Population means may be equal.")


# # question 11
Q11: What is Student’s t distribution? When to use the t-Distribution.
Student's t-distribution is a probability distribution that arises in hypothesis testing when the sample size is small (typically less than 30) and the population standard deviation is unknown. It is named after William Gosset, who wrote under the pseudonym "Student" when he published the distribution in 1908.

The t-distribution is similar to the standard normal distribution (i.e., the Z-distribution) in shape, but with slightly fatter tails. The shape of the distribution depends on the degrees of freedom (df), which is determined by the sample size. As the sample size increases, the t-distribution approaches the standard normal distribution.

The t-distribution is used when we want to test a hypothesis about the mean of a population based on a sample, but the population standard deviation is unknown. Specifically, it is used when:

The sample size is small (less than 30).
The population standard deviation is unknown.
The population is normally distributed or the sample size is large enough to use the central limit theorem.
The t-distribution allows us to calculate the probability of observing a particular sample mean if the null hypothesis (e.g., the population mean is equal to a specified value) is true. This probability, known as the p-value, can then be compared to a significance level (e.g., 0.05) to determine whether the null hypothesis should be rejected or not.
# # question 12
What is t-statistic? State the formula for t-statistic.
In hypothesis testing, the t-statistic is a test statistic that is used to determine whether there is a significant difference between the means of two groups or between the mean of a sample and a known population mean, when the population standard deviation is unknown.

The formula for the t-statistic depends on the specific scenario being tested, but in general it can be expressed as:

t = (x̄ - μ) / (s / √n)

where:

x̄ is the sample mean
μ is the population mean (the hypothesized value being tested)
s is the sample standard deviation
n is the sample size
Essentially, the t-statistic measures the difference between the sample mean and the hypothesized population mean, relative to the variability in the sample. If the difference between the sample mean and the hypothesized population mean is large relative to the variability in the sample (i.e., the standard error of the mean), then the t-statistic will be large, indicating that the observed difference is unlikely to have occurred by chance alone.

The t-statistic follows a t-distribution, with the number of degrees of freedom determined by the sample size. The p-value associated with the t-statistic can be calculated using a t-table or a statistical software package, and can be compared to a predetermined significance level (e.g., 0.05) to determine whether the null hypothesis should be rejected or not.
# # question 13
A coffee shop owner wants to estimate the average daily revenue for their shop. They take a random
sample of 50 days and find the sample mean revenue to be $500 with a standard deviation of $50.
Estimate the population mean revenue with a 95% confidence interval.A coffee shop owner wants to estimate the average daily revenue for their shop. They take a random
sample of 50 days and find the sample mean revenue to be $500 with a standard deviation of $50.
Estimate the population mean revenue with a 95% confidence interval.
To estimate the population mean revenue with a 95% confidence interval, we can use the following formula:

CI = X̄ ± t*(s/√n)

where:

X̄ is the sample mean revenue ($500)
s is the sample standard deviation ($50)
n is the sample size (50)
t is the critical value from the t-distribution, based on the desired confidence level and degrees of freedom (df = n-1)
Since we want a 95% confidence interval and we have a sample size of 50, the degrees of freedom is 49. We can look up the critical value from a t-table or use a statistical software package, which gives us a value of 2.0096.

Substituting these values into the formula, we get:

CI = $500 ± 2.0096*($50/√50)
= $500 ± $14.14

Therefore, we can say with 95% confidence that the true population mean revenue falls within the interval of $485.86 to $514.14. This means that if we were to take many random samples of 50 days and calculate a 95% confidence interval for each sample, about 95% of those intervals would contain the true population mean revenue.
# # question 14
A researcher hypothesizes that a new drug will decrease blood pressure by 10 mmHg. They conduct a
clinical trial with 100 patients and find that the sample mean decrease in blood pressure is 8 mmHg with a
standard deviation of 3 mmHg. Test the hypothesis with a significance level of 0.05.
To test the hypothesis that the new drug decreases blood pressure by 10 mmHg, we can use a one-sample t-test with the following null and alternative hypotheses:

Null hypothesis (H0): The true mean decrease in blood pressure is equal to 10 mmHg.
Alternative hypothesis (Ha): The true mean decrease in blood pressure is less than 10 mmHg.
We can use a significance level of 0.05, which means we are willing to reject the null hypothesis if the probability of obtaining our sample results under the null hypothesis is less than 0.05.

The test statistic for a one-sample t-test can be calculated as:

t = (X̄ - μ) / (s/√n)

where:

X̄ is the sample mean decrease in blood pressure (8 mmHg)
μ is the hypothesized mean decrease in blood pressure (10 mmHg, from the null hypothesis)
s is the sample standard deviation (3 mmHg)
n is the sample size (100)
Substituting these values, we get:

t = (8 - 10) / (3/√100) = -2.82

The degrees of freedom for this test are n-1 = 99. Using a t-table or a statistical software package, we can find the critical value for a one-tailed test with 99 degrees of freedom and a significance level of 0.05, which is -1.660.

Since our test statistic (-2.82) is less than the critical value (-1.660), we reject the null hypothesis. This means that we have evidence to suggest that the true mean decrease in blood pressure with the new drug is less than 10 mmHg, which supports the researcher's hypothesis.
# # question `15
An electronics company produces a certain type of product with a mean weight of 5 pounds and a
standard deviation of 0.5 pounds. A random sample of 25 products is taken, and the sample mean weight
is found to be 4.8 pounds. Test the hypothesis that the true mean weight of the products is less than 5
pounds with a significance level of 0.01.
To test the hypothesis that the true mean weight of the products is less than 5 pounds, we can use a one-sample t-test with the following null and alternative hypotheses:

Null hypothesis (H0): The true mean weight of the products is equal to 5 pounds.
Alternative hypothesis (Ha): The true mean weight of the products is less than 5 pounds.
We can use a significance level of 0.01, which means we are willing to reject the null hypothesis if the probability of obtaining our sample results under the null hypothesis is less than 0.01.

The test statistic for a one-sample t-test can be calculated as:

t = (X̄ - μ) / (s/√n)

where:

X̄ is the sample mean weight (4.8 pounds)
μ is the hypothesized mean weight (5 pounds, from the null hypothesis)
s is the sample standard deviation (0.5 pounds)
n is the sample size (25)
Substituting these values, we get:

t = (4.8 - 5) / (0.5/√25) = -2.0

The degrees of freedom for this test are n-1 = 24. Using a t-table or a statistical software package, we can find the critical value for a one-tailed test with 24 degrees of freedom and a significance level of 0.01, which is -2.492.

Since our test statistic (-2.0) is greater than the critical value (-2.492), we fail to reject the null hypothesis. This means that we do not have enough evidence to suggest that the true mean weight of the products is less than 5 pounds, and we conclude that the sample data is consistent with the hypothesis that the true mean weight is 5 pounds.
# # question 16
Q16. Two groups of students are given different study materials to prepare for a test. The first group (n1 =
30) has a mean score of 80 with a standard deviation of 10, and the second group (n2 = 40) has a mean
score of 75 with a standard deviation of 8. Test the hypothesis that the population means for the two
groups are equal with a significance level of 0.01.
To test the hypothesis that the population means for the two groups are equal, we can use a two-sample t-test with unequal variances. The null hypothesis is that the population means are equal, while the alternative hypothesis is that they are not equal.

The test statistic for this hypothesis test is calculated as:

t = (x̄1 - x̄2) / sqrt((s1^2/n1) + (s2^2/n2))

Where x̄1 and x̄2 are the sample means for the first and second groups, s1 and s2 are the sample standard deviations for the first and second groups, and n1 and n2 are the sample sizes for the first and second groups.

Using the given values, we get:

t = (80 - 75) / sqrt((10^2/30) + (8^2/40))
t = 2.51

The degrees of freedom for the t-distribution are calculated as:

df = ((s1^2/n1 + s2^2/n2)^2) / ((s1^2/n1)^2 / (n1 - 1) + (s2^2/n2)^2 / (n2 - 1))

Using the given values, we get:

df = ((10^2/30 + 8^2/40)^2) / ((10^2/30)^2 / 29 + (8^2/40)^2 / 39)
df = 64.8 (rounded to the nearest integer)

Using a significance level of 0.01 and the calculated degrees of freedom, we can find the critical value of t using a t-distribution table or a calculator. For a two-tailed test, the critical values are ±2.64.

Since our calculated t-value of 2.51 is within the range of -2.64 to 2.64, we fail to reject the null hypothesis. We do not have enough evidence to conclude that the population means for the two groups are not equal at the 0.01 significance level.
# # question 17
A marketing company wants to estimate the average number of ads watched by viewers during a TV
program. They take a random sample of 50 viewers and find that the sample mean is 4 with a standard
deviation of 1.5. Estimate the population mean with a 99% confidence interval.
To estimate the population mean with a 99% confidence interval, we can use the following formula:

Confidence interval = sample mean ± (z-value) x (standard error)

where the standard error is calculated as the standard deviation of the sample divided by the square root of the sample size.

The z-value corresponds to the level of confidence and can be obtained from the standard normal distribution table. For a 99% confidence interval, the z-value is 2.576.

Using the values given in the problem, we have:

sample mean (x̄) = 4
sample standard deviation (s) = 1.5
sample size (n) = 50

Therefore, the standard error is:

standard error = s / sqrt(n) = 1.5 / sqrt(50) = 0.2121 (rounded to four decimal places)

Now we can calculate the confidence interval:

Confidence interval = 4 ± (2.576) x (0.2121)
Confidence interval = 4 ± 0.5463

Thus, the 99% confidence interval for the population mean number of ads watched by viewers during a TV program is (3.4537, 4.5463). We can interpret this as follows: if we take repeated samples of size 50 from the population and calculate the 99% confidence intervals each time, we would expect that approximately 99% of those intervals would contain the true population mean.
# In[ ]:





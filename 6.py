#6. Perform univariate analysis on a dataset containing information about the performance of students in a school.
#The dataset includes variables such as student ID, test scores in different subjects, attendance, 
#and socio-economic background. Use Python to analyze the distribution of test scores in each subject separately.
#Calculate the mean, median, and standard deviation for each subject and visualize the distribution using box plots.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_performance.csv")

math_scores = df['math score']
reading_scores = df['reading score']

math_mean = math_scores.mean()
math_median = math_scores.median()
math_std = math_scores.std()

reading_mean = reading_scores.mean()
reading_median = reading_scores.median()
reading_std = reading_scores.std()

print("Math Scores:")
print("Mean:", math_mean)
print("Median:", math_median)
print("Standard Deviation:", math_std)
print("\nReading Scores:")
print("Mean:", reading_mean)
print("Median:", reading_median)
print("Standard Deviation:", reading_std)

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['math score', 'reading score']])
plt.title('Distribution of Math and Reading Scores')
plt.xlabel('Subject')
plt.ylabel('Score')
plt.xticks(ticks=[0, 1], labels=['Math', 'Reading'])
plt.show()
